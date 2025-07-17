``` markdown
```
# AlgoritmAPI

A FastAPI-based REST API that provides various algorithmic functionalities including Fibonacci number calculation and poker hand evaluation.

## Features

### Fibonacci Numbers (`/fibonacci/{n}`)
- GET endpoint that returns the nth number in the Fibonacci sequence
- Supports numbers from 0 to 1000
- Returns both the input number and its corresponding Fibonacci value
- Implements memoization for efficient calculation

### Poker Hand Evaluator (`/poker/`)
- POST endpoint that evaluates multiple poker hands and determines the winner(s)
- Supports standard poker hand rankings:
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pair
  - One Pair
  - High Card
- Handles ties correctly by comparing card ranks
- Returns the winning hand(s)

## Installation

1. Create a virtual environment:
```
bash python3 -m venv venv source venv/bin/activate # On Windows use: venv\Scripts\activate
``` 

2. Install dependencies:
```
bash pip install fastapi uvicorn
``` 

## Running the API

Start the server with:
```
bash uvicorn main:app --reload
``` 

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### GET /fibonacci/{n}
Returns the nth Fibonacci number.

Example request:
```
bash curl [http://localhost:8000/fibonacci/10](http://localhost:8000/fibonacci/10)
``` 

Example response:
```
json { "n": 10, "fibonacci": 55 }
``` 

### POST /poker/
Evaluates poker hands and returns the winner(s).

Example request:
```
bash curl -X POST [http://localhost:8000/poker/](http://localhost:8000/poker/)
-H "Content-Type: application/json"
-d '{"hands": ["2H 3H 4H 5H 6H", "KS AS TS QS JS"]}'
``` 

Example response:
```
json { "best hand": ["KS AS TS QS JS"] }
``` 

## Input Format

### Poker Hands
- Each card is represented by two characters:
  - First character: Rank (2-9, T, J, Q, K, A)
  - Second character: Suit (H, D, C, S)
- Each hand consists of exactly 5 cards separated by spaces
- Example: "2H 3H 4H 5H 6H" represents a straight flush in hearts

## Error Handling

- Fibonacci endpoint returns 400 for negative numbers or numbers > 1000
- Invalid input formats will return appropriate error messages

## Project Structure
```
AlgoritmAPI/ ├── fibonacci/ │ └── fibonacci.py ├── poker/ │ ├── card.py │ ├── hand.py │ ├── hand_type.py │ └── poker.py ├── tests/ │ ├── test_fibonacci.py │ └── test_poker.py └── main.py
``` 

## Testing

Run the tests with:
```
bash python -m pytest
``` 

## License

[Add your chosen license here]
```
