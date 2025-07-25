from zope.interface import Invalid, providedBy, implementedBy
from inspect import signature, ismethod, isfunction

def _verify(iface, candidate, tentative=False, vtype=None):
    """
    验证 *candidate* 是否能够正确地提供 *iface*。

    这个过程包括以下步骤：

    - 确保候选对象声明其提供了接口，通过调用 ``iface.providedBy`` （如果 *tentative* 为真，则跳过此步骤）。这意味着候选对象的类必须声明 `implements <zope.interface.implementer>` 该接口，或者候选对象自身声明 `provides <zope.interface.provider>` 该接口。

    - 确保候选对象定义了所有必要的方法。

    - 确保这些方法具有正确的签名（在可能的范围内进行检查）。

    - 确保候选对象定义了所有必要的属性。

    :return bool: 如果所有可以检查的条件都通过，则返回真。
    :raises zope.interface.Invalid: 如果上述任何条件不满足

    .. versionchanged:: 5.0
        如果有多个方法或属性无效，将收集并报告所有这些错误。之前的行为是仅报告第一个错误。作为一个特殊情况，如果只有一个错误，则像之前一样单独抛出该错误。
    """
    errors = []

    # Step 1: Verify that the candidate declares it provides the interface
    if not tentative:
        if not iface.providedBy(candidate):
            errors.append(f"{candidate} does not declare that it provides {iface}")

    # Step 2: Verify that the candidate defines all required methods
    required_methods = iface.namesAndDescriptions(all=True)
    for name, desc in required_methods:
        if not hasattr(candidate, name):
            errors.append(f"{candidate} is missing required method {name}")
        else:
            attr = getattr(candidate, name)
            if not (ismethod(attr) or isfunction(attr)):
                errors.append(f"{name} is not a method or function in {candidate}")

    # Step 3: Verify that the methods have the correct signatures
    for name, desc in required_methods:
        if hasattr(candidate, name):
            try:
                sig = signature(getattr(candidate, name))
                iface_sig = signature(desc.getSignature())
                if sig != iface_sig:
                    errors.append(f"Signature mismatch for method {name} in {candidate}")
            except ValueError:
                # Skip if signature cannot be determined
                pass

    # Step 4: Verify that the candidate defines all required attributes
    required_attrs = iface.namesAndDescriptions(all=True)
    for name, desc in required_attrs:
        if not hasattr(candidate, name):
            errors.append(f"{candidate} is missing required attribute {name}")

    # Handle errors
    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid("\n".join(errors))

    return True