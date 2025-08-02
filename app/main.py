from fastapi import FastAPI, HTTPException, Depends
from app.database import get_db
from app.models import Product, ProductCreate, ProductRead
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

app = FastAPI(title="Inventrack Inventory API")

@app.post("/products", response_model=ProductRead)
async def add_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    # Implement product creation logic in models.py
    new_product = await Product.create(db, product)
    if not new_product:
        raise HTTPException(status_code=400, detail="Duplicate SKU or database error.")
    return new_product

@app.get("/products", response_model=List[ProductRead])
async def get_products(db: AsyncSession = Depends(get_db)):
    # Implement product list retrieval logic in models.py
    return await Product.list_all(db)
