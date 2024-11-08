import login
import details
import requests

def book_reservation():

    payment_id = login.login()
    if payment_id == "fail":
        return
    book_token = details.find_book_token()
    if book_token == "fail":
        return

    url = "https://api.resy.com/3/book"

    headers = {
        "Authorization": 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
        "Content-Type": "application/json",
        "Host": "api.resy.com",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate"
    }
    body = {
        "book_token": str(book_token),
        "struct_payment_method": payment_id,
        "source_id": "resy.com-venue-details"
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        print(f"Request failed with status code: {response.status_code}")
        print("Response:")
        print(response.text)
        print("The reservation was a success!")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    
