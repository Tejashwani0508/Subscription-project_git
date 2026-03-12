from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class SubscriptionBase(BaseModel):
    title: str
    cost: float
    start_date: date
    end_date: date
    type: str
    autopay: bool = False

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionUpdate(BaseModel):
    title: Optional[str] = None
    cost: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    type: Optional[str] = None
    autopay: Optional[bool] = None

class SubscriptionResponse(SubscriptionBase):
    id: int
    
    class Config:
        from_attributes = True

class SubscriptionWithDaysLeft(SubscriptionResponse):
    days_left: int
    is_active: bool

class UpcomingRenewal(SubscriptionResponse):
    days_until_renewal: int

class DashboardResponse(BaseModel):
    total_monthly_spend: float
    total_subscriptions: int
    active_subscriptions: int
    subscriptions: List[SubscriptionWithDaysLeft]
    upcoming_renewals: List[UpcomingRenewal]
