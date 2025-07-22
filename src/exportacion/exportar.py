import pandas as pd
import sqlite3

def exportar_a_excel():
    conn = sqlite3.connect('db/residuos.db')
    df = pd.read_sql_query("SELECT * FROM detections", conn)
    df.to_excel('residuos_detectados.xlsx', index=False)
    conn.close()
