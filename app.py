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

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "date": self.date,
            "category_id": self.category_id
        }

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

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    amount = data.get("amount")
    description = data.get("description")
    category_id = data.get("category_id")

    if not amount or not category_id:
        return jsonify({"error": "Amount and category_id are required"}), 400
    
    expense = Expense(
        amount=amount,
        description=description,
        date=date.today(),
        category_id=category_id
    )

    db.session.add(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense added",
        "id": expense.id,
        "amount": expense.amount,
    }), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = Expense.query.all()
    result = [expense.to_dict() for expense in expenses]
    return jsonify(result), 200

@app.route("/expenses/<int:id>", methods=["GET"])
def get_expense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    return jsonify(expense.to_dict()), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


