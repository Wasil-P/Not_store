import db
from models import Base
from models.products import Products



db.configure_engine()
# Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)

session = db.Session()

s_products = Products(name="silver pen", cost=10, count=100)
p_products = Products(name="platinum pen", cost=20, count=12)
g_products = Products(name="golden pen", cost=40, count=2)
session.add(s_products)
session.add(p_products)
session.add(g_products)
session.commit()


