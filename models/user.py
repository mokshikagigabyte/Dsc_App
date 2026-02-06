from extensions import db
from datetime import date

class User(db.Model):
    __tablename__ ="user"
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(120),nullable =False)
    streak = db.Column(db.Integer, default=0)
    last_completed = db.Column(db.Date)

    submissions = db.relationship("Submission",backref="user", lazy=True)


    def update_streak(self):
        today = date.today()
        if self.last_completed == today:
            return
        elif self.last_completed and (today.toordinal() - self.last_completed.toordinal() == 1):
            self.streak += 1
        else:
            self.streak = 1

        self.last_completed = today

    @property
    def total_marks(self):
        return sum(sub.marks for sub in self.submissions if sub.verified)
    
    @property
    def percentage(self):
        total_challenges = len(self.submissions)
        if total_challenges == 0:
            return 0
        return round((self.total_marks/(total_challenges * 10))* 100,2)