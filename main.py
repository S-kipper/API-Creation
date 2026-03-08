from flask import Flask, request, jsonify  #This is bascially us importing the dependencies from Flask

'''Now we need to create our flask application'''
app = Flask(__name__) #This line creates your web server application
"""__name__ is a special Python variable that tells Flask where the application is running from"""

"""We need to create a root which is basically an endpoint which is kinda a location on the API we can go to, to get some kind of data (We have different kinds of roots too)"""

'''
@app.route("/") #To make this accessible we use a decorator and the name of the application in this case its app in the bracket you add the path that we want to access in this case its "/" which is the default root  
def home(): #Returning some data that the user will have access too when they reach this root
    return "Home" 
'''
    
'''Now we are about to use HTTP Methods to make more complex routes'''
@app.route("/get-user/<user_id>") #<user-id> is known as a path parameter - (now a path parameter is a dynamic value that you can pass in the path an URL that we will be able to access inside of our root)
def get_user(user_id):
    user_data = {
            "user_id" : user_id,
            "name" : "Aditya",
            "email" : "adi@exmple.com"
    }
    
    extra = request.args.get("extra")    #args basically stores all the query parameters in a dictionary
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200 #200 here is called the Status code (it is the default status code for success)

@app.route("/create-user", methods= ["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201
    
    
if __name__ == "__main__": #This is basically a python convention and checks if this file is running directly 
    app.run(debug = True) #http://127.0.0.1:5000  This the default server that runs the application
