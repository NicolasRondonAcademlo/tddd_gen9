import unittest
from auth import  Authentication, Authorization

class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "testpass")

        assert resp == {"username": "testuser", "password": "testpass"}


class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        resp = authz.can({"username": "testuser"}, "create")

        assert resp is True

# Ahora debemos construir nuestro test de integracion
class TestAuthorizeAuthenticatedUser(unittest.TestCase):
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        authz.PERMISSIONS = [{"user": "testuser",
        "permissions": {"create"}}]
        u = auth.login("testuser", "testpass")
        resp = authz.can(u, "create")
        assert resp is True

if __name__ == '__main__':
    unittest.main()
