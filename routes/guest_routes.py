from flask import Blueprint, request, jsonify
from models.guest import Guest  
from db import db 

guest_routes = Blueprint('guests', __name__)

@guest_routes.route('/guests', methods=['GET'])
def get_guests():
    """Retrieve a list of all guests."""
    guests = Guest.query.all()  
    return jsonify([{
        "id": guest.id,
        "name": guest.name,
        "occupation": guest.occupation
    } for guest in guests]), 200  

@guest_routes.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get(id)  
    if guest:
        return jsonify({
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }), 200  
    return jsonify({"error": "Guest not found"}), 404 

@guest_routes.route('/guests', methods=['POST'])
def create_guest():
    data = request.json  
    new_guest = Guest(name=data['name'], occupation=data['occupation']) 
    db.session.commit()  
    return jsonify(new_guest.to_dict()), 201 

@guest_routes.route('/guests/<int:id>', methods=['PUT'])
def update_guest(id):
   
    guest = Guest.query.get(id)  
    if guest:
        data = request.json 
        guest.name = data['name']  
        guest.occupation = data['occupation']  
        db.session.commit()  
        return jsonify(guest.to_dict()), 200  
    return jsonify({"error": "Guest not found"}), 404  

@guest_routes.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    
    guest = Guest.query.get(id)  
    if guest:
        db.session.delete(guest) 
        db.session.commit()  
        return jsonify({"message": "Guest deleted"}), 204  
    return jsonify({"error": "Guest not found"}), 404 
