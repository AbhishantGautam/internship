from flask import Flask, render_template, request, url_for, redirect
import pickle

app = Flask('app')


@app.route("/")
def index():
  return render_template("index.html", name="abhishant")


@app.route("/greet", methods=['POST', 'GET'])
def greet():
  plays = request.form["plays"]
  playing = request.form["playing"]
  backlogs = request.form["backlogs"]
  wishlist = request.form["wishlist"]
  lists = request.form["lists"]
  reviews = request.form["reviews"]

  with open("https://cdn.glitch.me/7c26cd85-1038-4760-81fb-b378b739ed72/Finalmodel.pkl?v=1690310487236", "rb") as file1:
    random_forest = pickle.load(file1)
  arr = [[plays, playing, backlogs, wishlist, lists, reviews]]
  predict_rating = random_forest.predict(arr)

  return render_template("index.html", name=predict_rating)


if __name__ == '__main__':
    app.run(debug=True)
