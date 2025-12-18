# 📨 Message Generator

Generador de mensajes en Python con arquitectura modular y enfoque en buenas prácticas de desarrollo.

Este proyecto está pensado como parte de un **portfolio profesional**, demostrando uso de **POO**, separación de responsabilidades, tests automatizados y estructura escalable.

---

## 📌 Características

* Arquitectura modular
* Programación Orientada a Objetos (OOP)
* Código limpio y legible
* Tests automatizados con `pytest`
* Preparado para crecer (extensible)

---

## 🗂️ Estructura del proyecto

```text
Message_Generator/  
├── src/
│   ├── main.py  
│   └── message_generator/  
│       ├── __init__.py  
│       ├── builder.py  
│       ├── message.py  
│       
├── tests/  
│   ├── test_builder.py  
│   └── test_message.py  
├── requirements.txt  
├── pyproject.toml  
└── README.md  
```

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/csodcaceres/Message_Generator.git
cd Message_Generator
```

Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\\Scripts\\activate     # Windows
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

Ejecutar el generador de mensajes:

```bash
python src/message_generator/main.py
```

Ejemplo de salida:

```text
Hola Oscar, ¡bienvenido al sistema!
```

---

## 🧪 Tests

Para ejecutar los tests automatizados:

```bash
pytest -v
```

Los tests validan el comportamiento del generador y aseguran que los mensajes se construyan correctamente.

---

## 🧠 Conceptos aplicados

* Programación Orientada a Objetos
* Separación de responsabilidades
* Testing unitario
* Buenas prácticas de estructura de proyectos en Python

---

## 🚀 Posibles mejoras futuras

* Agregar CLI con `argparse`
* Internacionalización (i18n)
* Configuración por archivo `.json` o `.yaml`
* Publicación como paquete instalable

---

## 📄 Licencia

Este proyecto se publica con fines educativos y de demostración.

---

## 📎 Autor

👤 **Oscar Cáceres**  
🐙 GitHub: [https://github.com/csodcaceres](https://github.com/csodcaceres)  
💼 LinkedIn: [https://www.linkedin.com/in/oscardanielcaceres95b95771/](https://www.linkedin.com/in/oscardanielcaceres95b95771/)

---

⭐ *Proyecto desarrollado con fines educativos y demostrativos como parte de mi portfolio profesional.*
