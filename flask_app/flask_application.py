import random as rand
import string
import time

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main_page():
    return '''
    <html>
        <head>
            <title> Main page </title>
        </head>
        <body>
            <dev align = center>
                <br>
                <h1> Main page </h1>
                <hr width = 50%>
                <h2><a href = "/whoami"> Go to "Who am I" </a></h2>
                <h2><a href = "/source_code"> Go to "Source code" </a></h2>
                <h2>
                    <a href = "/random?length=42&specials=1&digits=0"> 
                        Go to "Random" 
                    </a>
                </h2>
                <hr width = 50%>
            </dev>
        </body>
    </html>
    '''


@app.route("/whoami")
def whoami():
    server_time = time.strftime('%H:%M:%S')
    user_browser = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    return f'''
    <html>
        <head>
            <title> Who am I </title>
        </head>
        <body>
            <dev align = center>
                <br>
                <h1 align = center> Who am I </h1>
                <hr width = 50%>
                <p> User browser: {user_browser} </p>
                <p> User IP address: {ip_address} </p>
                <p> Server time: {server_time} </p>
                <hr width = 50%>
                <h2><a href = "/"> Go to "Main page" </a></h2>
            </dev>
        </body>
    </html>
    '''


@app.route("/source_code")
def source_code():
    with open("flask_application.py", "r") as file:
        result = file.read()

    result = result.replace('<', '&lt')

    return f'''
    <html>
        <head>
            <title> Source code </title>
        </head>
        <body>
            <br>
            <h1 align = center> Source code </h1>
            <hr>
            {result}
            <hr>
            <h2 align = center><a href = "/"> Go to "Main page" </a></h2>
        </body>
     </html>
     '''


@app.route("/random")
def random():
    length = request.values.get('length', '')
    specials = request.values.get('specials', '')
    digits = request.values.get('digits', '')

    check_length = [str(i) for i in range(1, 101)]
    check_bool = ['', '0', '1']

    symbols = string.ascii_letters

    if specials == "1":
        symbols += '!"№;%:?*()_+.'

    if digits == "1":
        symbols += string.digits

    if not (length in check_length and specials in check_bool and digits in check_bool):
        answer = "Not valid request"
    else:
        answer = ''.join(rand.choice(symbols) for _ in range(int(length)))

    return f'''
    <head>
        <title> Source code </title>
    </head>
    <body>
        <dev align = center>
            <h1 align = center> Source code </h1>
            <hr width = 25%>
            <br>
            <form action = "/random">
                Length input: <input name = "length">
                <br>
                <br>
                Specials input: <input name = "specials">
                <br>
                <br>
                Digits input: <input name = "digits">
                <br>
                <br>
                <input type = "submit">
                <br>
                <br>
                Random symbols: {answer}
            </form>
            <hr width = 25%>
            <h2 align = center><a href = "/"> Go to "Main page" </a></h2>
        </dev>
    </body>
     '''


if __name__ == '__main__':
    app.run(debug=True)
