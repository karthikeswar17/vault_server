from typing import Optional

from fastapi import FastAPI,Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

@app.get("/accounts")
def get_all_accounts(credentials: HTTPBasicCredentials = Depends(security)):
    return [{'name':'google','username':'test','password':'test_pass'}]
