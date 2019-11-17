from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

scraped_yet = False

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_Data"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    Mars_Info = mongo.db.Mars_Info.find_one()
    return render_template("index.html", Mars_Info=Mars_Info)
    
    


@app.route("/scrape")
def scraper():    
    Mars_Info = mongo.db.Mars_Info
    Information = scrape_mars.scrape()
    Mars_Info.update({}, Information, upsert=True)
    scraped_yet = True
    return redirect("/", code=302)
    


if __name__ == "__main__":
    app.run(debug=True)