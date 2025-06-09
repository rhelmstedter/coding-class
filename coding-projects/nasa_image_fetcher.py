import os
import datetime
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image
from rich import print
from rich.status import Status

API_KEY = os.environ["NASA_API"]
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
IMAGE_DIR = Path() / "images"
FIRST_DATE = datetime.datetime(1995, 6, 16)
DATE_FORMAT = "%Y-%m-%d"


def fetch_image(date):
    """Use the NASA Astronomy picture of the day API to fetch and download an image
    based on a given date"""
    with Status("Sending API request...") as status:
        url_for_date = f"{API_URL}&date={date}"
        response = requests.get(url_for_date)
        response.raise_for_status()
        data = response.json()

        status.update("Fetching Image...")
        image_response = requests.get(data["hdurl"])
        response.raise_for_status()

        status.update("Saving Image...")
        image = Image.open(BytesIO(image_response.content))
        title = data["title"]
        image.show()
        # image_name = f"{title}.{image.format}"
        # image.save(IMAGE_DIR / image_name, image.format)
        image.close()

    description = data["explanation"]
    print(f"\n:rocket: [bold]{title}[/bold] :rocket:\n")
    print(description)


def get_date():
    while True:
        date = input(
            "Enter a date in the form YYYY-MM-DD or just press enter for today:\n> "
        )
        if not date:
            return datetime.datetime.now().strftime(DATE_FORMAT)

        year, month, day = date.split("-")

        try:
            entered_date = datetime.datetime.strptime(date, DATE_FORMAT)
        except ValueError:
            print("Please enter a valid date.")
        if entered_date < FIRST_DATE:
            print("There are no pictures available before 1995-06-16")
        elif entered_date > datetime.datetime.now():
            print("There are no pictures available from the future.")
        else:
            break
    return date


if __name__ == "__main__":
    date = get_date()
    fetch_image(date)
