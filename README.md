# 🧱 Ejemplo de Proyecto con Arquitectura Hexagonal

## 📖 Resumen General

Este proyecto implementa una arquitectura hexagonal (Ports and Adapters) para separar la lógica de negocio de las interfaces externas y la infraestructura. Esta arquitectura garantiza modularidad y flexibilidad, permitiendo una fácil adaptación a nuevos requisitos o cambios en sistemas externos.

👉 [Como instalar pyenv](./README_INSTALL_PYTHON.md)

## 🗂️ Estructura del Proyecto

```
project/
├── application/
│   ├── services/
│   │   ├── user_services.py
│   └── ports/
│       ├── driving
│       │    └── user_adapter_port.py
│       └── driven
│            └── user_repository_port.py
├── domain/
│   ├── __init__.py
│   └── entities/
│       └── user.py
├── driven/
│   └── database/
│       ├── dbo.py
│       ├── database_user_mapper.py
│       └── database_user_repository.py
├── driving/
│   ├── api/
│   │   ├── dto.py
│   │   ├── database_user_mapper.py
│   │   └── api_user_adapter.py
│   └── cli/
│       └── cli_adapter.py
├── tests/
│   ├── __init__.py
│   ├── application/
│   ├── domain/
│   ├── driven/
│   └── driving/
├── main.py
├── README.md
└── pyproject.toml
```

## 📁 Descripción de Carpetas

- `application/`: Contiene la lógica de aplicación y los casos de uso.
  - `services/`: Implementa los casos de uso del negocio. Por ejemplo, `user_services.py` gestiona operaciones relacionadas con usuarios.
  - `ports/`: Define las interfaces (puertos) para los adaptadores driving y driven.
    - `driving/`: Interfaces para sistemas externos que impulsan la aplicación, como `user_adapter_port.py`.
    - `driven/`: Interfaces para acceder a recursos externos, como `user_repository_port.py`.

- `domain/`: Contiene la lógica principal del negocio y las entidades del dominio.
  - `entities/`: Define las entidades de negocio, como `user.py`.

- `driven/`: Contiene los adaptadores que implementan los puertos driven para interactuar con sistemas externos.
  - `database/`: Adaptadores para interacción con bases de datos, como `database_user_repository.py`.

- `driving/`: Contiene los adaptadores que implementan los puertos driving para manejar solicitudes entrantes.
  - `api/`: Maneja peticiones/respuestas HTTP, por ejemplo `api_user_adapter.py`.
  - `cli/`: Maneja interacciones por línea de comandos, por ejemplo `cli_adapter.py`.

- `tests/`: Contiene pruebas unitarias e integración organizadas por componente.

- `main.py`: Punto de entrada principal de la aplicación. Configura adaptadores e inicia el sistema.

- `pyproject.toml`: Archivo de configuración del proyecto Python (dependencias, metadatos, etc).

## 🤝 Cómo Contribuir

Por favor, consulta el archivo `CONTRIBUTING.md` para conocer las directrices de contribución al proyecto.

## 🪪 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📚 Artículos de Interés

- Building Scalable and Testable Python Applications with Modular Monoliths  
  🔗 https://tidalascent.com/?p=1

- Problems of big Django project  
  🔗 https://alexgrover.me/writing/python-hexagonal-architecture  
  🔸 ORMs no separan adecuadamente los datos y el comportamiento.  
  🔸 Muchos frameworks no guían bien dónde poner el grueso del código.  
  🔸 Sobrescribir métodos del ORM puede derivar en código confuso.

- Comparing Hexagonal Architecture with Other Patterns  
  🔗 https://python.plainenglish.io/hexagonal-architecture-a-basic-guide-on-why-its-better-than-mvc-or-clean-architecture-7864f5f97b0a

- Flask Blog tutorial with Hexagonal Architecture (part 1-3)  
  🔗 https://blog.devgenius.io/flask-blog-tutorial-with-hexagonal-architecture-part-1-6446e7e9aaaa

- Buen artículo con explicación clara del dominio  
  🔗 https://medium.com/@bergraan/hexagonal-architecture-catch-em-all-496cc4a88734  
  🧑‍💻 Código: https://github.com/bergran/pokemon_project_example/tree/master

- Ports and Adapters  
  🔗 https://hemanthhari2000.medium.com/the-ports-and-adapters-pattern-unraveling-the-mystery-2efbf678ab9b

- Explicación visual  
  🔗 https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c

- Mini explicación  
  🔗 https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63  
  🧑‍💻 Código: https://github.com/douwevandermeij/voting-system/tree/initial/app

- Ejemplo micro en Python  
  🔗 https://towardsdev.com/ports-and-adapters-architecture-python-micro-example-751302906684  
  🧑‍💻 Código: https://github.com/jorzel/opentable