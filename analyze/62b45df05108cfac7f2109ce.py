def validate(self, path):
    """
    Valida el objeto OCFL en la ruta o en la raíz de pyfs.

    Devuelve True si es válido (se permiten advertencias), False en caso contrario.
    """
    try:
        # Verificar que existe el directorio
        if not self.fs.exists(path):
            return False
            
        # Verificar archivo de inventario
        inventory_path = f"{path}/inventory.json"
        if not self.fs.exists(inventory_path):
            return False
            
        # Leer y validar el inventario
        with self.fs.open(inventory_path) as f:
            inventory = json.load(f)
            
        # Verificar campos requeridos del inventario
        required_fields = ['id', 'type', 'digestAlgorithm', 'head', 'versions']
        for field in required_fields:
            if field not in inventory:
                return False
                
        # Verificar que el tipo sea correcto
        if inventory['type'] != 'https://ocfl.io/1.0/spec/#inventory':
            return False
            
        # Verificar que existe el directorio de cada versión
        for version in inventory['versions']:
            version_path = f"{path}/{version}"
            if not self.fs.exists(version_path):
                return False
                
        # Verificar checksums de los archivos
        for version in inventory['versions'].values():
            for file_path, digest in version['state'].items():
                full_path = f"{path}/{file_path}"
                if not self.fs.exists(full_path):
                    return False
                    
                # Verificar checksum del archivo
                with self.fs.open(full_path, 'rb') as f:
                    file_content = f.read()
                    if inventory['digestAlgorithm'].lower() == 'sha256':
                        calculated_digest = hashlib.sha256(file_content).hexdigest()
                    elif inventory['digestAlgorithm'].lower() == 'sha512':
                        calculated_digest = hashlib.sha512(file_content).hexdigest()
                    else:
                        return False
                        
                if calculated_digest != digest:
                    return False
                    
        return True
        
    except Exception:
        return False