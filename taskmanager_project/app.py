from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route to serve the main HTML file
@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

# Route to serve static files (CSS, JS, images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Example API route for demonstration
@app.route('/api/example', methods=['GET'])
def example():
    # You can add more complex logic here as needed
    return jsonify({"message": "This is an example endpoint"})

if __name__ == '__main__':
    app.run(debug=True)
