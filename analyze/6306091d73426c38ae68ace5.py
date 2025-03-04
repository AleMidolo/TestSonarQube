def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if not parser_dict:
        return {}
        
    result = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            if 'include' in value:
                # Get included dictionary name
                include_name = value['include']
                
                # Look up included dictionary in self.groups
                if include_name in self.groups:
                    included_dict = self.groups[include_name]
                    # Merge included dict with current dict
                    merged = included_dict.copy()
                    merged.update(value)
                    # Remove include directive
                    del merged['include']
                    result[key] = merged
                else:
                    raise KeyError(f"Group '{include_name}' not found for inclusion")
            else:
                # Recursively process nested dictionaries
                result[key] = self._include_groups(value)
        else:
            result[key] = value
            
    return result