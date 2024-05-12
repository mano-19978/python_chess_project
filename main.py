


# Function to calculate valid moves for the Knight
from flask import request, jsonify, Flask, app
app = Flask(__name__)

def calculate_knight_moves(position):
    # Knight moves relative to its position
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    column = ord(position[0].upper()) - ord('A')
    row = int(position[1])

    valid_moves = []

    for move in moves:
        new_column = column + move[0]
        new_row = row + move[1]

        if 1 <= new_column <= 8 and 1 <= new_row <= 8:
            valid_moves.append(chr(new_column + ord('A') - 1) + str(new_row))

    return valid_moves


@app.route('/chess/<slug>'
           '', methods=['POST'])
def get_valid_moves(slug):
    positions = request.json.get('positions')

    if not positions:
        return jsonify({'error': 'Positions not provided'}), 400

    if slug.lower() == 'knight':
        knight_position = positions.get('Knight')

        if not knight_position:
            return jsonify({'error': 'Knight position not provided'}), 400

        valid_moves = calculate_knight_moves(knight_position)
        return jsonify({'valid_moves': valid_moves}), 200
    else:
        return jsonify({'error': 'Invalid slug'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
