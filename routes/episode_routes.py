from flask import Blueprint, request, jsonify
from models.episode import Episode  
from models.appearance import Appearance  
from db import db 

episode_routes = Blueprint('episodes', __name__)

@episode_routes.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()  
    return jsonify([{
        "id": episode.id,
        "date": episode.date,
        "number": episode.number
    } for episode in episodes]), 200  
@episode_routes.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id) 
    if episode:
        appearances = Appearance.query.filter_by(episode_id=episode.id).all() 
        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [{
                "episode_id": appearance.episode_id,
                "guest": {
                    "id": appearance.guest.id,  
                    "name": appearance.guest.name,
                    "occupation": appearance.guest.occupation
                },
                "guest_id": appearance.guest_id,
                "id": appearance.id,
                "rating": appearance.rating
            } for appearance in appearances]
        }), 200  
    
    return jsonify({"error": "Episode not found"}), 404  

@episode_routes.route('/episodes', methods=['POST'])
def create_episode():
    data = request.json  
    new_episode = Episode(date=data['date'], number=data['number'])  
    db.session.add(new_episode) 
    db.session.commit()  
    return jsonify(new_episode.to_dict()), 201  

