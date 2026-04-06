from sqlalchemy.orm import Session
import models

def create_transaction(db, data):
    transaction = models.Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        notes=data.notes
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transactions(db: Session):
    return db.query(models.Transaction).all()
def update_transaction(db, id, data):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    
    if not transaction:
        return None

    for key, value in data.dict().items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction
def delete_transaction(db, id):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return {"msg": "Deleted"}
def filter_transactions(db, type=None, category=None):
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)

    if category:
        query = query.filter(models.Transaction.category == category)

    return query.all()
def get_summary(db):
    transactions = db.query(models.Transaction).all()

    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
    def filter_transactions(db, type=None, category=None, date=None):
     query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)

    if category:
        query = query.filter(models.Transaction.category == category)

    if date:
        query = query.filter(models.Transaction.date == date)

    return query.all()
def category_summary(db):
    transactions = db.query(models.Transaction).all()
    result = {}

    for t in transactions:
        if t.category not in result:
            result[t.category] = 0
        result[t.category] += t.amount

    return result