from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import pyrebase

# Firebase configuration
firebaseConfig = {
  'apiKey': "AIzaSyDStkMZjtHodu_Jh1MriFbC9Zwydxs5Ihw",
  'authDomain': "loginauth-7a6a9.firebaseapp.com",
  'databaseURL': "https://loginauth-7a6a9-default-rtdb.firebaseio.com",
  'projectId': "loginauth-7a6a9",
  'storageBucket': "loginauth-7a6a9.appspot.com",
  'messagingSenderId': "509749301064",
  'appId': "1:509749301064:web:5f70080e1ffea82ffbed7d",
  'measurementId': "G-XMEE1CYDDT"
};

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
CORS(app)

# Routes for rendering the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Ensure your HTML file is named index.html

# Login Route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    try:
        # Log in user
        login = auth.sign_in_with_email_and_password(email, password)
        return redirect("https://www.youtube.com")
    except Exception as e:
        return f"Error in login: {e}"

if __name__ == '__main__':
    app.run(debug=True)