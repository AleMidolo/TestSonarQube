def base_config(user, etcd_host="localhost", etcd_port=2379):
    """
    创建一个包含一些简单参数的配置，其中关键参数包括 "tls"、"authentication"、"authorization"、"etcd"、"docs" 和 "log"。

    创建一个包含一些简单参数的配置，这些参数具有默认值，可以根据需要进行设置。

    参数:
      user (str): 用于静态认证的用户名。
      etcd_host (str): 数据库的主机地址。
      etcd_port (int): 数据库的端口号。

    返回值:
      dict: 建的配置字典。
    """
    config = {
        "tls": {
            "enabled": False,
            "cert_file": "",
            "key_file": "",
            "ca_file": ""
        },
        "authentication": {
            "enabled": True,
            "type": "static",
            "static": {
                "users": {
                    user: {
                        "password": "default_password"
                    }
                }
            }
        },
        "authorization": {
            "enabled": True,
            "type": "simple",
            "rules": []
        },
        "etcd": {
            "endpoints": [f"http://{etcd_host}:{etcd_port}"],
            "dial_timeout": 5,
            "request_timeout": 5
        },
        "docs": {
            "enabled": True,
            "path": "/docs"
        },
        "log": {
            "level": "info",
            "format": "text",
            "output": "stdout"
        }
    }
    
    return config