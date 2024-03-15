from flask import request, jsonify
from config import app
from models import Contact, db

# get method => get some context
# decorator above func
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # how to handle get request sent to route
    # uses flask sqlalchemy to get all of contacts as python obj
    contacts = Contact.query.all()
    # contact is list of obj => all have to_json method, and create new list with it
    # contacts.to_json() as maps obj => to list
    json_contacts = list(map(lambda x: x.to_json(),contacts))
    
    return jsonify({"contacts":json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return(
            jsonify({"message":"You must include a first name, last name, and email"}),
            400 # default is 200, this will say bad request
        )
    
    new_contact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    
    try:
        # not fully written to db, in limbo
        db.session.add(new_contact)
        # adds to database permanently
        db.session.commit()
    # need to account for errors cropping up here
    except Exception as e:
        return jsonify({"message":str(e)}), 400
    
    return jsonify({"message": "User Created."}), 201 # stands for created

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message":"User not found"}), 404

    data = request.json
    
    # handles any type of request to "update" by using the default return of the get function
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    # already exists, no need to add
    db.session.commit()
    return jsonify({"message": "User updated."}), 200

# deleting
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message":"User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "User deleted."}), 200
    

if __name__ == "__main__":
    
    # create instance of database
    with app.app_context():
        db.create_all() 
    
    app.run(debug=True)