import cProfile
import pstats
import io
from original_code import slow_fibonacci, find_duplicates
from optimized_code import fast_fibonacci, find_duplicates_optimized

def profile_function(func, *args):
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args)
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(10)
    print(f"\n--- Profiling {func.__name__} ---")
    print(s.getvalue())
    return result

if __name__ == "__main__":
    print("=== SLOW FIBONACCI (n=35) ===")
    profile_function(slow_fibonacci, 35)
    
    print("\n=== FAST FIBONACCI (n=35) ===")
    profile_function(fast_fibonacci, 35)
    
    test_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 4, 9, 1, 2]
    print("\n=== FIND DUPLICATES ORIGINAL ===")
    profile_function(find_duplicates, test_list)
    
    print("\n=== FIND DUPLICATES OPTIMIZED ===")
    profile_function(find_duplicates_optimized, test_list)