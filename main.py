from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def fetchData():
    with open('patients.json','r') as fetchable:
        data = json.load(fetchable)
        return data


@app.get("/")
def home():
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
def sortedData(sortBy: str= Query(..., description="The field that you want to sort...", example="bmi"), order: str= Query("asc", description="The order will be in ascending or decending order.", example="asc")):
    vaild_fields = ["height", "weight", "bmi"]

    if sortBy not in vaild_fields:
        raise HTTPException(status_code=400, detail=f"Invalid feild select from {vaild_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Enter a valid input either asc or desc")
    
    data = fetchData()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x[sortBy], reverse=sort_order)

    return sorted_data