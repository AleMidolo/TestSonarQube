def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    Trova i tag nel testo.

    Cerca di ignorare i tag all'interno dei blocchi di codice.

    Facoltativamente, se viene passato un "replacer", sostituirà anche la parola del tag con il risultato della funzione "replacer" chiamata con la parola del tag.

    Restituisce un set di tag e il testo originale o modificato.
    """
    tags = set()
    modified_text = text
    in_code_block = False
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for code block markers
        if line.strip().startswith('