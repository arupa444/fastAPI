from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional
from datetime import datetime
import time

class PydenticVal(BaseModel):
    name: str
    email: EmailStr
    githubURL: Optional[AnyUrl] = None
    age: Optional[int] = None
    drinkingWater: bool
    height: float
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
    print("viewed....")

def updateTheDB(patient):
    print(patient.age)
    print(patient.disease)
    print(patient.githubURL)
    print(patient.updateTime)
    print("updated....")


store = {
    "name":"Arupa",
    "height": "5.10",
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