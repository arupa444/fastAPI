from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
from datetime import datetime
import time

class PydenticVal(BaseModel):
    name: str
    email: EmailStr
    githubURL: Optional[AnyUrl] = None
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=40, title="Age of the Patient", description="Enter the age and the age must be inbetween 0-40")]
    drinkingWater: bool
    height: Annotated[float,Field(gt=0, strict=True)]
    disease: List[str]
    pets: Optional[Dict[str,str]] = None
    updateTime: Optional[datetime] = None
    viewTime: Optional[datetime] = None



def readTheDB(patient):
    print(patient.name)
    print(patient.height)
    print(type(patient.height))
    print(patient.pets)
    print(patient.email)
    print(patient.viewTime)
    print("viewed....\n\n\n")

def updateTheDB(patient):
    print(patient.age)
    print(patient.disease)
    print(patient.githubURL)
    print(patient.updateTime)
    print("updated....")


store = {
    "name":"Arupa",
    "height": 5.10,
    "age": "21",
    "drinkingWater":True,
    "disease": ["Ashatma", "cancer"],
    "pets": {
        "1": "Hamster",
        "2": "Rabit",
        "3": "Cat"
    },
    "email": "arupaswain7735@gmail.com",
    "githubURL": "https://github.com/SureChEMBL",
    "updateTime": time.time(),
    "viewTime": datetime.utcnow().timestamp()
}

patient1 = PydenticVal(**store)

readTheDB(patient1)
updateTheDB(patient1)