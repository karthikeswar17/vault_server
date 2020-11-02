from typing import Optional, List

from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def get_current_username(credentials: HTTPBasicCredentials = Depends(security),db: Session = Depends(get_db)):
    user = crud.get_user(db, credentials.username)
    hash_pass = credentials.password
    # raise Exception(user.password,hash_pass)
    if not user or hash_pass != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
    
@app.post("/accounts", response_model=schemas.Account)
def create_account(account:schemas.AccountCreate ,username: str = Depends(get_current_username),db: Session = Depends(get_db)):
    user_id = crud.get_user(db, username).id
    users = crud.create_account(db, account, user_id)
    return users

@app.post("/user", response_model=schemas.User)
def create_user(user:schemas.UserCreate ,db: Session = Depends(get_db)):
    users = crud.create_user(db, user)
    return users

@app.get("/accounts", response_model=List[schemas.Account])
def get_all_accounts(username: str = Depends(get_current_username),db: Session = Depends(get_db)):
    user = crud.get_user(db, username)
    if user:
        accounts = user.accounts
        return accounts
    

@app.get("/user", response_model=List[schemas.User],)
def get_all_users(username: str = Depends(get_current_username),db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users
