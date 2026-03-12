from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db, Base
from models import Subscription
from schemas import SubscriptionCreate, SubscriptionResponse, SubscriptionUpdate
import crud

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Subscription Management System",
    description="API for managing subscriptions with CRUD operations",
    version="1.0.0"
)

# CRUD Endpoints

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to Subscription Management System API"}

# CREATE - Add a new subscription
@app.post("/subscriptions", response_model=SubscriptionResponse, status_code=status.HTTP_201_CREATED, tags=["Subscriptions"])
def create_subscription(
    subscription: SubscriptionCreate,
    db: Session = Depends(get_db)
):
    """Create a new subscription"""
    return crud.create_subscription(db=db, subscription=subscription)

# READ - Get all subscriptions
@app.get("/subscriptions", response_model=List[SubscriptionResponse], tags=["Subscriptions"])
def get_all_subscriptions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all subscriptions with optional pagination"""
    subscriptions = crud.get_all_subscriptions(db=db, skip=skip, limit=limit)
    return subscriptions

# READ - Get a specific subscription
@app.get("/subscriptions/{subscription_id}", response_model=SubscriptionResponse, tags=["Subscriptions"])
def get_subscription(
    subscription_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific subscription by ID"""
    subscription = crud.get_subscription(db=db, subscription_id=subscription_id)
    if subscription is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subscription with id {subscription_id} not found"
        )
    return subscription

# UPDATE - Update a subscription
@app.put("/subscriptions/{subscription_id}", response_model=SubscriptionResponse, tags=["Subscriptions"])
def update_subscription(
    subscription_id: int,
    subscription: SubscriptionUpdate,
    db: Session = Depends(get_db)
):
    """Update a subscription"""
    db_subscription = crud.update_subscription(db=db, subscription_id=subscription_id, subscription=subscription)
    if db_subscription is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subscription with id {subscription_id} not found"
        )
    return db_subscription

# DELETE - Delete a subscription
@app.delete("/subscriptions/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Subscriptions"])
def delete_subscription(
    subscription_id: int,
    db: Session = Depends(get_db)
):
    """Delete a subscription"""
    success = crud.delete_subscription(db=db, subscription_id=subscription_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subscription with id {subscription_id} not found"
        )
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
