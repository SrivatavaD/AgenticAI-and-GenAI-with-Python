# menu =[
#     "masala chai",
#     "green tea",
#     "lemon tea",
#     "iced peach tea",
#     "ginger tea"
# ]

# iced_tea = [tea for tea in menu if "iced" in tea]

# print(iced_tea)

# favourite_chai = [
#     "masala chai","green tea", "masala chai",
#     "lemon tea", "masla chai", "elaichi chai"
# ]

# unique_chai = {chai for chai in favourite_chai}
# print(unique_chai)

# recipes = {
#     "masala chai" : ["ginger","cardamon","clove"],
#     "green tea" : ["cardamon","clove"],
#     "lemon tea" : ["lemon", "ginger"],
#     "spicy chao" : ["ginger","black pepper","clove"],
#     "elaichi chai" : ["cardamom","milk"]
# }

# unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

# print(unique_spices)

# generators in python
# def serve_chai():
#     yield "cup1: masala chai"
#     yield "cup2:ginger chao"
#     yield "cup3: elachi chai"

#     stall = serve_chai()

#     for cup in stall:
#         print(cup)

# def infinite_chai():
#     count = 1
#     while True:
#         yield f"refil #{count}"
#         count += 1
# refill = infinite_chai()
# for _ in range(3):
#     print(next(refill))        

# # decorators in python
# def my_decorator(func):
#     def wrapper():
#         print("before function runs")
#         func()
#         print("after function runs")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello from decorated function!")   

# greet()     

from functools import wraps
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling:{func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"brewing {type} chai")

brew_chai("masala")    