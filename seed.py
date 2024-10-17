from app import app, db
from models import Episode, Guest, Appearance

# Create an application context
with app.app_context():
    # Create sample data
    episode1 = Episode(date="1/11/99", number=1)
    guest1 = Guest(name="Michael J. Fox", occupation="actor")

    # Add records to the session
    db.session.add_all([episode1, guest1])
    db.session.commit()

    appearance1 = Appearance(rating=4, episode_id=episode1.id, guest_id=guest1.id)
    db.session.add(appearance1)
    db.session.commit()

    print("Database seeded successfully!")
