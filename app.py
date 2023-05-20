from flask import Flask, render_template ,request
from flask_pymongo import PyMongo
# from flask_mongoengine import MongoEngine
# from flask import jsonify
# flask app object
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


# connection parameters with uri
# app.config['MONGODB_SETTINGS'] = {
#     'host':'mongodb://localhost/mylib'
# }

# app.config['MONGODB_SETTINGS'] = {
#     "db":"mylib",
#     "host":"localhost",
#     "port":"27017"
# }

# Mongoengine object
# db = ""
# # db = MongoEngine()
# db.init_app(app)
# # db = MongoEngine(app)

# class create(str):
#     data=mongo.db.inventory.insert_one({
#     "name"=str.Name,
#     "Author" = str,
#     "Type" = str})
    
    


# @app.route('/movies')
# def  get_movies():
#     movies = Movie.objects()
#     return  jsonify(movies), 200


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        Name=request.form["name"]
        Author=request.form["author"]
        Type=request.form["check"]
        print(Name, Author, Type)
        mongo.db.inventory.insert_one({
        "name":Name,
        "author":Author,
        "type": Type
        })
    # data= mongo.db.inventory.find({})
    data= mongo.db.inventory.find()
    print(data) # this prints data is in cursor object, see here in terminal
    for item in data:
        # print(item) # this prints all data present in database 
        wdata=item
        # ** don't aspect sets will give data in orderwise. that's why storing all data in below form
        
        ndata={wdata["name"]} # storing all name values in ndata
        adata={wdata["author"]}
        tdata={wdata["type"]}
        # print(item["name"])
        alldata=ndata, adata, tdata
        # print(ndata,"end ndata", adata, "end adata", tdata, "end tdata")
        # print(alldata)
          
    mdata=alldata
    print(mdata)
        
    # return render_template("index.html", movie=hdata)

    return render_template("index.html", movie=mdata)

# for testing purpose
@app.route('/test', methods=['GET','POST'])
def test():
        # body = request.POST_json()
   if request.method=="POST":
        Name=request.form["name"]
        Author=request.form["author"]
        Type=request.form["check"]
        print(Name, Author, Type)

        # return Name, Author, Type
        # return body


# inserting in database practice
@app.route('/2')
def prac():
    mongo.db.inventory.insert_one({"a":1})
    return 'Hello, World!'

if __name__=="__main__":
    app.run(debug=True)