from typing import AnyStr, Union, Dict, Sequence, Tuple

def format(
                self,
                sql: AnyStr,
                params: Union[Dict[Union[str, int], Any], Sequence[Any]],
        ) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    Converte la query SQL per utilizzare i parametri in stile "out" invece dei parametri in stile "in".

    **sql** (:class:`str` o :class:`bytes`) è la query SQL.

    Restituisce una :class:`tuple` contenente:

    - La query SQL formattata (:class:`str` o :class:`bytes`).

    - L'insieme dei parametri convertiti in stile "out" (:class:`dict` o :class:`list`).
    """
    if isinstance(sql, bytes):
        sql_str = sql.decode('utf-8')
    else:
        sql_str = sql

    if isinstance(params, dict):
        out_params = {key: f'OUT_{value}' for key, value in params.items()}
    elif isinstance(params, list):
        out_params = [f'OUT_{value}' for value in params]
    else:
        raise TypeError("params must be a dict or a list")

    formatted_sql = sql_str.replace("?", "%s")  # Example of converting placeholders
    return formatted_sql, out_params