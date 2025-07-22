import sqlite3
from datetime import datetime

def guardar_deteccion(tipo_residuo):
    conn = sqlite3.connect('db/residuos.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_residuo TEXT,
            fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        INSERT INTO detections (tipo_residuo, fecha_hora)
        VALUES (?, ?)
    ''', (tipo_residuo, datetime.now()))
    conn.commit()
    conn.close()
