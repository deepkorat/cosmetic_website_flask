from flask import  Flask, Blueprint, render_template, url_for, request, session, flash, redirect
from flask import Blueprint
from .models import Category, Product, Order
from .forms import CheckoutForm
from datetime import datetime
from . import db


cosmetic_bp = Blueprint('main', __name__)

@cosmetic_bp.route('/')
def index():
     return render_template('index.html')

@cosmetic_bp.route('/category')
def category():
    category = Category.query.all()
    return render_template('category.html', category=category)

# show products category wise
@cosmetic_bp.route('/product/<int:category_id>')
def product(category_id):
    products = Product.query.filter(Product.category_id==category_id)
    return render_template('product.html', products=products)

# show all products
@cosmetic_bp.route('/all_product')
def all_product():
    products = Product.query.all()
    return render_template('product.html', products=products)

# show product search wise
@cosmetic_bp.route('/product/')
def search():
     search = request.args.get('search')
     search = "%{}%".format(search)
     products = Product.query.filter(Product.description.like(search) | Product.name.like(search)).all()
     return render_template('product.html', products=products)


@cosmetic_bp.route('/product_view/<int:product_id>')
def product_view(product_id):
    productdetail = Product.query.filter(Product.id == product_id).first()
    return render_template('product_view.html', productdetail = productdetail)


# add to cart function
@cosmetic_bp.route('/cart', methods=['POST','GET'])
def cart():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        print("Order is already exist. ")
    else:
        # there is no order
        order = None

    # create new order when its needed.
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            print(order)
            session['order_id'] = order.id
        except Exception as e:
            print('Oops!! failed at creating a new order, aaya error che bhai')
            order = None

    # calcultate totalprice
    total_price = 0
    if order is not None:
        for product in order.productdetails:
            total_price = total_price + product.price

    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        print(product)
        if product not in order.productdetails:
            try:
                order.productdetails.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.cart'))
        else:
            flash('Item already in basket.')
            return redirect(url_for('main.cart'))
    print(order)
    return render_template('add_to_cart.html', order = order, total_price=total_price)



# Delete specific basket items
@cosmetic_bp.route('/deleteorderitem', methods=['POST'])
def deleteitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.productdetails.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.cart'))
        except:
            return 'Not delete Item from Cart'
    return redirect(url_for('main.cart'))



@cosmetic_bp.route('/checkout', methods=['POST','GET'])
def checkout():
     form = CheckoutForm() 
     
     if 'order_id' in session:
          order = Order.query.get_or_404(session['order_id'])
          
          if request.method == 'POST':
               order.status = True
               order.firstname = form.firstname.data
               order.surname = form.surname.data
               order.email = form.email.data
               order.phone = form.phone.data
               totalcost = 0
               for book in order.productdetails:
                    totalcost = totalcost + book.price
               order.totalcost = totalcost
               order.date = datetime.now()
               try:
                    db.session.commit()
                    del session['order_id']
                    flash('Thank you for Ordered. One of our awesome team members will contact you soon...')
                    return redirect(url_for('main.index'))
               except:
                    return 'There was an issue completing your order'
     return render_template('checkout.html', form=form)