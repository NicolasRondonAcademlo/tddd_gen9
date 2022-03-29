import unittest
from auth import Authentication, Authorization


class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "testpass")

        assert resp == {"username": "testuser", "password": "testpass"}

    def test_failed_login(self):
        " Agregar"
        auth = Authentication()

        resp = auth.login("usernotexisting", "")

        assert resp is None

    def test_wrong_password(self):
        " Agregar"
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "wrongpass")

        assert resp == None

    def test_fetch_user(self):
        " Agregar"
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        user = auth.fetch_user("testuser")

        assert user == {"username": "testuser", "password": "testpass"}

    def test_fetch_user_not_existing(self):
        " Agregar"
        auth = Authentication()

        resp = auth.fetch_user("usernotexisting")

        assert resp is None


class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        resp = authz.can({"username": "testuser"}, "create")

        assert resp is True

    def test_not_found(self):
        "agregar"
        authz = Authorization()

        resp = authz.can({"username": "usernotexisting"}, "create")

        assert resp is False

    def test_unathorized(self):
        "agregar"
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        resp = authz.can({"username": "testuser"}, "delete")

        assert resp is False


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


        assert Aer

if __name__ == '__main__':
    unittest.main()
