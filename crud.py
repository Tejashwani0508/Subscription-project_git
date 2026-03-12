from sqlalchemy.orm import Session
from models import Subscription
from schemas import SubscriptionCreate, SubscriptionUpdate
from datetime import date, timedelta

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

# DASHBOARD
def get_dashboard_data(db: Session) -> dict:
    """
    Get comprehensive dashboard data including:
    - Total monthly spend
    - All subscriptions with days left
    - Upcoming renewals within 7 days
    """
    today = date.today()
    subscriptions = db.query(Subscription).all()
    
    # Calculate total monthly spend
    total_monthly_spend = 0.0
    for sub in subscriptions:
        if sub.type.lower() == "monthly":
            total_monthly_spend += sub.cost
        elif sub.type.lower() == "yearly":
            # For yearly, calculate approximate monthly cost
            total_monthly_spend += sub.cost / 12
    
    # Calculate subscriptions with days left and active status
    subscriptions_with_days = []
    for sub in subscriptions:
        days_left = (sub.end_date - today).days
        is_active = days_left > 0
        subscriptions_with_days.append({
            "id": sub.id,
            "title": sub.title,
            "cost": sub.cost,
            "start_date": sub.start_date,
            "end_date": sub.end_date,
            "type": sub.type,
            "autopay": sub.autopay,
            "days_left": days_left,
            "is_active": is_active
        })
    
    # Get upcoming renewals within 7 days
    upcoming_renewals = []
    for sub in subscriptions:
        days_until_renewal = (sub.end_date - today).days
        if 0 <= days_until_renewal <= 7:
            upcoming_renewals.append({
                "id": sub.id,
                "title": sub.title,
                "cost": sub.cost,
                "start_date": sub.start_date,
                "end_date": sub.end_date,
                "type": sub.type,
                "autopay": sub.autopay,
                "days_until_renewal": days_until_renewal
            })
    
    # Sort upcoming renewals by days until renewal
    upcoming_renewals.sort(key=lambda x: x["days_until_renewal"])
    
    # Count active subscriptions
    active_subscriptions = sum(1 for sub in subscriptions_with_days if sub["is_active"])
    
    return {
        "total_monthly_spend": round(total_monthly_spend, 2),
        "total_subscriptions": len(subscriptions),
        "active_subscriptions": active_subscriptions,
        "subscriptions": subscriptions_with_days,
        "upcoming_renewals": upcoming_renewals
    }
