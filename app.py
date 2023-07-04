from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, init_data, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_center'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'edwar3je'

connect_db(app)

# Upon connection, the application will drop any prior tables created and create a new table with some data
with app.app_context():
    db.drop_all()
    db.create_all()
    init_data()
 
@app.route('/')
def display_home_page():
    """Displays the home page along with the available pets (based on information from 'pets' table in the database)"""
    with app.app_context():
        pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/pet/<pet_id>', methods=["GET", "POST"])
def display_and_edit_pet_details(pet_id):
    """If the request is a GET request, the route will render a page containing information on the pet (based on id), along with a form 
    that will allow users to edit up to three fields. If the request is a POST request, the route will update the pet instance in the 
    database (but only if new information is present) and redirect the user to the home page."""
    path_id = int(request.path.replace('/pet/', ''))
    with app.app_context():
        current_pet = Pet.query.get(path_id)
    form = EditPetForm()
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        print(photo_url)
        print(notes)
        print(available)
        with app.app_context():
            edited_pet = Pet.query.get(path_id)
            if photo_url:
                edited_pet.photo_url = photo_url
            if notes:
                edited_pet.notes = notes
            if available != edited_pet.available:
                edited_pet.available = available
            db.session.add(edited_pet)
            db.session.commit()
        return redirect('/')
    else:
        return render_template('pet.html', form=form, pet=current_pet)

@app.route('/add', methods=["GET", "POST"])
def display_and_handle_add_form():
    """If the request is a GET request, the route will render a page containing a form that allows users to add a new pet instance to
    the database (the form also contains validations for each field). If the request is a POST request, the route will process the request
    and (if successful), will add the new pet instance to the database and redirect the user to the home page."""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = True
        new_pet = Pet(name, species, photo_url, age, notes, available)
        with app.app_context():
            db.session.add(new_pet)
            db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form=form)