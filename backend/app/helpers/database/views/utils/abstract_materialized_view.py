# pylint: disable=unused-argument,arguments-differ
import abc
from typing import Any, Type

import psycopg2
from sqlalchemy import Table
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.ddl import DropTable
from sqlalchemy.sql.expression import ClauseElement, Executable


class AbstractMaterializedView(Table, metaclass=abc.ABCMeta):
    """
    AbstractMaterializedView is an abstract base class for materialized views. It provides methods to create, refresh, delete, and close materialized views in a PostgreSQL database.

    Attributes:
        `conn (psycopg2.connect)`: Connection to the PostgreSQL database.
        `cur (psycopg2.extensions.cursor)`: Cursor object to execute queries on the database.

    Methods:
        `create_view(view_name: str) -> bool`: Creates a new materialized view with the given name and query.
        `refresh_view(view_name: str) -> bool`: Refreshes the materialized view with the given name.
        `delete_view(view_name: str) -> bool`: Deletes the materialized view with the given name.
        `close() -> bool`: Closes the cursor and connection to the database.
    """
    is_view = True


    
    class CreateMaterializedView(Executable, ClauseElement):
        """
        DDL statement to create a materialized view.
        
        Args:
            name (str): The name of the materialized view.
            selectable (ClauseElement): The SELECT statement to create the materialized view from.
        """
        def __init__(self, name: str, selectable: ClauseElement) -> None:
            self.name = name
            self.select = selectable

    class RefreshMaterializedView(Executable, ClauseElement):
        """
        DDL statement to refresh a materialized view.
        
        Args:
            name (str): The name of the materialized view to refresh.
        """
        def __init__(self, name: str) -> None:
            self.name = name
        
        def __str__(self) -> str:
            return f"REFRESH MATERIALIZED VIEW {self.name}"
        
    class DropMaterializedView(DropTable):
        """
        DDL statement to drop a materialized view.
        
        Args:
            name (str): The name of the materialized view to drop.
        """

        drop_statements = {}

        def __init__(self, name: str) -> None:
            """
            Initialize a `DropMaterializedView` object with the name of the materialized view to drop.
            
            Args:
                name (str): The name of the materialized view to drop.
            """
            self.name = name
            super().__init__(name)

        def __call__(self, is_cascade: bool, **kw) -> str:
            """
            Generate the DDL statement to drop the materialized view.
            
            Args:
                is_cascade (bool): A flag indicating whether the statement should include a CASCADE option.
                **kw: Additional keyword arguments.
            
            Returns:
                str: The DDL statement to drop the materialized view.
            """
            if is_cascade:
                return f"DROP MATERIALIZED VIEW {self.name} CASCADE"
            return f"DROP MATERIALIZED VIEW {self.name}"

        def _compile_w_cache(self, element, **kw) -> bool:
            """
            Check if the DDL statement to drop the materialized view is already cached.
            
            Args:
                element (DropMaterializedView): The `DropMaterializedView` object.
                **kw: Additional keyword arguments.
            
            Returns:
                bool: `True` if the DDL statement is already cached, `False` otherwise.
            """
            return element.name not in self.drop_statements
        
        def compile_w_cache(self, element, **kw) -> bool:
            """
            Check if the DDL statement to drop the materialized view is already cached.
            
            Args:
                element (DropMaterializedView): The `DropMaterializedView` object.
                **kw: Additional keyword arguments.
            
            Returns:
                bool: `True` if the DDL statement is already cached, `False` otherwise.
            """
            return self._compile_w_cache(element, **kw)
        
        def cache_drop_statement(self, element) -> None:
            """
            Cache the DDL statement to drop the materialized view.
            
            Args:
                element (DropMaterializedView): The `DropMaterializedView` object.
            """
            self.drop_statements.update(element.name)

    def __init__(self, host, port, user, password, database):
        """
        Initialize a connection to the PostgreSQL database and create a cursor.
        
        Args:
            host (str): The hostname of the database.
            port (int): The port number of the database.
            user (str): The username to connect to the database.
            password (str): The password to connect to the database.
            database (str): The name of the database to connect to.
        """
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
        self.cur = self.conn.cursor()
    
    
    @abc.abstractmethod
    def create_view(self, view_name: str) -> bool:
        """
        Creates a new materialized view with the given name.

        Parameters:
        view_name (str): The name of the materialized view to create.

        Returns:
        bool: True if the materialized view was created successfully, False otherwise.

        Example implementation:
        def create_view(view_name: str) -> bool:
            connection = engine.connect()
            success = connection.execute(CreateMaterializedView(view_name))
            connection.close()
            return success
        """
    @abc.abstractmethod
    def refresh_view(self, view_name: str) -> bool:
        """
        Refreshes the materialized view with the given name.

        Parameters:
        view_name (str): The name of the materialized view to refresh.

        Returns:
        bool: True if the materialized view was refreshed successfully, False otherwise.

        Example implementation:
        def refresh_view(view_name: str) -> bool:
            connection = engine.connect()
            success = connection.execute(RefreshMaterializedView(view_name))
            connection.close()
            return success
        """
    
    @abc.abstractmethod
    def drop_view(self, view_name: str) -> bool:
        """
        Drops the materialized view with the given name.

        Parameters:
        view_name (str): The name of the materialized view to drop.

        Returns:
        bool: True if the materialized view was dropped successfully, False otherwise.

        Example implementation:
        def drop_view(view_name: str) -> bool:
            connection = engine.connect()
            success = connection.execute(DropMaterializedView(view_name))
            connection.close()
            return success
        """
        
    @abc.abstractmethod
    def close(self) -> bool:
        """
        Closes the connection to the database.

        Returns:
        bool: True if the connection was closed successfully, False otherwise.

        Example implementation:
        def close(self) -> bool:
            try:
                self.conn.close()
                return True
            except Exception:
                return False
        """
        
    @compiles(DropMaterializedView, "postgresql")
    def _drop_materialized_view(
        self,
        element: DropMaterializedView,
        compiler: Type[SQLCompiler],
        **kw: Any
    ) -> str:
        """
        Generate the DDL statement to drop the materialized view.
        
        Args:
            element (DropMaterializedView): The `DropMaterializedView` object representing the materialized view to drop.
            compiler (Type[SQLCompiler]): The compiler to use.
            **kw: Additional keyword arguments.
        
        Returns:
            str: The DDL statement to drop the materialized view.
        """
        if element.compile_w_cache(element.name):
            element.cache_drop_statement(element.name)    
        return element.__call__(False)

    @compiles(CreateMaterializedView, "postgresql")
    def _create_materialized_view(
        self,
        element: CreateMaterializedView,
        compiler: Type[SQLCompiler],
        **kw: Any
    ) -> str:
        """
        Generate the DDL statement to create the materialized view.
        
        Args:
            element (CreateMaterializedView): The `CreateMaterializedView` object representing the materialized view to create.
            compiler (Type[SQLCompiler]): The compiler to use.
            **kw: Additional keyword arguments.
        
        Returns:
            str: The DDL statement to create the materialized view.
        """
        return f"CREATE MATERIALIZED VIEW {element.name} AS {compiler.sql_compiler.process(element.selectable, literal_binds=True)}"
    
    @compiles(RefreshMaterializedView, "postgresql")
    def _compile_refresh_view(
        self,
        drop_element: DropMaterializedView,
        element: RefreshMaterializedView, 
        compiler: Type[SQLCompiler], 
        **kw: Any
    ) -> str:
        """
        Generates the DDL statement to refresh a materialized view.

        Args:
        drop_element (DropMaterializedView): The DDL statement to drop the materialized view.
        element (RefreshMaterializedView): The DDL statement to refresh the materialized view.
        compiler (Type[SQLCompiler]): The compiler used to generate the DDL statement.
        **kw: Additional keyword arguments.

        Returns:
        str: The DDL statement to refresh the materialized view.
        """
        return element.__str__(element)
