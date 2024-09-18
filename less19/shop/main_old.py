from sqlalchemy.orm import sessionmaker

from models.category import Category
from models.goods import Good
from models.traders import Trader
from models.orders import Order
from models.base import Base, engine

from views import my_ord 

metadata = Base.metadata
session_pool = sessionmaker(bind=engine)

# category1 = Category(name="produkty")
# category2 = Category(name="bytovyje")
# category3 = Category(name="instrument")

# trader1 = Trader(
#     firstName="Vasilij", 
#     lastname="Pupkin",
#     email="vasil.pup@gmail.com",
#     address="Partizan.st 123"
#     )

# trader2 = Trader(
#     firstName="Yuri", 
#     lastname="Sidorov",
#     email="yuri.sid@gmail.com",
#     address="Masherov.st 13"
#     )

# trader3 = Trader(
#     firstName="Ivan", 
#     lastname="Ivanov",
#     email="ivan.ivn@gmail.com",
#     address="Kuncevskaya.st 6"
#     )

# good1 = Good(
#     name="Chleb",
#     category=category1,
#     trader = trader1
#     )

# good2 = Good(
#     name="Venik",
#     category=category2,
#     trader = trader3
#     )

# good3 = Good(
#     name="Otvertka",
#     category=category3,
#     trader = trader2
#     )

# with session_pool() as session:
#     session.add_all([category1, category2, category3, trader1, trader2, trader3, good1, good2, good3]) # Add the new user to the session
#     session.commit()

with session_pool() as session:
    my_ord.show_goods(session)
    print("Make your order!")
    new_order = my_ord.make_order(session)
    session.add(new_order)
    session.commit()

# if __name__ == "__main__":
#     # Create the table in the database
#     metadata.create_all(engine)