from db import db

class Appearance(db.Model):
    __tablename__ = 'appearances'  

    
    id = db.Column(db.Integer, primary_key=True) 
    rating = db.Column(db.Integer, nullable=False)  
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False) 
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)      

    
    episode = db.relationship('Episode', back_populates='appearances') 
    guest = db.relationship('Guest', back_populates='appearances')      

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id,
            'guest': self.guest.to_dict() if self.guest else None,  
        }

    @classmethod
    def validate_rating(cls, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")  # Raise error if the rating is invalid
