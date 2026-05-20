# from pydantic import BaseModel

# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = True

# product_one = Product(id=101, name='Laptop', price=999.99)    
# product_two = Product(id=102, name='mouse', price=499.99, in_stock=False)

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = None    

car_data ={
    "user_id": 123,
    "items": ["laptop", "mouse","keyboard"],
    "quantity": {"laptop": 1, "mouse": 2, "keyboard": 1}
}   

cart = Cart(**car_data)
print(cart)

