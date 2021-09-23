import pymongo
from flask import Flask, render_template
from scrape_mars import scrape

app = Flask(__name__)

# App route to scrape
@app.route("/scrape")
def store:
    mars_data = scrape

    # Set up MongoDB to store data
    mongo = pymongo.MongoClient('mongodb://localhost:27017')
    db = mongo.mars_db
    mars = db.mars

    # Store data
    mars.insert_one(mars_data)

    return redirect("/", code=302)

@app.route("/")
def main:
    # Connect to db
    # Set up MongoDB to store data
    mongo = pymongo.MongoClient('mongodb://localhost:27017')
    db = mongo.mars_db
    mars = db.mars

    # Read data
    mars_data = list(mars.find)[0]

    return render_template('mars.html', parameters=['data'=mars_data])

if __name__ == "__main__":
    app.run(debug=True)