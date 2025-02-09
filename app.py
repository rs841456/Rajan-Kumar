from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # To handle CORS issues

# Replace with your Gemini API key
API_KEY = 'AIzaSyDNRX7pThdmg8w_2oJxcnyR35r7HwJbxj0'

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the request
        data = request.json
        user_input = data.get('message')

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # Send the user's message to the Gemini API
        response = model.generate_content(user_input)

        # Return the bot's response
        return jsonify({
            "message": response.text
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)