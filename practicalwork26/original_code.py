def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

def inefficient_list_operation():
    result = []
    for i in range(10000):
        result = result + [i * 2]
    return result

def unused_variable_example():
    x = 10
    y = 20
    return y

def bad_memory_usage():
    data = []
    for i in range(100000):
        data.append(i ** 2)
    return data