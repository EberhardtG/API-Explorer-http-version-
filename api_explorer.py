"""
DESIGN COMMENTARY

I used the requests library because it allows Python to communicate with
the PokeAPI and retrieve data using HTTP requests.

I created a base_url variable so I don't have to repeat the full API URL
for every request. I then created a list containing three Pokemon names
so I can use a loop to fetch and display information for each Pokemon.

For each Pokemon, I check the status code before trying to access the
response data. A status code of 200 means the request was successful, so
I convert the JSON response into a Python dictionary and extract the
Pokemon's name, height, weight, and types.

I used a list comprehension to extract the type names because a Pokemon
can have more than one type. This allows the program to handle Pokemon
with one or multiple types without needing separate code for each case. also included a timeout for the requests.get() call to avoid the program hanging indefinitely if the API is slow to respond.

I also included a separate request for "pikacu", which does not exist.
The program checks for a 404 status code and displays a helpful error
message instead of trying to access data that does not exist.

Overall, I designed the program to avoid repeating code, make the output
easy to read, and handle an expected API error without crashing.
"""


import requests

# Base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/pokemon/"

# List of Pokemon to fetch
pokemon_names = ["pikachu", "charizard", "bulbasaur"]

# Fetch and display information for each Pokemon

for pokemon in pokemon_names:
    try:
     response = requests.get(base_url + pokemon, timeout=5)  # Set a timeout to avoid hanging indefinitely
    except requests.exceptions.Timeout:
        print(f"The request for {pokemon} timed out. Please try again later.")
        continue

    if response.status_code == 200:
        data = response.json()

        # Extract Pokemon information
        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        # Extract the Pokemon's types
        types = [pokemon_type["type"]["name"] for pokemon_type in data["types"]]

        # Display Pokemon information
        print(f"\n--- {name.capitalize()} ---")
        print(f"Name: {name.capitalize()}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Types: {', '.join(types)}")

    else:
        print(f"Could not fetch {pokemon}. Status code: {response.status_code}")


# Test a Pokemon that does not exist
bad_pokemon = "pikacu"
response_404 = requests.get(base_url + bad_pokemon)

if response_404.status_code == 404:
    print(f"\nError: Pokemon '{bad_pokemon}' was not found.")
else:
    print(f"\nUnexpected status code: {response_404.status_code}")
