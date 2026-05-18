essential_spices = {"cinnamon", "cardamom", "clove"}
optional_spice = {"clove", "black pepper"}

all_spices = essential_spices.union(optional_spice)
print(f"All spices: {all_spices}")
common_spices = essential_spices.intersection(optional_spice)
# other way to write the intersection is:
#  common_spices = essential_spices & optional_spice
print(f"Common spices: {common_spices}")

# Dictionary operations in Python.
# Dictionaries are key-value pairs.
chai_order = dict(type = "masala chai", size = "large", sugar_level = 3)
print(f"chai_oder:{chai_order}")

chai_recipe = {}
chai_recipe["base"] = "water"
chai_recipe["liquid"] = "milk"
print(f"recipe base: {chai_recipe['base']}")
print(f"recipe liquid: {chai_recipe['liquid']}")
del chai_recipe["base"]
print(f"chai_recipe: {chai_recipe}")

# advanced datatypes in python are 
#  datetime , time, calender , time delta

