from . import db

class Category(db.Model):
     __tablename__ = 'categories'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable=False)
     productdetails = db.relationship('Product', backref='Category', cascade="all, delete-orphan")

     def __repr__(self):
          return f"\nID: {self.id}\nCategory: {self.name}"


orderdetails = db.Table('orderdetails', 
db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
db.Column('product_id',db.Integer,db.ForeignKey('product_details.id'),nullable=False),
db.PrimaryKeyConstraint('order_id', 'product_id') ) 


class Product(db.Model):
     __tablename__ = 'product_details'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable=False)
     description = db.Column(db.String(500), nullable=False)
     ingredients = db.Column(db.String(255), nullable=False)
     weight = db.Column(db.Float, nullable=False)
     price = db.Column(db.Float, nullable=False)
     image = db.Column(db.String(60), nullable=False)
     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

     def __repr__(self):
          return f"\nID: {self.id}\nName: {self.name}\nDescription: {self.description}\nIngredients: {self.ingredients}\nWeight: {self.weight}\nPrice: {self.price}\nImage: {self.image}\nCategory: {self.category_id}"


class Order(db.Model):
     __tablename__ = 'orders'
     id = db.Column(db.Integer, primary_key=True)
     status = db.Column(db.Boolean, default=False)
     firstname = db.Column(db.String(64))
     surname = db.Column(db.String(64))
     email = db.Column(db.String(128))
     phone = db.Column(db.String(32))
     totalcost = db.Column(db.Float)
     date = db.Column(db.DateTime)
     productdetails = db.relationship("Product", secondary=orderdetails, backref="orders")

     def __repr__(self):
          return f"ID: {self.id}\nStatus: {self.status}\nFirst Name: {self.firstname}\nSurname: {self.surname}\nEmail: {self.email}\nPhone: {self.phone}\nDate: {self.date}\nProduct Details: {self.productdetails}\nTotal Cost: ${self.totalcost}"


