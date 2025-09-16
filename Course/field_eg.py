from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantity: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    
cart_data = {
    "user_id": 123,
    "items": ["apple", "banana", "orange"],
    "quantity": {"apple": 2, "banana": 3, "orange": 1}
}

cart = Cart(**cart_data)
print(cart)