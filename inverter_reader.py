
import time
from random import uniform
import sqlite3

def poll_inverter():
    timestamp = int(time.time())
    power_ac = round(uniform(500, 1500), 2)
    energy_total = round(uniform(10, 50), 2)
    return timestamp, power_ac, energy_total

def log_to_db(db='solar.db'):
    conn = sqlite3.connect(db)
    conn.execute('''CREATE TABLE IF NOT EXISTS inverter
                    (ts INTEGER, power_ac REAL, energy_total REAL)''')
    while True:
        ts, power, energy = poll_inverter()
        conn.execute('INSERT INTO inverter VALUES (?, ?, ?)', (ts, power, energy))
        conn.commit()
        time.sleep(10)

if __name__ == "__main__":
    log_to_db()
