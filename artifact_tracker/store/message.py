from artifact_tracker import tracker_app
from sqlalchemy import JSON

db = tracker_app.db


class InboxMessage(db.Model):
    """
    TODO:
    Storage of inbox AS2 messages for API audit of messages.
    """
    message = db.Column(db.Data(), JSON)
    created_at = db.Column(db.DateTime())
    last_updated = db.Column(db.DateTime())

    update_count = db.Column(db.Integer())
    # Status of task
    completed = db.Column(db.Boolean(), default=False)
