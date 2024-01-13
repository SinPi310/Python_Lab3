from functools import lru_cache
import timeit

class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step >= self.steps:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_step += 1
            return result

    #rekurencyjna
    def fibonacci_recursive(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    #dekorator
    @lru_cache(maxsize=None)
    def fibonacci_cached(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci_cached(n - 1) + self.fibonacci_cached(n - 2)

#Czas rekurencyjnej
fibonacci_instance = Fibonacci(steps=100)
time_recursive = timeit.timeit(lambda: fibonacci_instance.fibonacci_recursive(10), number=1000)
print(f"Czas rekurencyjnej: {time_recursive:.6f}s")

#Czas dekorator
time_lru_cache = timeit.timeit(lambda: fibonacci_instance.fibonacci_cached(10), number=1000)
print(f"Czas po @lru_cache: {time_lru_cache:.6f}s")

#Główna funkcja
#for num in fibonacci_instance:
#    print(num)
