from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy import func, extract

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

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    amount = data.get("amount")
    description = data.get("description")
    category_id = data.get("category_id")

    if amount is None or category_id is None:
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
        "expense": expense.to_dict()
    }), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():
    category_id = request.args.get("category_id")

    if category_id:
        expenses = Expense.query.filter_by(category_id=category_id).all()
    else:
        expenses = Expense.query.all()
        
    result = [expense.to_dict() for expense in expenses]
    return jsonify(result), 200

@app.route("/expenses/<int:id>", methods=["GET"])
def get_expense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    return jsonify(expense.to_dict()), 200

@app.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted"}), 200

@app.route("/expenses/<int:id>", methods=["PUT"])
def update_expense(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    expense = Expense.query.get(id)

    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    
    if "amount" in data:
        expense.amount = data["amount"]

    if "description" in data:
        expense.description = data["description"]

    if "date" in data:
        expense.date = date.fromisoformat(data["date"])

    if "category_id" in data:
        expense.category_id = data["category_id"]

    db.session.commit()

    return jsonify({
        "message": "Expense updated",
        "id": expense.id,
        "amount": expense.amount,
        "description": expense.description,
        "category_id": expense.category_id
    })  

@app.route("/expenses/total", methods=["GET"])
def get_total_spent():
    expenses = Expense.query.all()

    total = 0
    for expense in expenses:
        total += expense.amount

    return jsonify({
        "total_spent": total
    }), 200

@app.route("/expenses/summary/month", methods=["GET"])
def monthly_summary():
    results = (
        db.session.query(
            extract("year", Expense.date).label("year"),
            extract("month", Expense.date).label("month"),
            func.sum(Expense.amount).label("total")
        )
        .group_by("year", "month")
        .order_by("year", "month")
        .all()
    )

    summary = []
    for row in results:
        summary.append({
            "year": int(row.year),
            "month": int(row.month),
            "total": float(row.total)
        })
    
    return jsonify(summary), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


