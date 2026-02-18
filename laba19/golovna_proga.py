def main():
    print("=" * 50)
    print("ДЕМОНСТРАЦІЯ ВСІХ ВИДІВ SINGLETON")
    print("=" * 50)
    
    # Простий Singleton
    s1 = SimpleSingleton()
    s2 = SimpleSingleton()
    print(f"\nПростий: {s1.increment()}, {s2.increment()}")
    
    # Лінива ініціалізація
    lazy = LazySingleton()
    lazy.add_data("test")
    
    # Потокобезпечний
    safe = ThreadSafeSingleton()
    safe.safe_increment("main")
    
    # ConfigManager
    config = ConfigManager()
    print(f"Config app: {config.get('app_name')}")
    
    # Logger
    log = Logger()
    log.info("Демонстрація завершена")
    
    print("\n" + "=" * 50)
    print("Всі Singleton працюють коректно!")
    print("=" * 50)

if __name__ == "__main__":
    main()