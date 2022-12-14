# Models

Application for Money jar financing system.

## TOC

- [Backend](/backend/README.md)
    - [api](/backend/api/README.md)
    - [models](/backend/models/README.md)
    - [utils](/backend/utils/Readme.md) 
- [Frontend](/frontend/README.md)
    - [components](/frontend/src/components/README.md)
    - [pages](/frontend/src/pages/README.md)
    - [services](/frontend/src/services/README.md)


This is what a general implementation in `models` looks like:

```python
from app import db
from flask_bcrypt import generate_password_hash
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserObjectType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (ObjectType,)

```

In general, this code defines a GraphQL object type that is mapped to a SQLAlchemy model, and it specifies that the object type should implement a set of common fields and arguments defined in the ObjectType interface. This can be helpful for ensuring that the object type works properly with other parts of the GraphQL schema.

The code defines a GraphQL object type named UserObjectType that is mapped to a SQLAlchemy model named User. The object type is defined as a subclass of SQLAlchemyObjectType and it has a Meta subclass that specifies that the object type should implement the ObjectType interface.

## Interfaces

### ObjectType

The ObjectType interface is a built-in interface in the Graphene library that defines a set of common fields that are available on all object types, such as the id field and the __typename field. By implementing the ObjectType interface, the UserObjectType class ensures that it includes all of these common fields.

### Connections

```python

class UserObjectType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (ObjectType,)

```

When defining relationships between entities in our GraphQL schema, we use the Connection interface from the Graphene library. The Connection interface provides a set of common fields and arguments that are often used when working with connections in GraphQL, and it makes it easy to include these fields and arguments in our connections without having to define them ourselves.

For example, the Connection interface defines a pageInfo field that provides information about the current page of results in the connection, such as the total number of pages and the current cursor position. It also defines an edges argument that can be used to paginate the results of the connection, by providing a limit and an offset for the results.

By using the Connection interface, we can easily include these common fields and arguments in our connections, which makes our schema more concise and easier to work with. This helps us to define and work with connections between our entities in a consistent and efficient way.

#### Relationships

The Connection interface from the Graphene library can be used to represent different kinds of relationships between entities in a GraphQL schema. Here are some examples of how you might use the Connection interface to represent different relationships:

- **One-to-many relationship:** To represent a one-to-many relationship between two entities, you can define a connection field on the entity that has the many side of the relationship. For example, if you have a User entity and a Post entity, where each user can have multiple posts, you might define the relationship like this:


```python
from graphene import Connection, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserObjectType(SQLAlchemyObjectType):
    posts = Connection(lambda: PostObjectType)

    class Meta:
        model = User
        interfaces = (ObjectType,)

class PostObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (ObjectType,)
```

In this example, the UserObjectType class is defined with a posts field that is a connection to the PostObjectType class. This defines a one-to-many relationship between User and Post, where each User can have multiple Post objects associated with it.

- **Many-to-one relationship:** To represent a many-to-one relationship between two entities, you can define a non-connection field on the entity that has the many side of the relationship. For example, if you have a User entity and a Post entity, where each post is written by a single user, you might define the relationship like this:

```python

from graphene import Field, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserObjectType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (ObjectType,)

class PostObjectType(SQLAlchemyObjectType):
    user = Field(UserObjectType)

    class Meta:
        model = Post
        interfaces = (ObjectType,)
```

- **One-to-one relationship:** To represent a one-to-one relationship between to entities, you can define a connection field on both sides of the relationship by using the opposite's side ObjectType.


```python
from graphene import Connection, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

class UserObjectType(SQLAlchemyObjectType):
    # One-to-one relationship: each user has one profile
    profile = Connection(lambda: ProfileObjectType)

    # Many-to-many relationship: each user can have multiple posts
    posts = Connection(lambda: PostObjectType)

    class Meta:
        model = User
        interfaces = (ObjectType,)

class ProfileObjectType(SQLAlchemyObjectType):
    # One-to-one relationship: each profile belongs to one user
    user = Connection(lambda: UserObjectType)

    class Meta:
        model = Profile
        interfaces = (ObjectType,)

```

- **Many-to-many relationship:** To represent a Many-to-many relationship between to entities, you can define a connection field on both sides of the relationship by using the opposite's side ObjectType.

```python

class PostObjectType(SQLAlchemyObjectType):
    # Many-to-many relationship: each post can have multiple tags
    tags = Connection(lambda: TagObjectType)

    class Meta:
        model = Post
        interfaces = (ObjectType,)

class TagObjectType(SQLAlchemyObjectType):
    # Many-to-many relationship: each tag can be applied to multiple posts
    posts = Connection(lambda: PostObjectType)

    class Meta:
        model = Tag
        interfaces = (ObjectType,)
```