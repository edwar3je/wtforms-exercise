from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Establishes a connection between Flask and the database ('adoption_agency')"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """A model used to create the table 'pets' inside the database 'adoption_center' and to create new pet instances. Default values
    have been provided for the 'optional' fields if no values are provided."""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    species = db.Column(db.String(70), nullable=False)
    # maybe add a default image?
    photo_url = db.Column(db.String(400), nullable=False, default='https://w7.pngwing.com/pngs/430/764/png-transparent-a-group-of-pet-dogs-border-collie-the-dog-pet.png')
    age = db.Column(db.Integer, nullable=False, default='Not listed. Contact us to learn more.')
    notes = db.Column(db.String(500), nullable=False, default='This little one does not have any notes. Contact us to learn more.')
    # check if the boolean default works
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, name, species, photo_url, age, notes, available):
        self.name = name
        self.species = species
        self.photo_url = photo_url
        self.age = age
        self.notes = notes
        self.available = available

# Create a small set of data to place into the database upon running Flask
def init_data():
    """Provides a small set of data to initialize the table 'pets' in the database ('adoption_center) upon application startup"""
    reggie = Pet('Reggie', 'dog', 'https://a-z-animals.com/media/2021/08/681px-Jaxson_-_American_Bully_Pocket_Male_8599222904.jpg', 2, 
    'Reggie is very energetic and loves to play with kids and adults alike.', True)
    sparkles = Pet('Sparkles', 'cat', 'https://www.thehappycatsite.com/wp-content/uploads/2017/12/White-Cat-HC-long.jpg', 4,
    'Sparkles got her name because she always loves to be the center of attention.', True)
    cleo = Pet('Cleo', 'dog', 'https://dogsbestlife.com/wp-content/uploads/2020/08/Vizsla-1366x2048.jpg', 1,
    'Cleo is a bit shy, but she warms up to everyone quickly.', True)
    cheetoh = Pet('Cheetoh', 'cat', 'https://www.nicepng.com/png/detail/821-8219216_orangecat-cute-orange-tabby-cat.png', 5,
    'Cheetoh is a very social cat that loves to race everything.', None)
    db.session.add(reggie)
    db.session.add(sparkles)
    db.session.add(cleo)
    db.session.add(cheetoh)
    db.session.commit()