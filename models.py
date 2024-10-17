from extensions import db

class Episode(db.Model):
    """Represents a TV show episode."""
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the episode
    date = db.Column(db.String, nullable=False)    # Air date of the episode
    number = db.Column(db.Integer, nullable=False)  # Episode number in the series
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")
    # One-to-many relationship with Appearance; if an episode is deleted, its appearances are also deleted.

class Guest(db.Model):
    """Represents a guest on a TV show episode."""
    id = db.Column(db.Integer, primary_key=True)   # Unique identifier for the guest
    name = db.Column(db.String, nullable=False)      # Name of the guest
    occupation = db.Column(db.String, nullable=False) # Occupation of the guest
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")
    # One-to-many relationship with Appearance; if a guest is deleted, their appearances are also deleted.

class Appearance(db.Model):
    """Represents the appearance of a guest in an episode."""
    id = db.Column(db.Integer, primary_key=True)    # Unique identifier for the appearance
    rating = db.Column(db.Integer, nullable=False)    # Rating of the guest's appearance (1-5)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id')) # Foreign key linking to the Episode
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))     # Foreign key linking to the Guest

    def __init__(self, rating, episode_id, guest_id):
        """Initialize an Appearance instance with validation."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")  # Validate that rating is between 1 and 5
        self.rating = rating
        self.episode_id = episode_id
        self.guest_id = guest_id
