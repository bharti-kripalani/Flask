# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the homepage
# Testing http://127.0.0.1:8080/
@app.route("/")
def home():
    # This function runs when the user visits '/'
    return "Welcome to the homepage!"

# Define the route for the about page
# Testing http://127.0.0.1:8080/about
@app.route("/about")
def about():
    # This function runs when the user visits '/about'
    return "This is the about page."

# Define a route with a variable part for user profiles
# Testing http://127.0.0.1:8080/user/helloworld
@app.route("/user/<username>")
def user_profile(username):
    # This function runs when the user visits '/user/<username>'
    # The value in <username> is passed as an argument
    return f"Hello, {username}! This is your profile."

# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True, port=8080)
