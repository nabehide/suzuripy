import pytest  # NOQA
from SuzuriTest import SuzuriTest


class TestClass(SuzuriTest):

    @pytest.mark.parametrize('productId, limit, offset', [
        (2737748, 30, 100),
    ])
    def test_getFavoriteOfProduct(self, client, productId, limit, offset):
        r = client.getFavoriteOfProduct(productId, limit, offset)
        assert r.status_code == 200

    @pytest.mark.parametrize('userId', [
        (217290),
    ])
    def test_getFavoriteOfUser(self, client, userId):
        r = client.getFavoriteOfUser(userId)
        assert r.status_code == 200

    @pytest.mark.parametrize('productId, annonymouse', [
        (7, True),
    ])
    def test_createFavoriteToProduct(self, client, productId, annonymouse):
        r = client.createFavoriteToProduct(productId, annonymouse)
        assert r.status_code == 200
