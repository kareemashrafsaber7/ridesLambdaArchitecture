from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from connection import send_to_event_hub
from data import generate_uber_ride_confirmation


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/")
def booking_home(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        }
    )


# ============================================================
# BOOK RIDE
# ============================================================

@app.get("/book")
def book_ride(request: Request):

    # Generate one ride event
    ride = generate_uber_ride_confirmation()

    # Send ride event to Event Hub
    result = send_to_event_hub(ride)

    return templates.TemplateResponse(
        "confirmation.html",
        {
            "request": request
        }
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )