"""Models for melon tasting reservation scheduler."""

from flask_sqlalchemy import SQLAlchemy

#instantiates SQLAlchemy object
db = SQLAlchemy()

# Assuming your Flask app is in server.py
def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    app.app_context().push()

    with app.app_context(): 
        db.create_all()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Appointment(db.Model):
    """An appointment."""

    __tablename__ = "appointment"

    appointment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    appointment = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


    def __repr__(self):
        return f'<Appointment: appointment_id={self.appointment_id}, user_id={self.user_id}>'

if __name__ == "__main__":
    from server import app
    app.app_context()
    connect_to_db(app, "melon-tasting-scheduler-db")