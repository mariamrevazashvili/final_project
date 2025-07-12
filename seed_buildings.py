from app import create_app, db
from app.models import Building

app = create_app()

with app.app_context():
    buildings = [
        Building(
            title="ატენის სიონი",
            image="images/ateni.jpg",
            description="VII საუკუნის ქართული ტაძარი შიდა ქართლში."
        ),
        Building(
            title="დანახვისის მონასტერი",
            image="images/danakhvisi.jpg",
            description="XI საუკუნის მონასტერი შიდა ქართლში."
        ),
        Building(
            title="მარტვილის კანიონი",
            image="images/martvili.jpg",
            description="მდინარე აბაშის ულამაზესი კანიონი სამეგრელოში."
        ),
        Building(
            title="უფლისციხე",
            image="images/uplistsikhe.jpg",
            description="უძველესი კლდეში ნაკვეთი ქალაქი შიდა ქართლში."
        ),
    ]

    db.session.add_all(buildings)
    db.session.commit()
    print("ნაგებობები წარმატებით დაემატა!")
