from fastapi import FastAPI
from models import Product

app = FastAPI()


# Product Objects
p1 = Product(
    id=1,
    name="Laptop",
    description="Gaming laptop 16GB RAM",
    price=75000.50,
    quantity=5
)

p2 = Product(
    id=2,
    name="Mobile",
    description="Android smartphone 128GB",
    price=18000.00,
    quantity=20
)

p3 = Product(
    id=3,
    name="Headphones",
    description="Noise cancelling headphones",
    price=2999.99,
    quantity=15
)

p4 = Product(
    id=4,
    name="Keyboard",
    description="Mechanical RGB keyboard",
    price=2499.50,
    quantity=10
)

p5 = Product(
    id=5,
    name="Mouse",
    description="Wireless optical mouse",
    price=799.00,
    quantity=25
)

p6 = Product(
    id=6,
    name="Monitor",
    description="24 inch Full HD LED monitor",
    price=12999.99,
    quantity=8
)

p7 = Product(
    id=7,
    name="Tablet",
    description="10 inch Android tablet 64GB",
    price=15500.00,
    quantity=12
)


# List of products (acts like database)
products = [p1, p2, p3, p4, p5, p6, p7]


@app.get("/")
def greet_user():
    return {"Hello": "World"}
@app.get("/products")

def get_all_products():
    return products

@app.get("/get_product/{id}")
def get_product(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Not Found"

@app.post("/add_product")
def add_product(product:Product):
    products.append(product)
    return product

@app.put("/update_product")
def update_product(id:int, product:Product):
    print("helllo")
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
    
    return "Product Updated succeesfully"
@app.delete("/delete_product/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"