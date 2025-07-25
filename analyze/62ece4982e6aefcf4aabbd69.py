def _replace_register(flow_params, register_number, register_value):
    """
    दिए गए रजिस्टर नंबर में फ्लो से मान को बदलें  

    डिक्शनरी में 'register_value' कुंजी को 'register_number' द्वारा दिए गए रजिस्टर नंबर से बदल दिया जाएगा  

    पैरामीटर विवरण:
    - flow_params: एक डिक्शनरी जिसमें परिभाषित फ्लो शामिल हैं  
    - register_number: वह रजिस्टर नंबर जिसमें मान संग्रहीत किया जाएगा  
    - register_value: वह कुंजी जिसे रजिस्टर नंबर द्वारा बदल दिया जाएगा  
    """
    flow_params[register_number] = register_value
    return flow_params