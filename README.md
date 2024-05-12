# Chess Moves API Documentation  :-
## Overview
This documentation offers insights into the Chess Moves API, a tool designed to compute the permissible moves for a chess piece on a chessboard.

## API Endpoint
The API endpoint designated for computing chess piece moves for a knight is `/chess/knight`.

## Request
The API entertains POST requests alongside JSON payload. The payload must entail the positions of the chess pieces.

### Endpoint
POST /chess/knight
Content-Type: application/json

```json
{
    "positions": {
        "Knight": "D4"
    }
}


### Request Body
```json
{
    "positions": {
        "Knight": "position"
    }
}
```


**position**: The location of the knight piece on the chessboard, defined as a string incorporating the column letter (A-H) followed by the row number (1-8). For instance, "A1", "B3", etc.

## Response
The API furnishes JSON responses containing the valid moves for the knight piece.

### Success Response
HTTP/1.1 200 OK
Content-Type: application/json

```json
{
    "valid_moves": ["B3", "B5", "C2", "C6", "E2", "E6", "F3", "F5"]
}
```


## Implementation Details
The API is built utilizing Flask, a micro web framework for Python.

### Function to Calculate Valid Moves for the Knight
The `calculate_knight_moves()` function computes valid moves for the knight grounded on its current position on the chessboard.

### Flask Route
The `/chess/knight` route manages POST requests and computes valid moves for the knight relying on the provided position.

## Dockerization of the Application
**This Dockerfile is employed to construct a Docker image for a Python application. **

```Dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN echo "Current Working Directory: $(pwd)"
CMD ["python", "main.py"]
In summary, this Dockerfile establishes a Docker image integrating Python 3.10, installs dependencies specified in `requirements.txt`, 
replicates the application code into the container, and defines the default command to execute the Python application.

## Running the Project
1. Set up the python   interpreter.
2. Install requirements from the requirement file.
3. Execute the project in the IDE.
4. Following that, in the terminal, execute this command to create an image in Docker. Ensure Docker is downloaded and installed on your system.
```bash
docker build -t python-chess-project  .
```

5. Then, run the Docker image by executing this command.
```bash
docker run python-chess-project
```

