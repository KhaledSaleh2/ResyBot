# ResyBot

**ResyBot** is a Python script designed to automatically book restaurant reservations on Resy.com, specifically for high-demand restaurants in New York. The script relies on a dictionary of some of the hardest-to-obtain reservations (see `id_library.py`), so it can only work with these predefined restaurants.

## How It Works
1. **User Input**:  
   The script collects the following details from the user:
   - Resy.com username and password
   - Desired restaurant
   - Party size
   - Time preference  

2. **Reservation Search**:  
   Using this information, the script checks every 5 minutes to see if a reservation that matches the user's criteria becomes available.  

3. **Booking**:  
   If a reservation opens up, the script automatically books it.  
   **Note**: A valid Resy.com account and a payment method linked to the account are required for the script to function.

4. **API Calls**:  
   The script interacts with Resy's APIs using four types of network calls:  
   - `login`: Authenticates the user  
   - `availability`: Checks for open reservations  
   - `details`: Retrieves specific reservation details  
   - `book`: Books the reservation  

   Each API call is implemented in its respective file within the script.

## DISCLAIMER
As of December 2023, the script is no longer functional.  

The exact cause is unknown, but it is possible that Resy has implemented measures to block scripts like this. I have been unable to identify a workaround.  

If you are interested, feel free to investigate the issue and explore potential solutions.
