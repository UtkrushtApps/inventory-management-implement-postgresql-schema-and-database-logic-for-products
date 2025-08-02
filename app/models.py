from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional, List

Base = declarative_base()

# SQLAlchemy Model
class ProductDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    sku = Column(String(50), nullable=False, unique=True, index=True)
    quantity = Column(Integer, nullable=False, default=0)
    last_updated = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

# Pydantic Schemas
class ProductCreate(BaseModel):
    name: str
    sku: str
    quantity: int

class ProductRead(BaseModel):
    id: int
    name: str
    sku: str
    quantity: int
    last_updated: Optional[str]

    class Config:
        orm_mode = True

class Product:
    @staticmethod
    async def create(db, product_in: ProductCreate) -> Optional[ProductRead]:
        # Implement the async product creation logic using ProductDB model
        pass

    @staticmethod
    async def list_all(db) -> List[ProductRead]:
        # Implement the async query to fetch all product rows
        pass
