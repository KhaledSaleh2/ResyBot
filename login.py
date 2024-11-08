import requests

def login():
    url = "https://api.resy.com/3/auth/password"
    headers = {
        "Authorization": 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
    }
    email = input("Please type your email for resy.com account: ")
    password = input("Please enter your password for this account: ")
    data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Check for any error in the response

        # If the request is successful, you can handle the response data here

        response_data = response.json()
        if "payment_methods" in response_data:
            if "id" in response_data["payment_methods"]:
                return response_data["payment_methods"]["id"]
            else:
                raise Exception("Must have a card on file on your resy.com account")
                return "fail"
        else:
                raise Exception("Must have a card on file on your resy.com account")
                return "fail"


    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
