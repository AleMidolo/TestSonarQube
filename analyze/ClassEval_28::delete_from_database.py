def delete_from_database(self, table_name, name):
        """
        Elimina righe dalla tabella indicata del database con un nome corrispondente.
        :param table_name: str, il nome della tabella da cui eliminare le righe.
        :param name: str, il nome da abbinare per l'eliminazione.
        >>> db.delete_from_database('user', 'John')
        """
        
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(delete_query, (name,))
        
        conn.commit()
        conn.close()