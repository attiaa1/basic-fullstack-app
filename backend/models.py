# defining database models
from config import db

class Contact(db.Model):
    # always have id for database instances
    id = db.Column(db.Integer, primary_key=True)
    # whenever you specify string column, have to pass in max length
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    # object => python dict => json for API requests/response
    def to_json(self):
        return{
            
            # camelcase for JSON, snake case for python
            "id":self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email
            
        }
        
