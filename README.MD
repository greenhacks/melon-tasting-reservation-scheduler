## Melon Tasting Reservation Scheduler

# MVP
- All reservations must start and end on the hour or half hour (completed)
- All reservations are exactly 30 minutes long (completed)
- A user can only have 1 reservation on a calendar date (#tooMuchMelon) (in progress)
- No two appointments can be scheduled at the same time (in progress)


# Technologies
- Python, Flask for the server
- HTML, Javascript for the front end
- PostgreSQL and SQLAlchemy for the database
- Calendly API

I chose these technologies because I thought they facilitated the MVP best. Flask is lightweight. However, I ran into a challenge figuring out how to persist appointment data from the Calendly API from the documentation. I would address this by reviewing other APIs for better data integration.

# Database Structure
- I chose to create User and Appointment classes for my database in a one-to-one relationship.

