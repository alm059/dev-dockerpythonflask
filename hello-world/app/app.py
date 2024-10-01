from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    # Obtain dict for post method
    #data = request.get_json()

    # Write POST data to data.txt in app folder
    #with open('data.txt', 'a') as f:  # Open the file in append mode
    #    f.write(json.dumps(data) + '\n')  # Convert dict to JSON and write to file
    return "Flask development environment!"
  

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
