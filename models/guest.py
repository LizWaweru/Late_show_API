from db import db

class Guest(db.Model):

    __tablename__ = 'guests'  

    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String, nullable=False)     
    occupation = db.Column(db.String, nullable=False)  

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }
