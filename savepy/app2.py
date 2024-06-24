# # # from flask import Flask, request, jsonify
# # # from pymongo import MongoClient
# # # import smtplib
# # # from email.mime.multipart import MIMEMultipart
# # # from email.mime.text import MIMEText
# # # import csv

# # # app2 = Flask(__name__)

# # # # MongoDB connection setup
# # # mongo_client = MongoClient('mongodb+srv://ilaraecodes:Prayalways1986!@emaillist.tpnge6l.mongodb.net/')
# # # db = mongo_client['EmailList']
# # # collection = db['contacts']

# # # # Gmail credentials and SMTP settings
# # # gmail_user = 'ilaraecodes@gmail.com'
# # # gmail_password = 'cjyr hofv smwa ajaz'
# # # smtp_server = 'smtp.gmail.com'
# # # smtp_port = 587

# # # def get_html_template(template_name, subject, body):
# # #     if template_name == "Template 1":
# # #         return f"""\
# # #         <html>
# # #         <head>
# # #           <style>
# # #             .container {{
# # #               font-family: Arial, sans-serif;
# # #               max-width: 600px;
# # #               margin: auto;
# # #               padding: 20px;
# # #               border: 1px solid #ddd;
# # #               border-radius: 8px;
# # #               background-color: #f9f9f9;
# # #             }}
# # #             .content {{
# # #               text-align: center;
# # #               padding: 20px;
# # #             }}
# # #             .button {{
# # #               display: inline-block;
# # #               padding: 10px 20px;
# # #               font-size: 16px;
# # #               color: white;
# # #               background-color: #34d399;
# # #               border-radius: 5px;
# # #               text-decoration: none;
# # #             }}
# # #             .button:hover {{
# # #               background-color: #3b82f6;
# # #             }}
# # #           </style>
# # #         </head>
# # #         <body>
# # #           <div class="container">
# # #             <div class="content">
# # #               <h1>{subject}</h1>
# # #               <p>{body}</p>
# # #               <a href="https://soundgui.com" class="button">Get Started</a>
# # #             </div>
# # #           </div>
# # #         </body>
# # #         </html>
# # #         """

# # # @app2.route('/preview', methods=['POST'])
# # # def preview_email():
# # #     data = request.get_json()
# # #     subject = data['subject']
# # #     body = data['body']
# # #     template_name = data['template']

# # #     html_content = get_html_template(template_name, subject, body)
# # #     return jsonify({"preview": html_content}), 200

# # # @app2.route('/sendemails', methods=['POST'])
# # # def send_emails():
# # #     data = request.get_json()
# # #     subject = data['subject']
# # #     body = data['body']
# # #     template_name = data['template']

# # #     with open('email-csv.csv', 'r') as csvfile:
# # #         email_reader = csv.reader(csvfile, delimiter=',')
# # #         for row in email_reader:
# # #             recipient_email = row[0]
# # #             message = MIMEMultipart()
# # #             message['From'] = gmail_user
# # #             message['To'] = recipient_email
# # #             message['Subject'] = subject

# # #             tracking_id = recipient_email.replace('@', '_').replace('.', '_')
# # #             tracking_url = f"http://yourserver.com/track?email_id={tracking_id}"
# # #             html_body = get_html_template(template_name, subject, body) + f'<img src="{tracking_url}" width="1" height="1" alt="">'

# # #             message.attach(MIMEText(html_body, 'html'))

# # #             with smtplib.SMTP(smtp_server, smtp_port) as server:
# # #                 server.starttls()
# # #                 server.login(gmail_user, gmail_password)
# # #                 server.sendmail(gmail_user, recipient_email, message.as_string())
# # #                 print(f'Email sent to {recipient_email}')

# # #     return jsonify({"status": "success"}), 200

# # # if __name__ == '__main__':
# # #     app2.run(debug=True)



# # from flask import Flask, render_template, request, redirect, jsonify
# # from pymongo import MongoClient
# # import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # import csv

