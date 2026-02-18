import json
import os

class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config_file="config.json"):
        if not hasattr(self, 'config'):
            self.config_file = config_file
            self.config = self._load_config()
            print("Конфігурацію завантажено")
    
    def _load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {"app_name": "DefaultApp", "version": "1.0.0", "debug": False}
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self._save_config()
    
    def _save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

# Тестування
print("\n=== ConfigManager Singleton ===")
config1 = ConfigManager()
config2 = ConfigManager()

print(f"config1 is config2: {config1 is config2}")
print(f"App name: {config1.get('app_name')}")
config1.set("debug", True)
print(f"Debug mode: {config2.get('debug')}")