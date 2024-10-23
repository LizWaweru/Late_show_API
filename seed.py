from flask import Flask  
from models.episode import Episode  
from models.guest import Guest 
from models.appearance import Appearance  
from db import db  

app = Flask(__name__)
# Configure the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def populate_tables():
    with app.app_context():  
        db.drop_all()  
        db.create_all()  

        # Inserting data into the Guest table 
        guest_data = [
            ('Michael J. Fox', 'actor'),
            ('Sandra Bernhard', 'comedian'),
            ('Tracey Ullman', 'television actress'),
            ('Gillian Anderson', 'film actress'),
            ('David Alan Grier', 'actor'),
            ('William Baldwin', 'actor'),
            ('Michael Stipe', 'singer-lyricist'),
            ('Carmen Electra', 'model'),
            ('Matthew Lillard', 'actor'),
            ('David Cross', 'stand-up comedian'),
        ]

        # create a Guest object
        for name, occupation in guest_data:
            guest = Guest(name=name, occupation=occupation)
            db.session.add(guest)  

        # Inserting data into the Episode table
        episode_data = [
            ('1/5/99', 1),
            ('1/12/99', 2),
            ('1/19/99', 3),
            ('1/26/99', 4),
            ('2/2/99', 5),
            ('2/9/99', 6),
            ('2/16/99', 7),
            ('2/23/99', 8),
            ('3/2/99', 9),
            ('3/9/99', 10),
        ]

        # create an Episode object
        for date, number in episode_data:
            episode = Episode(date=date, number=number)
            db.session.add(episode)  

         # (rating, episode_id, guest_id)
        appearance_data = [
            (1, 1, 1), 
            (2, 2, 2),
            (3, 3, 3),
            (4, 4, 4),
            (5, 5, 5),
        ]

        # create an Appearance object
        for rating, episode_id, guest_id in appearance_data:
            Appearance.validate_rating(rating)  

            appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
            db.session.add(appearance) 

        db.session.commit()  

if __name__ == '__main__':
    populate_tables()  
