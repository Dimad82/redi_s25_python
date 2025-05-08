from fastapi import FastAPI
import httpx
# Initialise app
app = FastAPI()

# Trigger the app when the url is accessed
@app.get("/")

# Define the function that is called with the get request
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/weather/{location}")
async def location_weather(location):
    r = httpx.get('https://api.openweathermap.org/data/2.5/weather?q={location}&appid=7943218f495c4502f7d0333c2a6bb63e')
    return r.text


# Main code for app, run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
