from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate", methods=["POST"])  # ✅ API endpoint for generating trivia questions
def generate_question():
    data = request.get_json()  # Get JSON data from the request
    topic = data.get("topic", "general")  # Extract topic or default to "general"

    # Example trivia question generation logic
    question = f"What is a famous fact about {topic}?"

    return jsonify({"question": question})  # Return the question as JSON response

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode

