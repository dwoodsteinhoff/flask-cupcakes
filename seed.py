from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
	flavor = "blueberry",
	image= "https://sallysbakingaddiction.com/wp-content/uploads/2016/04/blueberry-lemon-cupcakes.jpg",
	rating = 8.0,
	size= "small"
)

db.session.add_all([c1, c2, c3])
db.session.commit()