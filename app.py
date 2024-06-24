
from flask import Flask, request, redirect, jsonify, render_template_string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import csv

app = Flask(__name__)

# Gmail credentials and SMTP settings
gmail_user = 'ilaraecodes@gmail.com'
gmail_password = 'cjyr hofv smwa ajaz'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# MongoDB connection setup
mongo_client = MongoClient('mongodb+srv://ilaraecodes:Prayalways1986!@emaillist.tpnge6l.mongodb.net/')
db = mongo_client['EmailList']
collection = db['contacts']

def send_email(recipient_email):
    """Send an email to the specified recipient with HTML styling and a signup link."""
    sender_email = gmail_user
    password = gmail_password
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Join Our Community!"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # HTML Content with a signup 
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Join Our Community</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            .container {
                width: 100%;
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            .container img {
                width: 100%;
                border-radius: 8px 8px 0 0;
            }
            .content {
                padding: 20px;
            }
            .content h2 {
                font-size: 24px;
                margin-bottom: 16px;
            }
            .content p {
                font-size: 16px;
                margin-bottom: 24px;
            }
            .btn {
                background-color: #007bff;
                border: none;
                border-radius: 4px;
                color: #ffffff;
                padding: 10px 20px;
                text-decoration: none;
                font-size: 16px;
                display: inline-block;
                margin-top: 10px;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://foothillranchliving.com/assets/foothill-C4Za23dy.png" alt="Community">
            <div class="content">
                <h2>Join Our Community!</h2>
                <p>We are excited to have you join our community. Click the link below to sign up:</p>
                <a href="http://localhost:5000/" class="btn">Sign Up Here</a>
            </div>
        </div>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f'Email sent to {recipient_email}')
    
        
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up Form</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/daisyui@2.0.3/dist/full.css" rel="stylesheet">
</head>
<body>
    <div class="mx-auto my-10 shadow-xl card bg-base-100 w-96">
        <figure class="px-10 pt-10">
            <img src="/static/FoothillOG.png" alt="Community" class="rounded-xl">
        </figure>
        <div class="card-body">
            <h2 class="card-title">Sign Up for Our List</h2>
            <form id="signupForm">
                <div class="mb-4">
                    <label for="firstName" class="block text-sm font-medium text-gray-700">First Name:</label>
                    <input type="text" id="firstName" name="firstName" class="w-full input input-bordered" required>
                </div>
                <div class="mb-4">
                    <label for="lastName" class="block text-sm font-medium text-gray-700">Last Name:</label>
                    <input type="text" id="lastName" name="lastName" class="w-full input input-bordered" required>
                </div>
                <div class="mb-4">
                    <label for="email" class="block text-sm font-medium text-gray-700">Email:</label>
                    <input type="email" id="email" name="email" class="w-full input input-bordered" required>
                </div>
                <div class="justify-end card-actions">
                    <button type="submit" class="btn btn-primary">Sign Up</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('signupForm').addEventListener('submit', async function(event) {
                event.preventDefault();

                const formData = {
                    firstName: document.getElementById('firstName').value,
                    lastName: document.getElementById('lastName').value,
                    email: document.getElementById('email').value
                };

                const response = await fetch('/api/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    alert('Thank you for signing up!');
                } else {
                    alert('There was an error. Please try again.');
                }
            });
        });
    </script>
</body>
</html>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.getElementById('signupForm').addEventListener('submit', async function(event) {
                    event.preventDefault();

                    const formData = {
                        firstName: document.getElementById('firstName').value,
                        lastName: document.getElementById('lastName').value,
                        email: document.getElementById('email').value
                    };

                    const response = await fetch('/api/signup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    });

                    if (response.ok) {
                        alert('Thank you for signing up!');
                    } else {
                        alert('There was an error. Please try again.');
                    }
                });
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

 

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return jsonify({"error": "Missing data"}), 400

    collection.insert_one({
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    })

    return jsonify({"message": "Data saved successfully"}), 200

@app.route('/sendemails', methods=['GET'])
def send_emails_from_csv():
    """Read email addresses from a CSV file and send emails with a signup link to each."""
    with open('email-csv.csv', 'r') as csvfile:
        email_reader = csv.reader(csvfile)
        next(email_reader)  # Skip the header row if present
        for row in email_reader:
            if row:  # Ensure the row isn't empty
                recipient_email = row[0]  # Adjust as per your CSV column for email addresses
                send_email(recipient_email)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
