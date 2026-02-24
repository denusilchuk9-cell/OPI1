# Головний файл програми
from machine import Pin, I2C
import time
from config import *
from dht_sensor import DHTSensor
from lcd_display import LCDDisplay

# Ініціалізація компонентів
print("Ініціалізація системи...")
sensor = DHTSensor(DHT_PIN)
display = LCDDisplay(LCD_I2C_ADDR, LCD_I2C_SDA_PIN, LCD_I2C_SCL_PIN)

# Стартове повідомлення
display.show_startup()

# Головний цикл
print("Система запущена. Оновлення кожні", UPDATE_INTERVAL_MS/1000, "секунд")

while True:
    try:
        # Отримуємо дані з датчика
        temperature, humidity = sensor.read_with_retry()
        
        if temperature is not None:
            print(f"Температура: {temperature}C, Вологість: {humidity}%")
            display.show_message(temperature, humidity)
        else:
            print("Не вдалося отримати дані з сенсора")
            display.lcd.clear()
            display.lcd.move_to(0, 0)
            display.lcd.putstr("Sensor Error!")
            
        # Чекаємо перед наступним зчитуванням
        time.sleep_ms(UPDATE_INTERVAL_MS)
        
    except KeyboardInterrupt:
        print("Програму зупинено")
        display.lcd.clear()
        break
    except Exception as e:
        print("Помилка:", e)
        time.sleep(2)