# # app = Flask(__name__)




# # # Connect to your MongoDB Database
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['user_database']
# # users_collection = db['users']

# # # Gmail credentials and SMTP settings
# # gmail_user = 'ilaraecodes@gmail.com'
# # gmail_password = 'cjyr hofv smwa ajaz'
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 587

# # @app.route('/', methods=['GET', 'POST'])
# # def user_form():
# #     if request.method == 'POST':
# #         user_data = {
# #             'name': request.form.get('name'),
# #             'email': request.form.get('email')
# #         }
# #         users_collection.insert_one(user_data)
# #         send_email(user_data['email'], user_data['name'])
# #         return redirect('/success')
# #     return render_template('form.html')

# # def send_email(recipient_email, name):
# #     html = render_template('email_template.html', name=name)
# #     msg.attach(MIMEText(html, 'html'))
# #     sender_email = gmail_user
# #     password = gmail_password
    
# #     msg = MIMEMultipart('alternative')
# #     msg['Subject'] = "Welcome to Our Service!"
# #     msg['From'] = sender_email
# #     msg['To'] = recipient_email

# #     html = render_template('email_template.html', name=name)
# #     msg.attach(MIMEText(html, 'html'))

# #     with smtplib.SMTP(smtp_server, smtp_port) as server:
# #         server.starttls()
# #         server.login(sender_email, password)
# #         server.sendmail(sender_email, recipient_email, msg.as_string())

# # @app.route('/sendemails', methods=['POST'])
# # def send_emails():
# #     data = request.get_json()
# #     subject = data['subject']
# #     body = data['body']
# #     template_name = data['template']

# #     with open('email-csv.csv', 'r') as csvfile:
# #         email_reader = csv.reader(csvfile, delimiter=',')
# #         for row in email_reader:
# #             recipient_email = row[0]
# #             message = MIMEMultipart()
# #             message['From'] = gmail_user
# #             message['To'] = recipient_email
# #             message['Subject'] = subject

# #             # Convert the template into an HTML email
# #             html = render_template('email_template.html', name=recipient_email.split('@')[0])
# #             message.attach(MIMEText(html, 'html'))

# #             with smtplib.SMTP(smtp_server, smtp_port) as server:
# #                 server.starttls()
# #                 server.login(gmail_user, gmail_password)
# #                 server.sendmail(gmail_user, recipient_email, message.as_string())
# #                 print(f'Email sent to {recipient_email}')

# #     return jsonify({"status": "success"}), 200

# # @app.route('/success')
# # def success():
# #     return "Information successfully saved!"

# # if __name__ == '__main__':
# #     app.run(debug=True)


# # from flask import Flask, request, redirect, jsonify
# # from pymongo import MongoClient
# # import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # import csv

# # app = Flask(__name__)

# # # MongoDB connection setup
# # mongo_client = MongoClient('mongodb+srv://ilaraecodes:Prayalways1986!@emaillist.tpnge6l.mongodb.net/')
# # db = mongo_client['EmailList']
# # collection = db['contacts']

# # # Gmail credentials and SMTP settings
# # gmail_user = 'ilaraecodes@gmail.com'
# # gmail_password = 'cjyr hofv smwa ajaz'
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 587

# # @app.route('/', methods=['GET', 'POST'])
# # def user_form():
# #     if request.method == 'POST':
# #         user_data = {
# #             'first_name': request.form.get('first_name'),
# #             'last_name': request.form.get('last_name'),
# #             'email': request.form.get('email')
# #         }
# #         collection.insert_one(user_data)
# #         send_email(user_data['email'], user_data['first_name'], user_data['last_name'])
# #         return redirect('/success')
# #     return '''
# #         <form method="post">
# #             First Name: <input type="text" name="first_name"><br>
# #             Last Name: <input type="text" name="last_name"><br>
# #             Email: <input type="email" name="email"><br>
# #             <input type="submit" value="Submit">
# #         </form>
# #     '''

