# Модуль для роботи з датчиком температури/вологості
from machine import Pin
import dht
import time

class DHTSensor:
    def __init__(self, pin_num):
        self.sensor = dht.DHT11(Pin(pin_num))
        
    def read(self):
        """Зчитує дані з сенсора і повертає температуру та вологість"""
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()
            hum = self.sensor.humidity()
            return temp, hum
        except Exception as e:
            print("Помилка читання DHT:", e)
            return None, None
            
    def read_with_retry(self, retries=3):
        """Спроба зчитати дані кілька разів у разі помилки"""
        for i in range(retries):
            temp, hum = self.read()
            if temp is not None:
                return temp, hum
            time.sleep(1)
        return None, None