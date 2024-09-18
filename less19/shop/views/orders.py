from models.orders import Order
from models.goods import Good

def show_goods(session):
    goods = session.query(Good).all()
    # goods = good_class.query.all()
    for good in goods:
        print(good)

def make_order(session):
    good_name = input("Enter good name: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    notes = input("Enter notes: ")

    requested_good = session.query(Good) \
                            .filter(Good.name == good_name).first()
    
    new_order = Order(
        address = address,
        email = email,
        notes = notes,
        good = requested_good
    )

    return new_order