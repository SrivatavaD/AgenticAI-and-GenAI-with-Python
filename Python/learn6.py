# class chai:
#     pass

# class chaitime:
#     pass

# print(type(chai))

# ginger_tea = chai()
# print(type(ginger_tea))
# print(type(ginger_tea) is chai)
# print(type(ginger_tea) is chaitime)

# class chai:
#     origin = "India"
# print(chai.origin)    

# chai.is_hot = True
# print(chai.is_hot)

# # creating objects of chai class

# masala = chai()
# print(masala.origin)
# print(f"masala{masala.is_hot}")
# masala.is_hot = False

# print("class: ", chai.is_hot)
# print(f"masala:{masala.is_hot}")
# print(masala.flavor)

class chaicup:
    size = 150 #ml

    def describe(self):
        return f"A{self.size}ml chai cup"
    
cup = chaicup()
print(cup.describe())
print(chaicup.describe(cup))

cup_two = chaicup()
cup_two.size = 100
print(chaicup.describe(cup_two))
    