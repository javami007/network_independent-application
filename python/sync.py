import sqlite3

# Database for storing unsent messages
db = sqlite3.connect('messages.db')

def setup_db():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

# Function to store unsent messages
def store_message(content):
    cursor = db.cursor()
    cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
    db.commit()

# Function to retrieve unsent messages
def get_unsent_messages():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM messages')
    return cursor.fetchall()

if __name__ == "__main__":
    setup_db()
    store_message("Test Message")
    print(get_unsent_messages())

