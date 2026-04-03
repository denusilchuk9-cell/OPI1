import tracemalloc
import time
import psutil
import os
from original_code import bad_memory_usage, inefficient_list_operation
from optimized_code import efficient_memory_usage, efficient_list_operation

def check_memory_usage(func, *args):
    tracemalloc.start()
    start_mem = tracemalloc.get_traced_memory()[0]
    
    result = func(*args)
    
    current_mem = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    
    memory_used = current_mem - start_mem
    print(f"{func.__name__}: {memory_used / 1024:.2f} KB used")
    return result

def check_cpu_time(func, *args):
    start_time = time.process_time()
    result = func(*args)
    end_time = time.process_time()
    print(f"{func.__name__}: CPU time = {end_time - start_time:.5f} sec")
    return result

def system_resource_usage():
    process = psutil.Process(os.getpid())
    print(f"CPU percent: {process.cpu_percent(interval=0.1)}%")
    print(f"Memory RSS: {process.memory_info().rss / 1024 ** 2:.2f} MB")
    print(f"Memory VMS: {process.memory_info().vms / 1024 ** 2:.2f} MB")

if __name__ == "__main__":
    print("=== MEMORY USAGE ===")
    check_memory_usage(bad_memory_usage)
    check_memory_usage(efficient_memory_usage)
    
    print("\n=== CPU TIME ===")
    check_cpu_time(inefficient_list_operation)
    check_cpu_time(efficient_list_operation)
    
    print("\n=== SYSTEM RESOURCES ===")
    system_resource_usage()