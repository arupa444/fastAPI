from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field
from typing import Annotated, Dict




class BankPatientRelationshipDataStruct(BaseModel):
    name: Annotated[str, Field(min_length=1,title="Name of the patient", description="Enter the name of the patient but that must be greater then 1")]
    age: Annotated[int, Field(gt=0, lt=40, strict=True, title="The patients age", description="The age must inbetween 0 - 40")]
    email: EmailStr
    referal: Annotated[AnyUrl, Field(strict=True)]
    contact: Dict[str, str]

    @field_validator('email')
    @classmethod
    def emailValidator(cls, value):
        bankWithThisFeature = ["icici.com", "idbi.com", "sbi.com"]
        if value.split("@")[-1] not in bankWithThisFeature:
            raise "not a bank with this feature"
        return value
    
    @field_validator("name")
    @classmethod
    def transformName(cls, value):
        return value.upper()
    
    @model_validator(mode="after")
    def addEmeragencyContact(cls, model):
        if model.age<20 and 'emergancy' not in model.contact:
            raise "add a emergency contact in contacts"
        return model
    
    @computed_field
    @property
    def amountRaise(self)-> int:
        raisedAmount = self.age * 200000
        return raisedAmount




def verifyYourSelfForEligibility(patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.referal)
    print(patient.amountRaise)
    print("vaild.....\n\n")


def updatePatientID(patient):
    print(patient.contact)
    print("updated....")


store = {
    "name" : "Arupa",
    "age" : 21,
    "email" : "arupaswain7735@idbi.com",
    "referal" : "https://www.geeksforgeeks.org/python/get-current-timestamp-using-python/",
    "contact": {
        "phone": "12134214",
        "emergancy": "8688"
    }
}
patientObj = BankPatientRelationshipDataStruct(**store)

verifyYourSelfForEligibility(patientObj)
updatePatientID(patientObj)