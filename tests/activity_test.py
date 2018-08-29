import pytest
from SuzuriTest import SuzuriTest


class TestClass(SuzuriTest):

    @pytest.mark.parametrize('limit', [
        (10),
    ])
    def test_getActivities(self, client, limit):
        r = client.getActivities(limit)
        assert r.status_code == 200

    def test_getUnreads(self, client):
        r = client.getUnreads()
        return r.status_code == 200
