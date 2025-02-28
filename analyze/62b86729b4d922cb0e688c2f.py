def base_config(user, etcd_host="localhost", etcd_port=2379):
    """
    Crea una configuración con algunos parámetros simples, los cuales tienen un valor predeterminado que puede ser configurado.

    Argumentos:
    user (str): el nombre del usuario para la autenticación estática.
    etcd_host (str): el host para la base de datos.
    etcd_port (int): el puerto para la base de datos.

    Retorna:
    dict: la configuración creada.
    """
    config = {
        "user": user,
        "etcd_host": etcd_host,
        "etcd_port": etcd_port
    }
    return config