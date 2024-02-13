#!/usr/bin/env python3
"""Basic Authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Required Auth"""
        if path is None:
            return True

        if not excluded_paths:
            return True

        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if path == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authrozation header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
