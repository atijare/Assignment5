from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import models, schemas

def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def read_all_resources(db: Session):
    return db.query(models.Resource).all()

def read_resource(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update_resource(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    if not db_resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    db_resource.update(resource.dict(), synchronize_session=False)
    db.commit()
    return db_resource.first()

def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    if not db_resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    db_resource.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
