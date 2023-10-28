'''
Datase create and add initial data using dbseed database, also you can delete data to using "dbremove" function
'''

from flask import Blueprint
from . import db
from .models import Category, Product

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
     Category1 = Category(name='Skin')
     Category2 = Category(name='Hair')
    
     try:
          db.session.add(Category1)
          db.session.add(Category2)
          db.session.commit()
     except:
          return 'Oops!! There was an issue adding the Cateogy in dbseed function'

     product1 = Product(category_id=Category1.id,\
          name= 'Lakme Peach Milk Soft Creme Moisturizer',\
          description = 'This whipped cream formula has a soothing fragrance which will make you fall in love with it instantly. Thsi deeply nourishing formula easily absorbs into the skin to lock moisture for 12 hours to give you soft smooth glowing skin.    Lakme brings to you the goodness of peaches and milk in a creme for the very first time!  ',\
          ingredients= 'James Clear',\
          weight=50,\
          price=104,\
          image='p1.webp')

     product2 = Product(category_id=Category1.id,\
          name= 'Good Vibes Ubtan De Tan Glow Face Wash',\
          description = 'Is your skin loosing moisture as the day goes by ? Lakme brings to you the goodness of peaches and milk in a creme for the very first time! This whipped cream formula has a soothing fragrance which will make you fall in love with it instantly. Thsi deeply nourishing formula easily absorbs into the skin to lock moisture for 12 hours to give you soft smooth glowing skin. ',\
          ingredients= 'Ubtan, Tea Tree, Avocado, Milk & Oats, Organ Blossom',\
          weight=120,\
          price=211.00,\
          image='p2.webp')

     product3 = Product(category_id=Category1.id,\
          name= 'Lux Soft Skin Body Wash',\
          description = 'The alluring scent of French Roses will turn your shower into a moment of pure pleasure. Crafted by one of the best perfumer, top notes of bergamot and red fruits fill your senses before evolving into a feminine floral heart of rose, white florals and violets for perfume that indulges.',\
          ingredients= 'French Rose & Almond Oil, Lavender & Vitamin C',\
          weight=750,\
          price=300.00,\
          image='p3.webp')

     product4 = Product(category_id=Category1.id,\
          name= 'NIVEA Fresh Pure Shower Gel',\
          description = 'Experience the goodness of the Nivea fresh pure shower gel as its gentle sea minerals provide your skin with long lasting freshness.Let this fresh shower gel envelop your skin with a silky soft foam, while its fresh aquatic scent stimulates your senses',\
          ingredients= 'Sea Minerals',\
          weight=125,\
          price=129,\
          image='p4.webp')

     product5 = Product(category_id=Category1.id,\
          name= 'Nivea Powerfruit Fresh Shower Gel',\
          description = 'Gently cleanse your skin with this refreshing gel, containing Antioxidants from Blueberry and the delicious exotic scent of Acai Berry. Let the exotic fragrance of Acai Berry provide you with a feeling of invigorating freshness throughout the day while the silky shower gel with antioxidants from Blueberry caresses your skin and envelops you in smooth foam.',\
          ingredients= 'Blueberry, Waterlily Oil & Lemon Oil',\
          weight=250,\
          price=238,\
          image='p5.webp')

     product6 = Product(category_id=Category2.id,\
          name= "L'Oreal Paris Hyaluron Moisture Hydra Filling Night Cream", \
          description = 'Discover an exclusive night ritual enriched with hyaluronic acid to instantly infuse hair with deep hydration and seal cuticles overnight without any weigh down. Wakeup tohairthatissoft, detangled, and frizz controlled.First of its kind overnight technology created in the LOreal Laboratories gives you 4x more moisture in just 1 night, keeping your hair hydrated, shiny and bouncy. ',\
          ingredients= 'Hyaluronic acid for hair, Vitamin A',\
          weight=180,\
          price=346,\
          image='p6.webp')

     product7 = Product(category_id=Category2.id,\
          name= 'Sesa Ayurvedic Medicinal Shampoo',\
          description = 'CONTROL HAIR FALL IN 15 DAYS WITH AYURVEDA Hair fall can be a nightmare! Spending hours looking for a solution, reading reviews, buying expensive products and eventually being disappointed.',\
          ingredients= 'Bhringraj',\
          weight=500,\
          price=332,\
          image='p7.webp')

     product8 = Product(category_id=Category2.id,\
          name= "L'Oreal Paris Dream Lenghts Shampoo",\
          description = 'Dreaming of long hair but tired of long hair problems like hair breakage, damaged hair, and split ends? Save the last 3 cms of your hair',\
          ingredients= 'Castor oil, Vegetal Keratin, Vitamin PP & B5',\
          weight=800,\
          price=622,\
          image='p8.webp')

    
     try:
          db.session.add(product1)
          db.session.add(product2)
          db.session.add(product3)
          db.session.add(product4)
          db.session.add(product5)
          db.session.add(product6)
          db.session.add(product7)
          db.session.add(product8)

          db.session.commit()
     except:
          return 'Sorry, There was an issue to adding a Cosmetic Product in database.'

     return 'DATA LOADED SUCCESSFULLY'


@admin_bp.route('/dbremove')
def dbremove():
     # Delete all records
     try:
          Category.query.delete()
          Product.query.delete()
          db.session.commit()
          return "DATA DELETED SUCCESSFULLY"
     except:
          return "OOPS!! DATA NOT DELETED."
