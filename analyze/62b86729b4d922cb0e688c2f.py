def base_config(user, etcd_host="localhost", etcd_port=2379):
    config = {
        "tls": True,
        "authentication": {
            "user": user,
            "enabled": True
        },
        "authorization": {
            "enabled": True
        },
        "etcd": {
            "host": etcd_host,
            "port": etcd_port
        },
        "docs": "Configuration for the application",
        "log": {
            "level": "info",
            "file": "/var/log/app.log"
        }
    }
    return config