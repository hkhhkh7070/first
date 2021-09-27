from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)
print(__name__)


def write2txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(
            f'\nemail:{email}   subject:{subject}   message:{message}')


def write2csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/works.html")
def works():
    return render_template('works.html')


@app.route("/work.html")
def work():
    return render_template('work.html')


def apps(html_name):
    @app.route("/"+html_name)
    def html_name():
        return render_template(html_name)

# for all pages


@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write2csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Error1'
    else:
        return 'Error2'
