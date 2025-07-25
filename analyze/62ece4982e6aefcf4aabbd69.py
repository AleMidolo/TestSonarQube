def _replace_register(flow_params, register_number, register_value):
    """
    दिए गए रजिस्टर नंबर में फ्लो से मान को बदलें  

    डिक्शनरी में 'register_value' कुंजी को 'register_number' द्वारा दिए गए रजिस्टर नंबर से बदल दिया जाएगा  

    पैरामीटर विवरण:
    - flow_params: एक डिक्शनरी जिसमें परिभाषित फ्लो शामिल हैं  
    - register_number: वह रजिस्टर नंबर जिसमें मान संग्रहीत किया जाएगा  
    - register_value: वह कुंजी जिसे रजिस्टर नंबर द्वारा बदल दिया जाएगा
    """
    # Create a copy of the flow parameters dictionary
    new_flow_params = flow_params.copy()
    
    # Replace the register_value key with the register number
    if register_value in new_flow_params:
        value = new_flow_params[register_value]
        del new_flow_params[register_value]
        new_flow_params[f'R{register_number}'] = value
        
    return new_flow_params