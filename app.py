from flask import * #importing flask (Install it using python -m pip install flask)


app = Flask(__name__) #initialising flask


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")
def home():
    return render_template("home.html") #rendering our home.html contained within /templates

@app.route("/account", methods=["POST", "GET"]) #defining the routes for the account() funtion
def account():
    usr = "<User Not Defined>" #Creating a variable usr
    yearofbirth = "<Dawn of Time>"
    if (request.method == "POST"): #Checking if the method of request was post
        usr = request.form["name"] #getting the name of the user from the form on home page
        age = request.form["age"]
        yearofbirth = birthdate(age)
        if not usr: #if name is not defined it is set to default string
            usr = "<User Not Defined>"
    return render_template("account.html",username=usr, dayearofbirth=yearofbirth) #rendering our account.html contained within /templates

def birthdate(age):
    yearofbirth = 2024 - age
    return yearofbirth

if __name__ == "__main__": #checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)
