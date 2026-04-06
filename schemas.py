from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str

class User(BaseModel):
    name: str
    role: str
    
class TransactionWithUser(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str
    user: User