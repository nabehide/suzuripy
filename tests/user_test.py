import pytest
from SuzuriTest import SuzuriTest


class TestClass(SuzuriTest):

    @pytest.mark.parametrize('name, limit, offset', [
        ("surisurikun", 30, 100),
    ])
    def test_getUserList(self, client, name, limit, offset):
        r = client.getUserList(name, limit, offset)
        assert r.status_code == 200

    @pytest.mark.parametrize('userId', [
        (217290),
    ])
    def test_getUser(self, client, userId):
        r = client.getUser(userId)
        assert r.status_code == 200

    def test_getUserSelf(self, client):
        r = client.getUserSelf()
        assert r.status_code == 200

    def test_updateUserSelf(self, client):
        r = client.updateUserSelf()
        assert r.status_code == 200
