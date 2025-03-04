def base_config(user, etcd_host="localhost", etcd_port=2379):
    """
    Crea una configurazione con alcuni parametri semplici, che hanno un valore predefinito che può essere impostato.

    Argomenti:
    user (str): il nome dell'utente per l'autenticazione statica.
    etcd_host (str): l'host per il database.
    etcd_port (int): la porta per il database.

    Ritorna:
    dict: la configurazione creata.
    """
    config = {
        "user": user,
        "database": {
            "host": etcd_host,
            "port": etcd_port
        },
        "auth": {
            "type": "static",
            "username": user
        }
    }
    
    return config