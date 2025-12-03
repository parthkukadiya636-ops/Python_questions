def fib(n):
    x = 0
    y = 1
    
    if n == 0:
        return 0
    
    for i in range(1, n):
        sum_val = x + y
        x = y
        y = sum_val
    
    return y  # This holds the nth fibonacci number
