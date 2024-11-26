from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def gen_pass():
    password = " "
    symbols = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(8):
        password = password + random.choice(symbols) 

    return password 

orelreshka = ['Орел','Решка','Монета упала. Еще одна попытка.','Монета потерялась :(. Достаем новою..']

@app.route("/2")
def hello_world():
    return f'<p>{random.choice(orelreshka)}</p>'
    

app.run(debug=True)
