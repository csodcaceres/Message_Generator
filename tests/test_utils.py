#from src.generator.utils import validate_input, format_text 
from generator.utils import validate_input, format_text

import pytest

# --- Tests para validate_input ---

def test_validate_input_valid_text():
    """Prueba que la función retorne True para una cadena de texto válida."""
    assert validate_input("Oscar") is True

def test_validate_input_with_extra_spaces():
    """Prueba que retorne True para texto con espacios iniciales/finales."""
    assert validate_input("    Hola Mundo    ") is True

def test_validate_input_empty_string():
    """Prueba que la función retorne False para una cadena vacía."""
    assert validate_input("") is False

def test_validate_input_only_spaces():
    """Prueba que retorne False para una cadena que solo contiene espacios."""
    assert validate_input("          ") is False

def test_validate_input_none_value():
    """Prueba que retorne False si la entrada es None (aunque el Type Hint sugiera str, es bueno cubrirlo)."""
    # Pytest puede esperar que esto falle si se usa type checking estricto, 
    # pero para el propósito de validar entrada, si text es None, evalúa a False.
    assert validate_input(None) is False


# --- Tests para format_text ---

def test_format_text_basic_capitalization():
    """Prueba el formateo estándar (capitalización)."""
    assert format_text("programacion") == "Programacion"

def test_format_text_handles_pre_formatted():
    """Prueba que maneje texto que ya tiene mayúscula inicial."""
    assert format_text("Programacion") == "Programacion"

def test_format_text_strips_leading_and_trailing_spaces():
    """Prueba que elimine espacios al inicio y al final antes de capitalizar."""
    assert format_text("       python      ") == "Python"

def test_format_text_handles_empty_string():
    """Prueba que una cadena vacía permanezca vacía tras el formateo."""
    assert format_text("") == ""