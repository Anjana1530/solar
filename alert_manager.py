
import pandas as pd

df = pd.read_csv('data/mock_readings.csv')
avg = df['solar_kwh'].mean()
today_gen = df.iloc[-1]['solar_kwh']
if today_gen < 0.7 * avg:
    print("⚠️ Alert: Today's solar generation is below average!")
