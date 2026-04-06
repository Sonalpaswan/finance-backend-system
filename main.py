from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, SessionLocal

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Role check
def check_role(user, allowed_roles):
    if user.role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Access denied")

# Home
@app.get("/")
def home():
    return {"msg": "working"}

# CREATE → Admin only
@app.post("/transactions")
def create(data: schemas.TransactionWithUser, db: Session = Depends(get_db)):
    
    if data.user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create")

    return crud.create_transaction(db, data)
    check_role(user, ["admin"])
    return crud.create_transaction(db, data)

# READ → All roles
@app.get("/transactions")
def read(user: schemas.User, db: Session = Depends(get_db)):
    check_role(user, ["admin", "analyst", "viewer"])
    return crud.get_transactions(db)

# UPDATE → Admin only
@app.put("/transactions/{id}")
def update(id: int, data: schemas.TransactionCreate, user: schemas.User, db: Session = Depends(get_db)):
    check_role(user, ["admin"])

    result = crud.update_transaction(db, id, data)

    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return result

# DELETE → Admin only
@app.delete("/transactions/{id}")
def delete(id: int, user: schemas.User, db: Session = Depends(get_db)):
    check_role(user, ["admin"])

    result = crud.delete_transaction(db, id)

    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return result

# FILTER → Admin + Analyst
@app.get("/transactions/filter")
def filter(type: str = None, category: str = None, user: schemas.User = None, db: Session = Depends(get_db)):
    check_role(user, ["admin", "analyst"])

    return crud.filter_transactions(db, type, category)

# SUMMARY → Admin + Analyst
@app.get("/summary")
def summary(user: schemas.User, db: Session = Depends(get_db)):
    check_role(user, ["admin", "analyst"])

    return crud.get_summary(db)
@app.get("/transactions/filter")
def filter(type: str = None, category: str = None, date: str = None, user: schemas.User = None, db: Session = Depends(get_db)):
    
    check_role(user, ["admin", "analyst"])

    return crud.filter_transactions(db, type, category, date)
@app.get("/summary/category")
def category(user: schemas.User, db: Session = Depends(get_db)):
    
    check_role(user, ["admin", "analyst"])

    return crud.category_summary(db)
@app.get("/transactions")
def read(skip: int = 0, limit: int = 5, user: schemas.User = None, db: Session = Depends(get_db)):
    
    check_role(user, ["admin", "analyst", "viewer"])
