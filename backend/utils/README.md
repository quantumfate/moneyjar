# Utils
Application for Money jar financing system.

## TOC

- [Backend](backend/README.md)
    - [api](backend/api/README.md)
    - [models](backend/models/README.md)
    - [utils](backend/utils/Readme.md) 
- [Frontend](frontend/README.md)
    - [components](frontend/src/components/README.md)
    - [pages](frontend/src/pages/README.md)
    - [services](frontend/src/services/README.md)

## DB

The db directory contains the files that define the data models and establish the connections to the database for the app. The db directory is organized into subdirectories, one for each entity (`users`, `saving strategy`, `money jar`, etc.).

Each entity subdirectory contains a `*_connection.py` file that defines the data model and connection for the entity, and a `*_utils.py` file that defines utility functions for interacting with the data for the entity. For example, the users subdirectory contains the `user_connection.py` and `user_utils.py` files, which define the User class and utility functions for working with user data, respectively.

The db directory also contains an `__init__.py` file, which is used to define the package's API and make the classes and functions defined in the db directory available to other parts of the app.

Overall, the db directory is an important part of the app, as it provides the foundation for storing and managing the data that your app uses. By organizing the db directory into subdirectories for each entity, it will be easier to maintain and extend your app as it grows and becomes more complex.

## Logging

In this section, the logger variable is defined using the logging module and is configured to log messages at the INFO level. The logger is also configured to write log messages to a file called app.log using a FileHandler.

The log_info, log_warning, and log_error functions are defined as convenience functions that can be used to log messages at the INFO, WARNING, and ERROR levels, respectively. These functions simply call the corresponding methods on the logger object (e.g., logger.info(), logger.warning(), etc.).

This logger.py file could be used in a Python app to provide a simple logging mechanism for logging messages at different levels. Users of the logger can import the logger module and use the log_info, log_warning, and log_error functions to log messages in their code.