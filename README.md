# Inventrack - Product Database Integration Challenge

## Task Overview
Inventrack operates an inventory management platform where product information is handled through a FastAPI backend. The API endpoints for adding new products and retrieving the current product list are implemented. However, database support is missing—there is no schema or data access logic yet. Your job is to enable persistent product storage by creating an appropriate PostgreSQL schema and implementing the async Python logic to insert and fetch products.

## Guidance
- The API code and main routing logic are complete in `app/main.py`. 
- Implement your database schema in `schema.sql` and async integration logic in `app/database.py` and `app/models.py`.
- Use the included `run.sh` script to start all services and initialize the PostgreSQL database within Docker.

## Objectives
- Design and create a PostgreSQL table to persist product records with columns for: name, SKU (unique), quantity (integer), and last_updated (timestamp).
- Implement SQLAlchemy models and async DB logic (CRUD) to support adding and retrieving products via the existing API.
- Ensure that all DB access is non-blocking (fully async with SQLAlchemy/asyncpg).
- Apply sensible keys, uniqueness, and an index on SKU for fast lookups.
- Do not modify endpoint logic or API contract—focus on database files and logic only.

## How to Verify
- Bring up all services using `./run.sh`. 
- Use the FastAPI docs (http://localhost:8000/docs) to add a new product and list products.
- Confirm that products persist between restarts (database is being used, not in-memory storage).
- Try adding duplicate SKUs to check that your uniqueness constraint is enforced at the DB level.
- Check that all product information is returned via API exactly as stored in the database.