# # def send_email(recipient_email, first_name, last_name):
# #     sender_email = gmail_user
# #     password = gmail_password
# #     msg = MIMEMultipart('alternative')
# #     msg['Subject'] = "Welcome to Our Service!"
# #     msg['From'] = sender_email
# #     msg['To'] = recipient_email
# #     html = f"""
# #         <html>
# #         <body>
# #             <h1>Welcome, {first_name} {last_name}!</h1>
# #             <p>Thank you for registering with us at {recipient_email}. We're excited to have you on board!</p>
# #             <p>Visit our website by clicking <a href="https://yourwebsite.com">here</a>.</p>
# #         </body>
# #         </html>
# #     """
# #     msg.attach(MIMEText(html, 'html'))
# #     with smtplib.SMTP(smtp_server, smtp_port) as server:
# #         server.starttls()
# #         server.login(sender_email, password)
# #         server.sendmail(sender_email, recipient_email, msg.as_string())

# # @app.route('/sendemails', methods=['POST'])
# # def send_emails():
# #     data = request.get_json()
# #     subject = data['subject']
# #     body = data['body']
# #     with open('email-csv.csv', 'r') as csvfile:
# #         email_reader = csv.reader(csvfile, delimiter=',')
# #         for row in email_reader:
# #             recipient_email = row[0]
# #             message = MIMEMultipart()
# #             message['From'] = gmail_user
# #             message['To'] = recipient_email
# #             message['Subject'] = subject
# #             # Splitting to assume first and last name are separated by a space in the CSV
# #             first_name, last_name = recipient_email.split('@')[0].split('.')[:2]
# #             html = f"""
# #                 <html>
# #                 <body>
# #                     <h1>Dear {first_name} {last_name},</h1>
# #                     <p>{body}</p>
# #                 </body>
# #                 </html>
# #             """
# #             message.attach(MIMEText(html, 'html'))
# #             with smtplib.SMTP(smtp_server, smtp_port) as server:
# #                 server.starttls()
# #                 server.login(gmail_user, gmail_password)
# #                 server.sendmail(gmail_user, recipient_email, message.as_string())
# #                 print(f'Email sent to {recipient_email}')
# #     return jsonify({"status": "success"}), 200

# # @app.route('/success')
# # def success():
# #     return "Information successfully saved!"

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # from flask import Flask, request, redirect, jsonify
# # from pymongo import MongoClient
# # import smtplib
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # import csv

# # app = Flask(__name__)

# # # MongoDB connection setup
# # mongo_client = MongoClient('mongodb+srv://ilaraecodes:Prayalways1986!@emaillist.tpnge6l.mongodb.net/')
# # db = mongo_client['EmailList']
# # collection = db['contacts']

# # # Gmail credentials and SMTP settings
# # gmail_user = 'ilaraecodes@gmail.com'
# # gmail_password = 'cjyr hofv smwa ajaz'
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 587

# # @app.route('/', methods=['GET', 'POST'])
# # def user_form():
# #     if request.method == 'POST':
# #         user_data = {
# #             'first_name': request.form.get('first_name'),
# #             'last_name': request.form.get('last_name'),
# #             'email': request.form.get('email')
# #         }
# #         collection.insert_one(user_data)
# #         send_email(user_data['email'])
# #         return redirect('/success')
# #     return '''
# #         <form method="post">
# #             First Name: <input type="text" name="first_name"><br>
# #             Last Name: <input type="text" name="last_name"><br>
# #             Email: <input type="email" name="email"><br>
# #             <input type="submit" value="Submit">
# #         </form>
# #     '''

