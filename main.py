from flask import Flask, request, jsonify  #This is bascially us importing the dependencies from Flask

'''Now we need to create our flask application'''
app = Flask(__name__) #This line creates your web server application
"""__name__ is a special Python variable that tells Flask where the application is running from"""

"""We need to create a root which is basically an endpoint which is kinda a location on the API we can go to, to get some kind of data (We have different kinds of roots too)"""

@app.route("/") #To make this accessible we use a decorator and the name of the application in this case its app in the bracket you add the path that we want to access in this case its "/" which is the default root  
def home(): #Returning some data that the user will have access too when they reach this root
    return "Home"

if __name__ == "__main__": #This is basically a python convention and checks if this file is running directly 
    app.run(debug = True) #http://127.0.0.1:5000  This the default server that runs the application
