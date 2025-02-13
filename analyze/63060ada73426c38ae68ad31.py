def _convert_non_cli_args(self, parser_name, values_dict):
    for key, value in values_dict.items():
        if value.isdigit():
            values_dict[key] = int(value)
        else:
            try:
                float_value = float(value)
                values_dict[key] = float_value
            except ValueError:
                pass  # Keep the value as string if it cannot be converted
    return values_dict