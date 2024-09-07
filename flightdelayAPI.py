from fastapi import FastAPI
from pydantic import BaseModel
#Creating an instance of the application
app = FastAPI()

#Structure of the request body
class flight_info(BaseModel):
    carrier_code: str
    scheduled_elapsed_time: int
    delay_weather: int
    HourlyPrecipitation_x: float
    HourlyWindSpeed_x: float

@app.post('/flight-prediction')
async def func(info:flight_info):
    return info