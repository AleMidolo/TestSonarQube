def _get_conditionally_required_args(self, command_name, options_spec, args):
    conditionally_required = []
    
    for option in options_spec:
        # Check if option has required_when condition
        if 'required_when' in option:
            required_when = option['required_when']
            
            # Get the dependent argument and expected value
            dependent_arg = required_when.get('arg')
            expected_value = required_when.get('value')
            
            # Check if dependent argument exists in provided args
            if dependent_arg in args:
                actual_value = args[dependent_arg]
                
                # If actual value matches expected value, this option becomes required
                if actual_value == expected_value:
                    conditionally_required.append(option['name'])
                    
    return conditionally_required