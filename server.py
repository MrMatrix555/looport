from flask import Flask, render_template, url_for, request, redirect
#from werkzeug.utils import redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello_World():
    # print(url_for('static', filename='sun.ico'))
    return render_template('index.html')


@app.route('/<string:page_name>')
def Blog(page_name):
    return render_template(page_name)


def write_data(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def csv_write_data(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar=':', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit', methods=['POST', 'GET'])
def sumbit():
    if request.method == 'POST':
        data = request.form.to_dict()
        csv_write_data(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went Wrong, Try again!!'
