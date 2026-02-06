from extensions import db
from models.challenge import Challenge
from datetime import date,timedelta
from app import app

with app.app_context():
    print(Challenge.query.count())

    print(Challenge.query.filter_by(date=date.today()).all())

    db.create_all()

    start_date=date.today()

    challenges = [
        ("English" , "Write 5 lines about yourself"),
        ("Tech", "Open Excel and create a table"),
        ("Career", "Search one new job role online"),
    ]

    for i, (category, text) in enumerate(challenges * 10):
        challenge = Challenge(
            category = category,
            text = text,
            date = start_date + timedelta(days = i)
        )
        db.session.add(challenge)

    db.session.commit()
    print("30 challenges added successfully!")

    