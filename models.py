"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__= "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    flavor = db.Column(db.Text,
                       nullable = False)
    
    size = db.Column(db.Text,
                     nullable = False)
    
    rating = db.Column(db.Float,
                       nullable = False)
    
    image = db.Column(db.Text,
                      nullable = False,
                      default = "https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor' : self.flavor,
            'size': self.size,
            'rating' : self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} flaver={self.flavor} size={self.size} rating={self.rating} image={self.image}"