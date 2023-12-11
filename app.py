from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your existing API endpoint
BASE_API_URL = "https://app.ylytic.com/ylytic/test"

@app.route('/search', methods=['GET'])
def search_comments():
    # Extract search parameters from the query string
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Construct the search URL
    search_params = {
        'author': search_author,
        'at_from': at_from,
        'at_to': at_to,
        'like_from': like_from,
        'like_to': like_to,
        'reply_from': reply_from,
        'reply_to': reply_to,
        'text': search_text
    }

    # Make a request to the actual YouTube comments API
    response = requests.get(BASE_API_URL, params=search_params)

    # Check if the request to the existing API was successful
    if response.status_code == 200:
        # Parse the JSON response
        comments = response.json()
        return jsonify(comments)
    else:
        # Return an error if the request to the existing API fails
        return jsonify({'error': f'Failed to fetch comments. Status code: {response.status_code}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
