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
def serve_chai():
    yield "cup1: masala chai"
    yield "cup2:ginger chao"
    yield "cup3: elachi chai"

    stall = serve_chai()

    for cup in stall:
        print(cup)