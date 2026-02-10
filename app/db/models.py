from sqlalchemy import Column, Integer, String
from app.db.database import Base

class PatrolLog(Base):
    __tablename__ = "patrol_logs"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    text = Column(String)
    crowd_level = Column(String)
