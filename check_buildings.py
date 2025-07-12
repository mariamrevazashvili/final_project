from app import create_app, db
from app.models import Building

app = create_app()

with app.app_context():
    buildings = Building.query.all()
    print(f"ნაგებობების რაოდენობა: {len(buildings)}")
    for b in buildings:
        print(f"- {b.title}: {b.description[:50]}...")
