from flask import Flask, jsonify, request, abort
from extensions import db, migrate
from models import Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tv_shows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    return jsonify({"message": "TV Show API"})

# Episodes routes

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": len(episode.appearances)
    } for episode in episodes]), 200

@app.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()
    new_episode = Episode(date=data['date'], number=data['number'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({"message": "Episode created", "episode": {
        "id": new_episode.id,
        "date": new_episode.date,
        "number": new_episode.number
    }}), 201

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200

# Guests routes

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": guest.id,
        "name": guest.name,
        "occupation": guest.occupation,
        "appearances": len(guest.appearances)
    } for guest in guests]), 200

@app.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    new_guest = Guest(name=data['name'], occupation=data['occupation'])
    db.session.add(new_guest)
    db.session.commit()
    return jsonify({"message": "Guest created", "guest": {
        "id": new_guest.id,
        "name": new_guest.name,
        "occupation": new_guest.occupation
    }}), 201

@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = Guest.query.get_or_404(id)
    db.session.delete(guest)
    db.session.commit()
    return jsonify({"message": "Guest deleted"}), 200

# Appearances routes

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify({"message": "Appearance created", "appearance": {
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "episode_id": new_appearance.episode_id,
            "guest_id": new_appearance.guest_id
        }}), 201
    except ValueError as e:
        abort(400, description=str(e))

@app.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    db.session.delete(appearance)
    db.session.commit()
    return jsonify({"message": "Appearance deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
