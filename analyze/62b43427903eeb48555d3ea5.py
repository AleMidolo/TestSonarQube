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
    # Convert the SQL query and parameters to use "out" style
    if isinstance(sql, bytes):
        formatted_sql = sql.decode('utf-8')
    else:
        formatted_sql = sql

    if isinstance(params, dict):
        out_params = {key: f'${key}' for key in params}
    else:
        out_params = [f'${i}' for i in range(len(params))]

    return formatted_sql, out_params