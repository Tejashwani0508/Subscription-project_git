from sqlalchemy.orm import Session
from models import Subscription
from schemas import SubscriptionCreate, SubscriptionUpdate

# CREATE
def create_subscription(db: Session, subscription: SubscriptionCreate) -> Subscription:
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

# READ
def get_subscription(db: Session, subscription_id: int) -> Subscription:
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()

def get_all_subscriptions(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(Subscription).offset(skip).limit(limit).all()

# UPDATE
def update_subscription(db: Session, subscription_id: int, subscription: SubscriptionUpdate) -> Subscription:
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if db_subscription is None:
        return None
    
    update_data = subscription.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_subscription, field, value)
    
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

# DELETE
def delete_subscription(db: Session, subscription_id: int) -> bool:
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if db_subscription is None:
        return False
    
    db.delete(db_subscription)
    db.commit()
    return True
