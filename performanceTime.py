from time import perf_counter
from functools import wraps

def performance_time(func):
    @wraps(func)
    
    def wrapper_decorator(*args, **kwargs):
        
        start_time = perf_counter()
        
        value= func(*args, **kwargs)
    
        end_time = perf_counter()
        
        run_time= end_time - start_time
        
        print(f"{func.__name__} run time is: {run_time}")
        
        return value
    return wrapper_decorator


# sample functions for test

@performance_time
def A(y):
    s = 0
    for i in range(y):
        s += i**2
        

@performance_time
def B(x):
    fact=1
    for i in range(1, x+1):
        fact *= i
        
        

A(2000)

B(2000)        
        
        
            
    



