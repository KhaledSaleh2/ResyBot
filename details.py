import requests
import json
import availability
from datetime import datetime, date
import id_library

def find_book_token():
    url = "https://api.resy.com/3/details"

    restaurant_name = input("Please enter the name of your desired restaurant\n")
    restaurant_library = restaurant_name.lower().strip()
    venue_id = id_library.get_venue_id(restaurant_library) # input name of restaurant
    party_size = get_positive_integer_input() # input party size
    day = get_valid_date() # input desired day
    early_time = get_valid_time_early()
    late_time = get_valid_time_late()

    print(venue_id)
    print(party_size)
    print(day)
    print(early_time)
    print(late_time)

    details_token = availability.find_availability(restaurant_name, venue_id, party_size, day, early_time, late_time, 1)
    if details_token == "fail":
        return "fail"

    body = {
        "commit": "1",
        "config_id": details_token,
        "day": str(day),
        "party_size": str(party_size)
    }

    headers = {
       "Authorization": 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        data = response.json()
        if "book_token" in data:
            return data["book_token"]["value"]
        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Response:")
            print(response.text)
            return "fail"

    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)

# gets a positive integer inputted from user
def get_positive_integer_input():
    while True:
        try:
            user_input = int(input("What is your party size? "))  # Get input from the user
            if user_input <= 0:
                print("Please enter a positive integer.")
            else:
                return user_input  # Return the input if it's a positive integer
        except ValueError:
            print("Invalid input. Please enter an integer.")

# gets a valid date inputted from user
def get_valid_date():
    while True:
        try:
            date_input = input("Please enter a date in YYYY-MM-D format: ")
            input_date = datetime.strptime(date_input, '%Y-%m-%d').date()

            # Get the current date
            current_date = date.today()

            if input_date < current_date:
                print("Date cannot be before the current date.")
            else:
                return date_input  # Return the input if it matches the specified format and is not before the current date
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

def get_valid_time_early():
    while True:
        try:
            time_input = input("Please enter your earliest desired time for this reservation in HH:MM AM/PM format: ")
            datetime.strptime(time_input, "%I:%M %p")
            return time_input  # Return the input if it matches the specified format
        except ValueError:
            print("Invalid time format. Please enter in HH:MM AM/PM format.")

def get_valid_time_late():
    while True:
        try:
            time_input = input("Please enter your latest desired time for this reservation in HH:MM AM/PM format: ")
            datetime.strptime(time_input, "%I:%M %p")
            return time_input  # Return the input if it matches the specified format
        except ValueError:
            print("Invalid time format. Please enter in HH:MM AM/PM format.")