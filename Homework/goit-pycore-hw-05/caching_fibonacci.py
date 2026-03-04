
# caching_fibonacci returns the n-th Fibonacci number

from linecache import cache


def caching_fibonacci(n):

    cache = {}

    def fibonacci (n):
        
        if n <= 1:
            cache[n] = n
            return n
        
        if n in cache:
            return cache[n]
        
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    

    return fibonacci(n)



if __name__ == "__main__":

    print(f"Fibbonachi for 2 -> {caching_fibonacci(2)}")
    print(f"Fibbonachi for 9 ->  {caching_fibonacci(9)}")
    print(f"Fibbonachi for 50 -> {caching_fibonacci(50)}")





