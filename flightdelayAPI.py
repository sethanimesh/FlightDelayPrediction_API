from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

#Creating an instance of the application
app = FastAPI()

#Structure of the request body
class flight_info(BaseModel):
    carrier_code: str
    scheduled_elapsed_time: int
    delay_weather: int
    HourlyPrecipitation_x: float
    HourlyWindSpeed_x: float

#Loading the model
with open("best_model.pkl", 'rb') as f:
    model = pickle.load(f)

@app.post('/flight-prediction')
async def func(info:flight_info):
    df = pd.DataFrame([info.dict().values()], columns = info.dict().keys())
    yhat = model.predict(df)
    return {"prediction": float(yhat[0])}