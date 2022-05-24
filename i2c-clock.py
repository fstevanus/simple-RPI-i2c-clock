from rpi_lcd import LCD
from datetime import datetime
import psutil
import math

lcd = LCD(0x27, 1, 16, 2, True)

while True:
  now = datetime.now()

  second = now.second
  minute = now.minute
  hour = now.hour
  day = now.day
  month = now.month
  cpu_percentage = int(psutil.cpu_percent(None))
  memory_percentage = int(psutil.virtual_memory().percent)
  temperature_celcius = int(math.ceil(psutil.sensors_temperatures()['cpu_thermal'][0].current))

  lcd.text(f"{month}/{day} {hour}:{minute}:{second}", 1, 'center')
  lcd.text(f"C{cpu_percentage}% R{memory_percentage}% {temperature_celcius}c", 2, 'center')