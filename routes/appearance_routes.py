from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from models.appearance import Appearance 
from models.episode import Episode  
from models.guest import Guest  
from db import db  

#Appearance routes blueprint
appearance_routes = Blueprint('appearances', __name__)

#Routes
@appearance_routes.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()  
    return jsonify([appearance.to_dict() for appearance in appearances]), 200 

@appearance_routes.route('/appearances/<int:id>', methods=['GET'])
def get_appearance(id):
    appearance = Appearance.query.get(id)  
    if appearance:
        return jsonify(appearance.to_dict()), 200  
    return jsonify({"message": "Appearance not found"}), 404  

@appearance_routes.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json 
    # Validate required fields
    if not all(key in data for key in ("rating", "episode_id", "guest_id")):
        return jsonify({"errors": ["validation errors"]}), 400

    try:
        # Validate rating
        Appearance.validate_rating(data['rating']) 
        # Check for Episode and Guest
        episode = Episode.query.get(data['episode_id'])
        guest = Guest.query.get(data['guest_id'])
        if not episode or not guest:
            return jsonify({"errors": ["Episode or Guest not found"]}), 404

        # Create new appearance instance
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id'])  
        
        db.session.add(new_appearance)  
        db.session.commit()  

        # Prepare response data
        response_data = {
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "guest_id": new_appearance.guest_id,
            "episode_id": new_appearance.episode_id,
            "episode": {
                "date": episode.date,
                "id": episode.id,
                "number": episode.number
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }
        return jsonify(response_data), 201

    except ValidationError as ve:
        return jsonify({"errors": [str(ve)]}), 400 
    except Exception as error:
        return jsonify({"errors": ["An error occurred"]}), 500  # Handle other errors

