from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def handle_input():
    data = request.json
    # Process the input data here
    user_message = data.get("message", "")
    # For demonstration, echo back the message with a prefix
    response_message = f"Echo: {user_message}"
    response = {"message": response_message}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
