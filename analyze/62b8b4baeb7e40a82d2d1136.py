from zope.interface import Invalid
from zope.interface.verify import verifyObject, verifyClass

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
    if vtype == 'class':
        verifyClass(iface, candidate, tentative=tentative)
    else:
        verifyObject(iface, candidate, tentative=tentative)
    return True