import pytest
from SuzuriTest import SuzuriTest


class TestClass(SuzuriTest):

    def test_getProductList(self, client):
        r = client.getProductList()
        assert r.status_code == 200

    @pytest.mark.parametrize('limit, offset, q, itemId', [
        (30, 100, "NINJYA", 1),
    ])
    def test_searchProduct(self, client, limit, offset, q, itemId):
        r = client.searchProduct(limit, offset, q, itemId)
        assert r.status_code == 200

    @pytest.mark.parametrize('productId', [
        (2737748),
    ])
    def test_getProduct(self, client, productId):
        r = client.getProduct(productId)
        assert r.status_code == 200
