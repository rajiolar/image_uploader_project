from sqlalchemy import Column, ForeignKey, String, Integer
from model import Base


class Document (Base):
    __tablename__ = "document"
    
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    original_file_url = Column(String, nullable=True)
    converted_file_url = Column(String, nullable=True)
    
   