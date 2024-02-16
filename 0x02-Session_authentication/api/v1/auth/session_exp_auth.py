#!/usr/bin/env python3
"""Session Expiration"""

import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session Expiration
    """

    def __init__(self):
        super().__init__()
        self.session_duration = self.get_session_duration()

    def get_session_duration(self):
        """Get a session duration
        """
        session_duration_str = os.getenv("SESSION_DURATION")
        try:
            session_duration = int(session_duration_str)
        except (ValueError, TypeError):
            session_duration = 0
        return session_duration

    def create_session(self, user_id=None):
        """Create a session
        """
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                "user_id": user_id,
                "created_at": datetime.now()
            }
            return session_id
        else:
            return None

    def user_id_for_session_id(self, session_id=None):
        """User id for session id
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        if self.session_duration <= 0:
            return session_dict.get("user_id")

        created_at = session_dict.get("created_at")
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return session_dict.get("user_id")
