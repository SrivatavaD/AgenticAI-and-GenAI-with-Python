# def get_input():
#     print("getting input")

# def validate_to_db():
#     print("saving to db")

# def register_user():
#     get_input()
#     validate_to_db()
  
#     print("user registered successfully")
# register_user()    

# def calculate_bill(cups, price_per_cup):
#     total = cups * price_per_cup
#     return total

# a=int(input("Enter number of cups: "))
# b=int(input("Enter price per cup: "))
# bill_amount = calculate_bill(a, b)

# print("The total bill amount is:", bill_amount)

# def add_vat(price,vat_rate):
#     return price *(100 + vat_rate)/100

# orders = [100,150,200]
# for price in orders:
#     final_amount = add_vat(price, 10)
#     print(f"original: {price} , final with vat: {final_amount}")

# def serve_chao():
#     chai_type = "masala"   #local scope
#     print(f"inside function{chai_type}")

# chai_type = "green"
# serve_chai()
# print(f"outside function: {chai_type}")    