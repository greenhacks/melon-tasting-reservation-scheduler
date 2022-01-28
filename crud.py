from model import db, User

def create_user(email):
    """Create and return a new user."""

    # Standardize input
    email = str(email).lower()

    # instantiate user
    user = User(email=email)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Get a user by email."""

    try:
        user = User.query.filter(User.email == email).one() #needs to be .one because we want a unique user
        return user # user will be either the user or None

    except Exception as e:
        print(e)
        print('\n'*10)
        return None
