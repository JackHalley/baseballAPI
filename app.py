from flask import Flask, jsonify, request
from models import fetch_player_stats

app = Flask(__name__)


@app.route('/player-stats', methods=['GET'])
def get_player_stats_endpoint():
    last_name = request.args.get('last_name')
    first_name = request.args.get('first_name')
    start_date = request.args.get('start_date', '2022-04-01')
    end_date = request.args.get('end_date', '2022-09-30')

    data = fetch_player_stats(last_name, first_name, start_date, end_date)

    if not data:
        return jsonify({'error': 'Data not found or error occurred'}), 404

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
