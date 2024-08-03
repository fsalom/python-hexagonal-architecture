# Python Hexagonal Architecture

## Overview

This project implements a hexagonal architecture (Ports and Adapters) to separate business logic from external interfaces and infrastructure. The architecture ensures modularity and flexibility, allowing easy adaptation to new requirements and changes in external systems.

## Project Structure

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
## Folder Descriptions

- application/: Contains the application logic and services.
  - services/: Implements business use cases and operations. For example, user_services.py handles user-related operations.
  - ports/: Defines interfaces (ports) for driving and driven adapters.
    - driving/: Interfaces for external systems to drive the application, like user_adapter_port.py.
    - driven/: Interfaces for accessing external resources, like user_repository_port.py.
    
- domain/: Contains the core business logic and domain entities. 
  - entities/: Defines business entities, such as user.py for user-related data and behavior.
  
- driven/: Contains adapters that implement the driven ports to interact with external systems.
  - database/: Adapters for database interactions, such as database_user_repository.py for user data storage.

- driving/: Contains adapters that implement the driving ports to handle incoming requests.
  - api/: Handles HTTP requests and responses, e.g., api_user_adapter.py.
  - cli/: Handles command-line interactions, e.g., cli_adapter.py.
  
- tests/: Contains unit and integration tests organized by the components they test.
- main.py: The main entry point of the application, setting up the adapters and starting the system.
- pyproject.toml: Configuration file for Python project, specifying dependencies and project metadata.

## Contributing

Please read our CONTRIBUTING.md for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Articles

- Building Scalable and Testable Python Applications with Modular Monoliths 
  - https://tidalascent.com/?p=1

- Problems of big django project
  - https://alexgrover.me/writing/python-hexagonal-architecture
  - ORMs don’t adequately separate data and behavior. They make it too easy to access the database from anywhere in your codebase - with simple “dot” access, you can issue a complex query that slows down your whole application and you might not even realize it! All of a sudden, your view code, your model code, and even helper functions are making database calls that eventually cause a bottleneck.
  - Most frameworks don’t give you good guidance as to where the bulk of your code should actually go. Once you have a non-trivial app, your views start to get really big. There are different schools of thought on how to grow your application (see: Fat Models and Service Objects) but the Python community doesn’t seem to discuss them often, and the frameworks themselves don’t mention much about architecture at all in their documentation.
  - Some generally bad conventions. One that comes to mind is overriding ORM methods and hooks in Django. When calling save() on an object can potentially mutate it or have side effects on other models, and you can also have a post_save hook with even more behavior that no one could figure out where else to put, it’s easy to write confusing, messy code. Obviously, no one sets out to write something poorly, but when you’re working with a large team it’s easy to add a couple lines of code in a place that seems right and realize later that it’s really hard to understand.

- Comparing Hexagonal Architecture with Other Patterns
  - https://python.plainenglish.io/hexagonal-architecture-a-basic-guide-on-why-its-better-than-mvc-or-clean-architecture-7864f5f97b0a

- Flask Blog tutorial with Hexagonal Architecture(part 1-3)
  - https://blog.devgenius.io/flask-blog-tutorial-with-hexagonal-architecture-part-1-6446e7e9aaaa

- Good article with very clear domain explanation 
  - https://medium.com/@bergraan/hexagonal-architecture-catch-em-all-496cc4a88734
  - code: https://github.com/bergran/pokemon_project_example/tree/master

- Ports and adapters
  - https://hemanthhari2000.medium.com/the-ports-and-adapters-pattern-unraveling-the-mystery-2efbf678ab9b

- Visual explanation 
  - https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c

- Tiny explantion
  - https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63
  - code: https://github.com/douwevandermeij/voting-system/tree/initial/app

- Ports and adapters architecture. Python micro example
  - https://towardsdev.com/ports-and-adapters-architecture-python-micro-example-751302906684
  - code: https://github.com/jorzel/opentable

---