from flask import Flask
from flask import render_template

app = Flask(__name__)

bd = {
    "clothes": [
        {"name": "clothes", "img": "images/shirt1.jpg", "desc": "This is a clothes", "price": 4100},
        {"name": "clothes", "img": "images/shirt2.jpg", "desc": "This is a clothes", "price": 2200},
        {"name": "clothes", "img": "images/shirt3.jpg", "desc": "This is a clothes", "price": 3600},
        {"name": "clothes", "img": "images/shirt4.jpg", "desc": "This is a clothes", "price": 5300},
    ],
    "shoes": [
        {"name": "shoes", "img": "images/shoes1.jpg", "desc": "This is shoes", "price": 4100},
        {"name": "shoes", "img": "images/shoes2.jpg", "desc": "This is shoes", "price": 6700},
    ],
    "jackets": [
        {"name": "jacket", "img": "images/jacket1.jpg", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "images/jacket2.jpg", "desc": "This is a jacket", "price": 6600},
        {"name": "jacket", "img": "images/jacket3.jpg", "desc": "This is a jacket", "price": 8700},
    ],
}

@app.route("/")
def index():
    content = {
        "home": "active",
    }
    return render_template("index.html", content=content)


@app.route("/clothes/")
def clothes():
    content = {
        "clothes": "active",
        "items": bd["clothes"]
    }
    return render_template("clothes.html", content=content)


@app.route("/shoes/")
def shoes():
    content = {
        "shoes": "active",
        "items": bd["shoes"]
    }
    return render_template("shoes.html", content=content)


@app.route("/jackets/")
def jackets():
    content = {
        "jackets": "active",
        "items": bd["jackets"]
    }
    return render_template("jackets.html", content=content)


if __name__ == '__main__':
    app.run(debug=True)