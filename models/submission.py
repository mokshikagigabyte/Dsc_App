from extensions import db

class Submission(db.Model):
    __tablename__ = "submissions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey("challenges.id"), nullable=False)
    answer = db.Column(db.Text)
    verified = db.Column(db.Boolean, default=False)
    marks = db.Column(db.Integer, default=0)
