def validate_input(text: str) -> bool:
    """
    Valida que el texto no esté vacío.
    """
    return bool(text and text.strip())


def format_text(text: str) -> str:
    """
    Formatea el texto: elimina espacios y capitaliza.
    """
    return text.strip().capitalize()
