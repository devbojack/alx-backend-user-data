#!/usr/bin/env python3
"""Authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/')

        for x_path in excluded_paths:
            x_path = x_path.rstrip('/')
            if x_path.endswith('*') and path.startswith(x_path[:-1]):
                return False
            elif path == x_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None
