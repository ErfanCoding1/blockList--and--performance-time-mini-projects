from functools import wraps

    
passwords = {'jack':'12248','john':'95624','sara':'52874','chris':'32025'}
    
blocklist_ = {'jack','chris'}
    
    
    
def blocklist(func):
    @wraps(func)
        
    def wrapper_decorator(*args,**kwargs):
        if args[0] in blocklist_:
            print("this user is blocked!!")
        else:        
            func(*args,**kwargs)
    return wrapper_decorator
    
    
    
@blocklist
def print_password(name):
    print(f"{name} : {passwords[name]}")
    
    
@blocklist    
def change_password(name, password):
        
    passwords[name]= password
    print(f"{name} : {passwords[name]}")
        
        

print_password('sara')    

change_password('chris','45692')    


           
        
        
    