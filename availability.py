import requests
from datetime import datetime
import time


# finds and prints all Resy availabilities for a restaurant
# day, party size, and restaurant are all taken as input
def find_availability(restaurant_name, venue_id, party_size, day, early_time, late_time, attempt_num):
    url = "https://api.resy.com/4/find"
    headers = {
        "Authorization": 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
        "Content-Type": "application/json",
        "Host": "api.resy.com",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate"
    }
    params = {
        "lat": "0",
        "long": "0",
        "day": str(day), 
        "party_size": str(party_size),
        "venue_id": str(venue_id) 
    }

    try:
        print("Trying to make reservation at " + restaurant_name)
        print("Attempt number: " +str(attempt_num))
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Check for any error in the response

        data = response.json()

        # finds all availabilities on the day specified
        if "results" in data:
            print("results")
            results = data["results"]
            if "venues" in results:
                print("venues")
                venues = results["venues"]
                if "slots" in venues[0]:
                    print("slots")
                    slots = venues[0]["slots"]
                    print(slots)
                    if len(slots) == 0:
                        time.sleep(300) # if no availabilities, wait 5 minutes and check again
                        attempt_num+= 1
                        find_availability(restaurant_name, venue_id, party_size, day, early_time, late_time, attempt_num)
                    for item in slots:
                        if "date" in item:
                            date_time = item["date"]["start"]
                            military_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S") # converts to just time
                            slot_time = military_time.strftime("%I:%M %p") # converts to standard time
                            if early_time <= slot_time <= late_time: # ignores slots outside the time frame specified by the user
                                print(item["config"]["token"])
                                return item["config"]["token"] # returns the book token
                            
    # handles exceptions if request fails
    except requests.exceptions.RequestException as e:
        print("Error occurred: availability")
        return "fail"

if __name__ == "__main__":
    find_availability("Hudson Clearwater", "5853", "2", "2024-01-4", "06:00 PM", "07:00 PM")