# # def send_email(recipient_email):
# #     sender_email = gmail_user
# #     password = gmail_password
# #     msg = MIMEMultipart('alternative')
# #     msg['Subject'] = "Welcome to Our Service!"
# #     msg['From'] = sender_email
# #     msg['To'] = recipient_email
# #     html = f"""
# #         <html>
# #         <body>
# #             <h1>Welcome to Our Service!</h1>
# #             <p>Thank you for registering with us. We're excited to have you on board!</p>
# #             <p>Visit our website by clicking <a href="https://yourwebsite.com">here</a>.</p>
# #         </body>
# #         </html>
# #     """
# #     msg.attach(MIMEText(html, 'html'))
# #     with smtplib.SMTP(smtp_server, smtp_port) as server:
# #         server.starttls()
# #         server.login(sender_email, password)
# #         server.sendmail(sender_email, recipient_email, msg.as_string())

# # @app.route('/sendemails', methods=['POST'])
# # def send_emails():
# #     with open('email-csv.csv', 'r') as csvfile:
# #         email_reader = csv.reader(csvfile)
# #         next(email_reader)  # Skip the header row if present
# #         for row in email_reader:
# #             recipient_email = row[2]  # Assuming the email is in the third column
# #             send_email(recipient_email)
# #     return jsonify({"status": "success"}), 200

# # @app.route('/success')
# # def success():
# #     return "Information successfully saved!"

# # if __name__ == '__main__':
# #     app.run(debug=True)



# from flask import Flask, jsonify
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import csv

# app = Flask(__name__)

# # Gmail credentials and SMTP settings
# gmail_user = 'ilaraecodes@gmail.com'
# gmail_password = 'cjyr hofv smwa ajaz'
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587

# def send_email(recipient_email):
#     """Send an email to the specified recipient."""
#     sender_email = gmail_user
#     password = gmail_password
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = "Welcome to Our Service!"
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     html = f"""
#         <html>
#         <body>
#             <h1>Welcome to Our Service!</h1>
#             <p>Thank you for joining us. We're excited to have you on board!</p>
#             <img src="https://yourdomain.com/image.jpg" alt="Welcome Image">
#             <p>Please complete the form below to complete your registration:</p>
#             <form action="https://yourflaskappdomain.com/register" method="post">
#                 First Name: <input type="text" name="first_name"><br>
#                 Last Name: <input type="text" name="last_name"><br>
#                 Email: <input type="email" name="email" value="{recipient_email}"><br>
#                 <button type="submit">Submit</button>
#             </form>
#             <p>Visit our website by clicking <a href="https://yourwebsite.com">here</a>.</p>
#         </body>
#         </html>
#     """
#     msg.attach(MIMEText(html, 'html'))
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.sendmail(sender_email, recipient_email, msg.as_string())


# # def send_email(recipient_email):
# #     """Send an email to the specified recipient."""
# #     sender_email = gmail_user
# #     password = gmail_password
# #     msg = MIMEMultipart('alternative')
# #     msg['Subject'] = "Welcome to Our Service!"
# #     msg['From'] = sender_email
# #     msg['To'] = recipient_email
# #     html = """
# #         <html>
# #         <body>
# #             <h1>Welcome to Our Service!</h1>
# #             <p>Thank you for joining us. We're excited to have you on board!</p>
# #             <p>Visit our website by clicking <a href="https://yourwebsite.com">here</a>.</p>
# #         </body>
# #         </html>
# #     """
# #     msg.attach(MIMEText(html, 'html'))
# #     with smtplib.SMTP(smtp_server, smtp_port) as server:
# #         server.starttls()
# #         server.login(sender_email, password)
# #         server.sendmail(sender_email, recipient_email, msg.as_string())
# #         print(f'Email sent to {recipient_email}')

# @app.route('/sendemails', methods=['GET'])
# def send_emails_from_csv():
#     """Read email addresses from a CSV file and send emails to each."""
#     with open('email-csv.csv', 'r') as csvfile:
#         email_reader = csv.reader(csvfile)
#         next(email_reader)  # Skip the header row if present
#         for row in email_reader:
#             recipient_email = row[0]  # Adjust the index as per your CSV column for email addresses
#             send_email(recipient_email)
#     return jsonify({"status": "success"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)
