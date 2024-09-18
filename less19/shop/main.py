from flask import Flask, render_template, request, make_response, redirect
from sqlalchemy.orm import sessionmaker
from models.base import engine
from models.category import Category
from models.goods import Good
from models.traders import Trader
from models.orders import Order

app = Flask(__name__)
session_pool = sessionmaker(bind=engine)

@app.route("/")
def get_goods():
    with session_pool() as session:
        some_goods = session.query(Good).all()
    return render_template("goods.html", goods=some_goods)


@app.route("/traders")
def get_traders():
    with session_pool() as session:
        some_traders = session.query(Trader).all()
    return render_template("traders.html", traders=some_traders)


@app.route("/trader/add", methods=["GET", "POST"])
def add_trader():
    if request.method == "POST":
        new_trader = Trader(
            firstName=request.form["first_name"],
            lastname=request.form["last_name"],
            email=request.form["email"],
            address=request.form["address"],
        )
        with session_pool() as session:
            session.add(new_trader)
            session.commit()
        return redirect("/traders")
    else:
        return render_template("add_trader.html")


@app.route("/trader/edit/<id_t>", methods=["GET", "POST"])
def edit_trader(id_t):
    if request.method == "POST":
        with session_pool() as session:
            session.query(Trader).filter(Trader.id==id_t).update(
                {
                    "firstName": request.form["first_name"],
                    "lastname": request.form["last_name"],
                    "email": request.form["email"],
                    "address": request.form["address"]
                }
            )
            session.commit()
        return redirect("/traders")
    else:
        with session_pool() as session:
            requested_trader = session.query(Trader).filter(Trader.id==id_t).first()
        return render_template("edit_trader.html", trader=requested_trader)


@app.route("/trader/delete/<id_t>", methods=["GET"])
def delete_trader(id_t):
    with session_pool() as session:
        session.query(Trader).filter(Trader.id==id_t).delete()
        session.commit()
    return redirect("/traders")

if __name__ == "__main__":
    app.run("localhost", 8000)
