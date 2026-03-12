from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from database import Base
from datetime import date

class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    type = Column(String(50), nullable=False)  # e.g., "Monthly", "Yearly", "Weekly"
    autopay = Column(Boolean, default=False)
