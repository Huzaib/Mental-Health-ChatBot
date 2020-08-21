import sqlite3

def insert_data(name, age, history, feeling, addiction, knowledge, Stars, sharing):
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql='''CREATE TABLE table(
    name VARCHAR,
    age VARCHAR,
    history VARCHAR,
    feeling VARCHAR,
    addiction VARCHAR,
    knowledge VARCHAR,
    Stars VARCHAR,
    sharing VARCHAR
    )'''
    cursor.execute(
        '''INSERT INTO table(name, age, history, feeling, addiction, knowledge, Stars, sharing)) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (name, age, history, feeling, addiction, knowledge, Stars, sharing))

    print("Table created successfully........");

    # Commit your changes in the database
    conn.commit();

    # Closing the connection
    conn.close();

# if __name__ == "__main__":
# insert_data('12-10-2017',3, 'adventure', 2, 1, 6000, 'qwerty@gmail.com', 987654321)