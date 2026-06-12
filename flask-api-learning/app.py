from flask import Flask, request, jsonify


app = Flask(__name__)

# GET route 
# this is the route with the link, and the path parameter(dynamic)
@app.route("/user-id/<user_id>")
def get_user(user_id):
    #fake data to test
    user_data = {
        "user_id": user_id,
        "name": "onion",
        "email": "onion@gmail.com"
    }

    #the extra parameters that goes after "?", ex. /user-id/100?extra="hi" 
    extra = request.args.get("extra")
    # check if there is an extra parameter and adds it to the user data
    if extra:
        user_data["extra"] = extra

    #make the data json and post with 200 HTTP code
    return jsonify(user_data) , 200

if __name__ == "__main__":
    app.run(debug=True)

