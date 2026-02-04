from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expense_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        note = request.form["note"]
        expense = {"Amount": amount, "Category": category, "Note": note}
        expense_list.append(expense)
        return redirect(url_for("view_expenses"))
    return render_template("add.html")

@app.route("/view")
def view_expenses():
    total = sum(expense["Amount"] for expense in expense_list)
    return render_template("view.html", expenses=expense_list, total=total)

@app.route("/summary")
def category_summary():
    category_totals = {}
    for expense in expense_list:
        category_totals[expense["Category"]] = category_totals.get(expense["Category"], 0) + expense["Amount"]
    return render_template("summary.html", summary=category_totals)

@app.route("/save")
def save_to_file():
    with open("expenses.txt", "w") as f:
        for expense in expense_list:
            f.write(f"{expense['Amount']},{expense['Category']},{expense['Note']}\n")
    return "Expenses saved to expenses.txt"

if __name__ == "__main__":
    app.run(debug=True)
