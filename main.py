from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def fetchData():
    with open('patients.json','r') as fetchable:
        data = json.load(fetchable)
        return data


@app.get("/")
def hello():
    return {"message":"Patient management system api"}

@app.get("/about")
def aboutMe():
    return {"message":"Here we gonna update the patients info in doctors dashboard."}

@app.get("/view")
def viewTheData():
    data = fetchData()
    return data

@app.get("/patient/{p_id}")
def fetchOneP(p_id: str = Path(..., description='Enter your patient id here....', example="P001",max_length=4)):
    data = fetchData()
    if p_id in data:
        return data[p_id]
    raise HTTPException(status_code=404, detail='patient not found in DB')

@app.get("/sort")
def sortedData(sortBy: str= Query(..., description="Enter the field that you want to sort...", example="bmi"), ):