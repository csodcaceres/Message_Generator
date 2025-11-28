class MessageBuilder:
    """
    Clase encargada de construir mensajes personalizados.
    """

    def __init__(self, username: str):
        self.username = username

    def generate_welcome_message(self, hobby: str) -> str:
        """
        Genera el mensaje de bienvenida personalizado.
        """
        return (
            f"Hello {self.username}!\n"
            f"Welcome to the world of programming.\n"
            f"It's great to know that you enjoy {hobby}.\n"
            "Get ready to explore and create amazing things!"
        )
