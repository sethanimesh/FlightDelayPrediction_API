
# Flight Delay Prediction API

This API predicts flight delays based on real-time weather and airline data. It is built using FastAPI and is deployed on Heroku for easy access.

## Features

- **FastAPI Framework**: Modern and fast web framework for creating APIs.
- **CORS Middleware**: Allows cross-origin requests from any origin.
- **Model Prediction**: Uses a pre-trained Random Forest model to predict delays based on flight and weather data.
- **Heroku Deployment**: Deployed on Heroku for easy cloud access.

## Requirements

- Python 3.7+
- FastAPI
- Pandas
- Pickle (for model loading)

## Project Files

- **Procfile**: Specifies how the app is run on Heroku.
- **runtime.txt**: Specifies the Python version.
- **requirements.txt**: Lists all dependencies required to run the project.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sethanimesh/FlightDelayPrediction_API.git
   ```

2. **Install dependencies**:

   You can install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally**:

   You can start the FastAPI server using Uvicorn:

   ```bash
   uvicorn flightdelayAPI:app --reload
   ```

   The application will now be running at `http://127.0.0.1:8000`.

4. **Model File**:

   Ensure that the `best_model.pkl` file is placed in the root directory of your project. This file should contain the trained model used for making predictions.

## Heroku Deployment Instructions

This application is already set up for deployment on Heroku. To deploy your own version, follow these steps:

1. **Login to Heroku**:

   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:

   ```bash
   heroku create
   ```

3. **Deploy the app**:

   ```bash
   git push heroku main
   ```

4. **Check logs**:

   ```bash
   heroku logs --tail
   ```

5. **Access the app**: Once deployed, you can access the app at the URL provided by Heroku.

### **Heroku-specific Files**

- **Procfile**: Specifies how to run the FastAPI application on Heroku using Uvicorn.
  ```bash
  web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker flightdelayAPI:app
  ```

- **runtime.txt**: Specifies the Python version to use on Heroku.
  ```txt
  python-3.9.12
  ```

- **requirements.txt**: Lists the Python dependencies needed to run the project.
  ```txt
  fastapi==0.70.0
  uvicorn==0.15.0
  pandas==1.3.3
  gunicorn==20.1.0
  ```

## API Endpoints

### **GET** `/`

- **Description**: Returns a welcome message to verify that the API is running.
- **Response**:
  ```json
  {
    "message": "Hello, the Flight Delay Prediction API is running!"
  }
  ```

### **POST** `/predict`

- **Description**: Takes in flight information and returns whether the flight is predicted to be delayed.
- **Request Body**:
  ```json
  {
    "carrier_code": "AA",
    "scheduled_elapsed_time": 180,
    "delay_weather": 1,
    "HourlyPrecipitation_x": 0.5,
    "HourlyWindSpeed_x": 10.5
  }
  ```
- **Response**:
  ```json
  {
    "prediction": "Delayed" 
  }
  ```

## Input Parameters

- **carrier_code** (str): Airline code (e.g., AA, DL, UA)
- **scheduled_elapsed_time** (int): Scheduled flight time in minutes.
- **delay_weather** (int): Indicates if there is a weather delay (1 for yes, 0 for no).
- **HourlyPrecipitation_x** (float): The hourly precipitation value at the time of the flight.
- **HourlyWindSpeed_x** (float): The hourly wind speed at the time of the flight.

## License

This project is licensed under the MIT License.
