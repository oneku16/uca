import sqlite3


def query_database(db_file, query):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_database():

    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect('my_data_base.db')

    # Create a cursor object
    cursor = conn.cursor()
    '''
    asd
    'asd'
    asd
    '''
    # Execute a query to create a new table
    cursor.execute("""CREATE TABLE STUDENT (
  id INT PRIMARY KEY,
  first_name VARCHAR(16) NOT NULL,
  last_name VARCHAR(16) NOT NULL,
  email VARCHAR(32) NOT NULL,
  major ENUM("CS", "CM", "EES", "GE", "ES", "BM") NOT NULL,
  cohort INT
);""")

    # Commit changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

create_database()