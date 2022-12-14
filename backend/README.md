# Project Name

Instructions for setting up a virtual environment and installing dependencies with pip.

## TOC

- [Backend](/backend/README.md)
    - [api](/backend/api/README.md)
    - [models](/backend/models/README.md)
    - [utils](/backend/utils/README.md) 
- [Frontend](/frontend/README.md)
    - [components](/frontend/src/components/README.md)
    - [pages](/frontend/src/pages/README.md)
    - [services](/frontend/src/services/README.md)



## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/)

## Installation

1. Clone or download this repository.
2. Open a terminal and navigate to the root directory of the project.
3. Run the following command to create a new virtual environment:

`python -m venv venv`


4. Activate your virtual environment by running the following command:

`source venv/bin/activate`

5. Install the necessary dependencies for your project by running the following command:

`pip install -r requirements.txt`

## Usage

Once the dependencies are installed, you can run your project by using the scripts defined in the `package.json` file. For example:

`python app.py`


This will start the development server and allow you to access your backend API.

For more information on the available scripts and their usage, see the `package.json` file.

## Structure

### API 

The api directory contains the files that define the GraphQL schema and resolvers for the app. The schema.py file defines the GraphQL types and queries that can be used to access your app's data, and the resolvers.py file defines the functions that are responsible for actually fetching the data when a query is made.

### Utils

The utils directory contains utility files that provide helper functions for various aspects of the app. For example, the db.py file in this directory contains functions for interacting with the app's database, such as functions for querying and mutating data.

### Models

The models directory contains the files that define the app's data models. These files typically use a language like UML to describe the structure of your app's data, including the relationships between different types of data. The data models defined in this directory can be used by your app to ensure that data is stored and accessed consistently.