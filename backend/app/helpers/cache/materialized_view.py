import psycopg2


class MaterializedView:
    """
    MaterializedViews class provides methods to create, refresh, delete and close materialized views in a PostgreSQL database.

    Attributes:
    conn (psycopg2.connect): Connection to the PostgreSQL database.
    cur (psycopg2.extensions.cursor): Cursor object to execute queries on the database.

    Methods:
    create_view(view_name: str, query: str): Creates a new materialized view with the given name and query.
    refresh_view(view_name: str): Refreshes the materialized view with the given name.
    delete_view(view_name: str): Deletes the materialized view with the given name.
    close(): Closes the cursor and connection to the database.
    """
    def __init__(self, host, port, user, password, database):
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.conn.cursor()
    
    def create_view(self, view_name, query):
        self.cur.execute(f"CREATE MATERIALIZED VIEW {view_name} AS {query}")
        self.conn.commit()
    
    def refresh_view(self, view_name):
        self.cur.execute(f"REFRESH MATERIALIZED VIEW {view_name}")
        self.conn.commit()
    
    def delete_view(self, view_name):
        self.cur.execute(f"DROP MATERIALIZED VIEW {view_name}")
        self.conn.commit()
    
    def close(self):
        self.cur.close()
        self.conn.close()