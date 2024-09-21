import sqlite3
from lora_driver import LoRaDriver  # Assuming you have a LoRaDriver class

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

# Function to send messages via LoRa
def send_message_via_lora(lora, message):
    try:
        lora.send(message)
        print(f"Message sent via LoRa: {message}")
    except Exception as e:
        print(f"Failed to send message via LoRa: {e}")
        store_message(message)

# Function to attempt to resend unsent messages
def resend_unsent_messages(lora):
    unsent_messages = get_unsent_messages()
    for message in unsent_messages:
        send_message_via_lora(lora, message[1])  # Send the content of each message

if __name__ == "__main__":
    setup_db()
    test_message = "Test message to send via LoRa"

    # Initialize LoRa
    lora = LoRaDriver()
    lora.connect()

    # Send a message and handle failures
    send_message_via_lora(lora, test_message)

    # Attempt to resend unsent messages
    resend_unsent_messages(lora)
