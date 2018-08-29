from SuzuriTest import SuzuriTest


class TestClass(SuzuriTest):

    def test_getItemList(self, client):
        r = client.getItemList()
        assert r.status_code == 200
