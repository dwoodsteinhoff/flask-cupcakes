"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

app.app_context().push()

connect_db(app)

@app.route('/')
def index_page():

    return render_template ("index.html")

@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    all_cupcakes = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcake():

    new_cupcake = Cupcake(flavor=request.json['flavor'], image=request.json['image'], rating=request.json['rating'], size=request.json['size'])

    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.iamge = request.json.get('image', cupcake.image)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.size = request.json.get('size', cupcake.size)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = "deleted")