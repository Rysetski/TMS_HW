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