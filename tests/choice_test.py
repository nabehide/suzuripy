import json
import pytest
from SuzuriTest import SuzuriTest

global createdChoiceId


class TestClass(SuzuriTest):

    @pytest.mark.parametrize('choiceId', [
        (15402),
    ])
    def test_getChoice(self, client, choiceId):
        r = client.getChoice(choiceId)
        assert r.status_code == 200

    @pytest.mark.parametrize('title, description, bannerUrl, choiceProducts', [
        (
            "choice test",
            "猫の商品を沢山集めてみました。",
            ("https://dp3obxrw75ln8.cloudfront.net/choices/"
             "banners/7.jpg?1415260246"),
            [
                {
                    "productId": 2737748,
                    "itemVariantId": 1,
                },
            ],
        )
    ])
    def test_createChoice(
            self, client, title, description, bannerUrl, choiceProducts):
        global createdChoiceId
        r = client.createChoice(title, description, bannerUrl, choiceProducts)
        createdChoiceId = json.loads(r.text)["choice"]["id"]
        assert r.status_code == 200

    @pytest.mark.parametrize('productId, itemVariantId', [
        (1289301, 2),
    ])
    def test_addProductToChoice(
            self, client, productId, itemVariantId):
        global createdChoiceId
        r = client.addProductToChoice(
            createdChoiceId, productId, itemVariantId)  # NOQA
        assert r.status_code == 200

    @pytest.mark.parametrize('productId, itemVariantId', [
        (1289301, 2),
    ])
    def test_removeProductFromChoice(
            self, client, productId, itemVariantId):
        global createdChoiceId
        r = client.removeProductFromChoice(
            createdChoiceId, productId, itemVariantId)  # NOQA
        assert r.status_code == 200

    @pytest.mark.parametrize(
        'title, description, bannerUrl, choiceProducts', [
            (
                "スリスリピックアップ",
                "猫の商品を沢山あつめてみました。",
                ("https://dp3obxrw75ln8.cloudfront.net/choices/"
                 "banners/7.jpg?1415260246"),
                {
                    "productId": 1,
                    "itemVariantId": 1,
                },
            ),
        ]
    )
    def test_updateChoice(
            self, client, title, description, bannerUrl, choiceProducts):
        global createdChoiceId
        r = client.updateChoice(
            createdChoiceId, title, description, bannerUrl,  # NOQA
            choiceProducts)
        assert r.status_code == 200

    def test_deleteChoice(self, client):
        global createdChoiceId
        r = client.deleteChoice(createdChoiceId)  # NOQA
        assert r.status_code == 204

    @pytest.mark.parametrize('limit, offset, userId, userName', [
        (10, 0, None, None),
    ])
    def test_getChoiceList(self, client, limit, offset, userId, userName):
        r = client.getChoiceList(limit, offset, userId, userName)
        assert r.status_code == 200
