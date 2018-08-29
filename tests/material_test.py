import json
import pytest  # NOQA
from SuzuriTest import SuzuriTest

global createdMaterialId


class TestClass(SuzuriTest):

    @pytest.mark.parametrize('limit, offset, userId', [
        (30, 100, 2),
    ])
    def test_getMaterialList(self, client, limit, offset, userId):
        r = client.getMaterialList(limit, offset, userId)
        assert r.status_code == 200

    @pytest.mark.parametrize('texture, title, price, description, products', [
        (
            "https://41.media.tumblr.com/QA9JpdgnOc8ov98s1C4S5EjJ_500.jpg",
            "test_title",
            100,
            "test_description",
            [
                {
                    "itemId": 1,
                    "exemplaryItemVariantId": 151,
                    "published": True,
                    "resizeMode": "contain",
                    # "sub_materials": [
                    #     {
                    #         "texture": ("https://41.media.tumblr.com/"
                    #                     "QA9JpdgnOc8ov98s1C4S5EjJ_500.jpg"),
                    #         "printSide": "back",
                    #         "enabled": True,
                    #     },
                    # ]
                },
            ]
        ),
    ])
    def test_createMaterial(
            self, client, texture, title, price, description, products):
        r = client.createMaterial(
            texture, title, price, description, products)
        global createdMaterialId
        createdMaterialId = json.loads(r.text)["material"]["id"]  # NOQA
        assert r.status_code == 200

    @pytest.mark.parametrize('title, price, description, products', [
        (
            "AAスリスリくん",
            100,
            "description_test",
            [
                {
                    "itemId": 1,
                    "exemplaryItemVariantId": 1,
                    "itemVariantId": 1,
                    "published": True,
                    "resizeMode": "contain",
                },
            ]
        ),
    ])
    def test_updateMaterial(
            self, client, title, price, description, products):
        global createdMaterialId
        r = client.updateMaterial(
            createdMaterialId, title, price, description, products)  # NOQA
        assert r.status_code == 200

    def test_deleteMaterial(self, client):
        global createdMaterialId
        r = client.deleteMaterial(createdMaterialId)  # NOQA
        assert r.status_code == 204
