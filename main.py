from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()

#pydantic model

class Disease(BaseModel):
    name : Annotated[str, Field(..., title="The diseases that the patient have...", description="Enter the disease that the patient have....")]
    description : Annotated[str, Field(..., title="The disease description that the patient have", description="Enter the description that the patient have...")]

class Patient(BaseModel):
    id : Annotated[str, Field(..., title="Id of the patient", description="Enter the id of the patient..")]
    name : Annotated[str, Field(..., title="Name of the patient", description="Enter the patient name")]
    city : Annotated[str, Field(..., title="place he/she lives", description="Enter the place the patient lives....")]
    age : Annotated[int, Field(..., gt=0, lt=111, title="The age of the patient", description="Enter the patient's age...")]
    feeling : Annotated[Literal["Worst","Normal","Good","Better","Best"], Field(..., title="The patient state of emotion" ,description="Enter the way you feeling rn...")]
    gender : Annotated[str, Field(..., title="The gender of the patient...", description="Enter the patients Gender...")]
    height : Annotated[float, Field(..., gt=0,title="The height of the patient", description="Enter the patient height..")]
    weight : Annotated[float, Field(..., gt=0,title="The Weight of the patient", description="Enter the patient weight...")]
    disease : Annotated[Disease, Field(title="The disease details", description="Enter the disease details...")]

    @computed_field
    @property
    def bmi(self)-> float:
        patientBMI = round(self.weight/(self.height**2),2)
        return patientBMI
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

    @field_validator('gender')
    @classmethod
    def validateGender(cls, value):
        store = ["Male", "Female"]
        if value not in store:
            raise ValueError("Enter the correct gender[Male or Female]")
        return value

class UpdatePatient(BaseModel):
    name : Annotated[Optional[str], Field(default=None, title="Name of the patient", description="Enter the patient name")]
    city : Annotated[Optional[str], Field(default=None, title="place he/she lives", description="Enter the place the patient lives....")]
    age : Annotated[Optional[int], Field(default=None, gt=0, lt=111, title="The age of the patient", description="Enter the patient's age...")]
    feeling : Annotated[Optional[Literal["Worst","Normal","Good","Better","Best"]], Field(default=None, title="The patient state of emotion" ,description="Enter the way you feeling rn...")]
    gender : Annotated[Optional[str], Field(default=None, title="The gender of the patient...", description="Enter the patients Gender...")]
    height : Annotated[Optional[float], Field(default=None, gt=0,title="The height of the patient", description="Enter the patient height..")]
    weight : Annotated[Optional[float], Field(default=None, gt=0,title="The Weight of the patient", description="Enter the patient weight...")]
    disease : Annotated[Optional[Disease], Field(default=None, title="The disease details", description="Enter the disease details...")]















def fetchData():
    with open('patients.json','r') as file:
        data = json.load(file)
        return data
    
def saveData(data):
    with open('patients.json','w') as file:
        json.dump(data, file)


@app.get("/")
def home():
    return {"message":"Patient management system api"}

@app.get("/about")
def aboutMe():
    return {"message":"Patient management system api which gonna help you in managing your web apps....\nuse them and give stars if you likes it..."}

@app.get("/view")
def viewTheData():
    data = fetchData()
    print(data["P002"]["gender"])
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

@app.post("/create")
def addPatient(patient: Patient):
    data = fetchData()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="The patient is already exists")
    data[patient.id] = patient.model_dump(exclude=["id"])

    saveData(data)
    return JSONResponse(status_code=201, content={"message": "Patient is successfully added"})


@app.put("/update/{patient_id}")
def updatePatient(patient_id: str, patient : UpdatePatient):
    data = fetchData()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    tempStoreUpdatedDataOfPatient = patient.model_dump(exclude_defaults=True)

    thatPatientData = data[patient_id]
    thatPatientData["id"] = patient_id

    for key, value in tempStoreUpdatedDataOfPatient.items():
        thatPatientData[key] = value
    
    objectForPatient = Patient(**thatPatientData)

    tempStoreAllDataForUpdate = objectForPatient.model_dump(exclude=["id"])
    data[patient_id] = tempStoreAllDataForUpdate
    

    saveData(data)
    return JSONResponse(status_code=200, content={"Message":"The data is updated"})


@app.delete("/delete/{patient_id}")
def deletePatient(patient_id):
    data = fetchData()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    
    del data[patient_id]

    saveData(data) # save data

    return JSONResponse(status_code=200, content={"message":f"Perfectly deleted the {patient_id}"})