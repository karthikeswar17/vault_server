from sqlalchemy.orm import Session

import models, schemas


def get_accounts(db: Session):
    return db.query(models.Account).all()
    # .filter(models.Account.id == id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, username: str):
    return db.query(models.User).filter(username == models.User.username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username,
                             password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def create_account(db: Session, account: schemas.AccountCreate, user_id: int):
    db_user = models.Account(name=account.name, username=account.username,
                             password=account.password, url=account.url, user_id= user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
