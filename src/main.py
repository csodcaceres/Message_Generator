from generator import MessageBuilder, format_text, validate_input

def main():
    print("=== Message Generator ===")

    # Inputs del usuario
    name = input("Enter your name: ")
    hobby = input("Enter your favorite hobby: ")

    # Validación de inputs
    if not validate_input(name):
        print("Invalid name. Exiting program.")
        return

    if not validate_input(hobby):
        print("Invalid hobby. Exiting program.")
        return

    # Crear el generador de mensajes
    builder = MessageBuilder(name)

    # Procesamiento
    formatted_hobby = format_text(hobby)
    message = builder.generate_welcome_message(formatted_hobby)

    print("\n---- Welcome Message -----")
    print(message)


if __name__ == "__main__":
    main()

