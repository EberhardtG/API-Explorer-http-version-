# Pokémon API Explorer

A Python project that uses the **PokéAPI** and the `requests` library to retrieve and display information about Pokémon. The project demonstrates how to work with REST APIs, JSON responses, HTTP status codes, and basic error handling.

## Features

- Fetches data from the PokéAPI using HTTP GET requests
- Retrieves information for three Pokémon:
  - Pikachu
  - Charizard
  - Bulbasaur
- Displays each Pokémon's:
  - Name
  - Height
  - Weight
  - Types
- Handles multiple Pokémon types
- Detects and handles a `404 Not Found` response
- Includes basic network error handling and request timeouts

## Technologies

- Python
- Requests
- REST APIs
- JSON
- HTTP status codes

## How It Works

The program stores the PokéAPI endpoint in a base URL and uses a list of Pokémon names to avoid repeating the same request logic.

For each Pokémon, the program:

1. Sends a GET request to the PokéAPI.
2. Checks the HTTP status code.
3. Converts a successful JSON response into a Python dictionary.
4. Extracts the Pokémon's name, height, weight, and types.
5. Displays the information in a clean format.

The program also attempts to retrieve an invalid Pokémon name (`pikacu`) to demonstrate how a `404` response can be handled without crashing the program.

## Example Output

```text
--- Pikachu ---
Name: Pikachu
Height: 4
Weight: 60
Types: electric

--- Charizard ---
Name: Charizard
Height: 17
Weight: 905
Types: fire, flying

--- Bulbasaur ---
Name: Bulbasaur
Height: 7
Weight: 69
Types: grass, poison

Error: Pokemon 'pikacu' was not found.
```

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd <project-directory>
```

### 3. Install the required dependency

```bash
pip install requests
```

### 4. Run the program

```bash
python api_explorer.py
```

## What I Practiced

This project provided hands-on practice with:

- Making API requests with Python
- Working with REST API endpoints
- Parsing JSON responses
- Accessing nested dictionaries and lists
- Using list comprehensions
- Working with HTTP status codes
- Handling API errors
- Using loops to reduce repetitive code
- Structuring API data into readable output

## API

This project uses the [PokéAPI](https://pokeapi.co/), a free RESTful API providing Pokémon-related data.
