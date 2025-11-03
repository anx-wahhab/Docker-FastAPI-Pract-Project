from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field
import pickle
import pandas as pd

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

app = FastAPI()

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient.')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the patient in meters.')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual Salary of the patient.')]
    smoker: Annotated[bool, Field(..., description='Is user smoker or not ?')]
    city: Annotated[str, Field(..., description='City of the patient')]
    occupation: Annotated[str, Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the patient')]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        return 'young' if self.age < 25 \
            else 'adult' if self.age < 45 \
            else 'middle_aged' if self.age < 60 \
            else 'Senior'

    @computed_field
    @property
    def city_tier(self) -> int:
        return 1 if self.city in tier_1_cities else 2 if self.city in tier_2_cities else 3

@app.get('/')
def root():
    return JSONResponse({'message': 'Insurance Premium API'})

@app.post('/predict')
def predict(instance: UserInput):
    input_ = pd.DataFrame({
        'bmi': instance.bmi,
        'age_group': instance.age_group,
        'lifestyle_risk': instance.lifestyle_risk,
        'city_tier': instance.city_tier,
        'income_lpa': instance.income_lpa,
        'occupation': instance.occupation
    }, index=[0])

    return JSONResponse(status_code=200, content={"prediction": model.predict(input_)[0]})
