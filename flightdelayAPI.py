from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

#Creating an instance of the application
app = FastAPI()

# Allowing CORS for specific origins (replace with your frontend URL if deployed)
origins = [
    "http://localhost:3000",  # React development URL
    "https://main--flighttracker.netlify.app",  # Production domain of your frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

#Structure of the request body
class flight_info(BaseModel):
    carrier_code: str
    scheduled_elapsed_time: int
    delay_weather: int
    HourlyPrecipitation_x: float
    HourlyWindSpeed_x: float

# Dictionary to map airline codes to integers
airline_code_mapping = {
    "AA": 0,
    "AS": 1,
    "B6": 2,
    "DL": 3,
    "F9": 4,
    "G4": 5,
    "HA": 6,
    "NK": 7,
    "UA": 8,
    "WN": 9
}

#Loading the model
with open("best_model.pkl", 'rb') as f:
    model = pickle.load(f)

@app.get("/")
def response_func():
    return "Hello"

@app.post('/flight-prediction')
async def func(info: flight_info):
    # Map the carrier_code to the corresponding integer
    if info.carrier_code in airline_code_mapping:
        info_dict = info.dict()
        info_dict['carrier_code'] = airline_code_mapping[info.carrier_code]
    else:
        return {"error": "Invalid carrier code"}

    # Convert the request data into a DataFrame
    df = pd.DataFrame([info_dict.values()], columns=info_dict.keys())

    # Make the prediction using the loaded model
    yhat = model.predict(df)

    # Return the prediction
    return {"prediction": float(yhat[0])}
