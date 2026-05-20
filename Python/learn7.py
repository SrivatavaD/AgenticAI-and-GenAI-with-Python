# try and except block
# chai_menu = {"masala": 30, "ginger": 40}

# try:
#     chai_menu("elaichi")
# except KeyError:
#     print("the key that you are trying to access does not exists")

# print("Hello chai code")        


def serve_chai(flavor):
    try:
        print(f"preparing{flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We dont know that flavor")
    except ValueError as e:
        print("Error:",e)
    finally:
     print("Thank you for ordering chai!")