# Конфігурація пінів та параметрів
DHT_PIN = 4  # Пін для датчика DHT11

# Для LCD I2C (зазвичай адреса 0x27 або 0x3F)
LCD_I2C_ADDR = 0x27
LCD_I2C_SDA_PIN = 21  # Для ESP32
LCD_I2C_SCL_PIN = 22  # Для ESP32

# Для Raspberry Pi Pico (розкоментуйте якщо треба)
# LCD_I2C_SDA_PIN = 0
# LCD_I2C_SCL_PIN = 1

UPDATE_INTERVAL_MS = 5000  # Оновлювати дані кожні 5 секунд