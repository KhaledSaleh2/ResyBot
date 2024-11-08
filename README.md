# ResyBot
ResyBot is a script that can be ran to automatically book a restaurant (specifically in New York) reservations on Resy.com as they open up. 
The script uses a dictionary of some of the hardest to obtain reservations in New York, and thus can only work for one of the listed restaurants (see id_library.py).

# How it works:
The script works by taking in input from the user, such as their resy.com username and password, desired restaurant, party size, time preference, etc. 
The script then uses this information to repeatedly check every 5 minutes if a reservation opens that matches the inputted parameters. If yes, it books said reservation.
Users must have a resy.com account, as well as a form of payment listed on their account, in order for the script to work.

The script uses the parameters to send different network calls to the Resy APIs. The script uses 4 different API network calls: login, availability, details, and book. Each of these are reflected in their respective file.

# DISCLAIMER
The script has suddenly stopped working as of December 2023. I am not sure as to why it suddenly stopped working (maybe resy is cracking down on these types of things), and have been unable to work around it.
Feel free to investigate why the script no longer works, and potentially find a way around it.
