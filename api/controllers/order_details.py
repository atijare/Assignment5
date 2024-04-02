from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas

def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def read_order_detail(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update_order_detail(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    db_order_detail.update(order_detail.dict(), synchronize_session=False)
    db.commit()
    return db_order_detail.first()

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_detail.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
