from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/getkey', methods=['GET'])
def get_key():
    hwid_link = request.args.get('hwid_link')
    if not hwid_link:
        return jsonify({'error': 'Missing hwid_link parameter'}), 400
    
    external_api_url = f'https://vacation-free.vercel.app/get_key?link={hwid_link}'
    
    try:
        response = requests.get(external_api_url)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except ValueError:
        return jsonify({'error': 'Failed to parse response'}), 500

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)