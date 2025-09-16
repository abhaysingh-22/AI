from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
    
product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)
print(product_one)

product_two = Product(id=2, name="Smartphone", price=499.49, in_stock=False)
print(product_two)