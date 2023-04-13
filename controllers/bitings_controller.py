from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.biting import Biting
import repositories.biting_repository as biting_repository
from models.human import Human
import repositories.human_repository as human_repository
from models.zombie import Zombie
import repositories.zombie_repository as zombie_repository

bitings_blueprint = Blueprint("bitings", __name__)


@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all() # NEW
    return render_template("bitings/index.html", bitings=bitings)

# NEW
# GET '/bitings/new'
@bitings_blueprint.route("/bitings/new", methods=['GET'])
def new_biting():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans = humans, zombies = zombies)

# CREATE
# POST '/bitings'
@bitings_blueprint.route("/bitings",  methods=['POST'])
def create_biting():
    human_id = request.form['human_id']
    zombie_id = request.form['zombie_id']
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    biting = Biting(human, zombie)
    biting_repository.save(biting)
    return redirect('/bitings')


# DELETE
# DELETE '/bitings/<id>'
@bitings_blueprint.route("/bitings/<id>/delete", methods=['POST'])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect('/bitings')

# INDEX

# NEW

# CREATE

# EDIT
@bitings_blueprint.route("/bitings/<id>/edit")
def edit_biting(id):
    biting = biting_repository.select(id)
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template('bitings/edit.html', biting=biting, humans=humans, zombies=zombies)
# UPDATE

# DELETE
