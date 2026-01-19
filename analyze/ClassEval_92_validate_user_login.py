def validate_user_login(self, username, password):
    """
    Determina se l'utente può accedere, ovvero se l'utente è nel database e la password è corretta
    :param username:str, il nome utente dell'utente da convalidare.
    :param password:str, la password dell'utente da convalidare.
    :return:bool, che rappresenta se l'utente può accedere correttamente
    >>> user_db = UserLoginDB("user_database.db")
    >>> user_db.create_table()
    >>> user_db.insert_user('user1', 'pass1')
    >>> user_db.validate_user_login('user1', 'pass1')
    True
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result is None:
        return False
    
    stored_password = result[0]
    return stored_password == password