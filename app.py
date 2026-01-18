from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(100))
    date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer, 
        db.ForeignKey("category.id")
    )

@app.route("/")
def home():
    return "Flask is running!"

@app.route("/categories", methods=["POST"])
def add_category():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Category name is required"}), 400
    
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category added", 
                    "id": category.id,
                    "name": category.name}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


