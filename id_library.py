
# Fixed number of restaurants that are considered the hardest
# to get reservations at on Resy in NYC
restaurant_data = {
    "roscioli - tasting menu": "6492",
    "roscioli - a la carte": "5206",
    "cafe carmellini": "74362",
    "sailor": "73658",
    "the polo bar": "6439",
    "four horseman": "2492",
    "the four horseman": "2492",
    "semma": "1263",
    "torrisi bar & restaurant": "64593",
    "carbone": "6194",
    "lilia": "418",
    "atomix": "69815",
    "4 charles prime rib": "834",
    "four charles prime rib": "834",
    "don angie": "1505",
    "via carota": "2567",
    "i sodi": "443",
    "jua": "8266",
    "dame": "34341",
    "tokyo record bar" : "1518",
    "tatiana by kwame onwuachi": "65452",
    "tatiana": "65452",
    "tatiana, by kwame onwuachi": "65452",
    "gramercy tavern": "52209",
    "the dining room at gramercy tavern": "52209",
    "rezdora": "48994",
    "atoboy": "587",
    "sushi nakazawa" : "5589",
    "sofreh": "27154",
    "hudson clearwater": "5853"

    # Open to suggestions! Contact saleh.h.khaled@gmail.com      
}

# Retrieves the venue ID for a given restaurant name
def get_venue_id(name) :
    return restaurant_data.get(name, None)

        