def find_duplicates_optimized(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

def fast_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fast_fibonacci(n - 1, memo) + fast_fibonacci(n - 2)
    return memo[n]

def efficient_list_operation():
    return [i * 2 for i in range(10000)]

def fixed_unused_variable():
    y = 20
    return y

def efficient_memory_usage():
    return [i ** 2 for i in range(100000)]