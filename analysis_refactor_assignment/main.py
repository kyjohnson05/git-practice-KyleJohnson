from line_profiler import profile

@profile
def expensive_op(n):
    return (999 * 1000 // 2) * n

@profile
def slow_func(lst):
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result
 
def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")

import line_profiler

def run_profile():
    profiler = line_profiler.LineProfiler()
    profiler.add_function(expensive_op)
    profiler.add_function(slow_func)
    profiler_wrapper = profiler(main)
    profiler_wrapper()
    profiler.print_stats()

if __name__ == "__main__":
    run_profile()
