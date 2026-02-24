# Модуль для роботи з LCD 1602 I2C
from machine import Pin, I2C
from time import sleep
import lcd_api
from i2c_lcd import I2cLcd  # Потрібно завантажити бібліотеку на плату

class LCDDisplay:
    def __init__(self, i2c_addr, sda_pin, scl_pin):
        self.i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.lcd = I2cLcd(self.i2c, i2c_addr, 2, 16)  # 2 рядки, 16 символів
        
    def show_message(self, temp, hum):
        """Виводить температуру та вологість на екран"""
        self.lcd.clear()
        self.lcd.move_to(0, 0)
        self.lcd.putstr(f"Temp: {temp}C")
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f"Hum: {hum}%")
        
    def show_startup(self):
        """Показує стартове повідомлення"""
        self.lcd.clear()
        self.lcd.move_to(0, 0)
        self.lcd.putstr("Monitoring...")
        self.lcd.move_to(0, 1)
        self.lcd.putstr("System Ready")
        sleep(2)