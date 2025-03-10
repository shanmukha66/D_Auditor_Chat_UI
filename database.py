import sqlite3
import os
from datetime import datetime

# Create database directory if it doesn't exist
os.makedirs('data', exist_ok=True)

def init_db():
    conn = sqlite3.connect('data/chat_history.db')
    cursor = conn.cursor()
    
    # Create table for chat history
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        prompt TEXT,
        response TEXT,
        timestamp DATETIME
    )
    ''')
    
    conn.commit()
    conn.close()

def save_conversation(user_id, prompt, response):
    conn = sqlite3.connect('data/chat_history.db')
    cursor = conn.cursor()
    
    timestamp = datetime.now().isoformat()
    
    cursor.execute(
        'INSERT INTO chat_history (user_id, prompt, response, timestamp) VALUES (?, ?, ?, ?)',
        (user_id, prompt, response, timestamp)
    )
    
    conn.commit()
    conn.close()

def get_user_history(user_id, limit=10):
    conn = sqlite3.connect('data/chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT prompt, response, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?',
        (user_id, limit)
    )
    
    history = cursor.fetchall()
    conn.close()
    
    return [{'prompt': row[0], 'response': row[1], 'timestamp': row[2]} for row in history] 
    