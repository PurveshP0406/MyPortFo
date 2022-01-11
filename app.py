from flask import Flask, render_template, request , redirect 
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def writingtofile(data):
    with open('DataBase.txt' , mode='a') as Database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        myfile = Database.write(f'\n {email} , {subject} , {message} ')

def writingtocsv(data):
    with open('DataBase.csv' , mode='a') as Database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        mycsv = csv.writer(Database2, delimiter=',' , quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        mycsv.writerow([email, subject, message])

@app.route('/submitform', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
    # try:
        data=request.form.to_dict()
        # writingtofile(data)
        writingtocsv(data)
        return render_template('Thanks.html')
    # except: 'Not beeen able to save to the database'
    else:
        return 'something went wrong. Please Try again'
     
