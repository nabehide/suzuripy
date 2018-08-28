import json
import requests


class SuzuriClient():

    mainURL = "https://suzuri.jp/api/v1/"

    def __init__(self, key):
        self.getHeaders = {"Authorization": "Bearer " + key}
        self.headers = self.getHeaders
        self.headers["Content-Type"] = "application/json"

    def getActivities(self, limit=10):
        payloads = {'limit': limit}
        return self._get("activities", payloads)

    def getUnreads(self):
        return self._get("activities/unreads")

    def getChoice(self, choiceID):
        return self._get("choices/" + str(choiceID))

    def createChoice(
            self, title, description=None,
            bannerUrl=None, choiceProducts=None):

        data = self._makeDict(
            locals(), title, description, bannerUrl, choiceProducts)
        return self._post("choices", data)

    def deleteChoice(self, choiceId):
        return self._delete("choices/" + str(choiceId))

    def addProductToChoice(self, choiceId, productId=None, itemVariantId=None):
        data = self._makeDict(locals(), choiceId, productId, itemVariantId)
        return self._post("choices/" + str(choiceId), data)

    def removeProductFromChoice(
            self, choiceId, productId=None, itemVariantId=None):
        data = self._makeDict(locals(), choiceId, productId, itemVariantId)
        return self._post("choices/" + str(choiceId) + "/remove", data)

    def updateChoice(
            self, choiceId, title=None, description=None, bannerUrl=None,
            choiceProducts=None):
        data = self._makeDict(
            locals(), choiceId, title, description, bannerUrl)
        return self._put("choices/" + str(choiceId), data)

    def getChoiceList(
            self, limit=None, offset=None, userId=None, userName=None):
        payloads = self._makeDict(locals(), limit, offset, userId, userName)
        return self._get("choices", payloads)

    def getFavoriteOfProduct(
            self, productId, itemId=None, limit=None, offset=None):
        payloads = self._makeDict(locals(), productId, itemId, limit, offset)
        return self._get("products/" + str(productId) + "/favorites", payloads)

    def getFavoriteOfUser(self, userId):
        payloads = self._makeDict(locals(), userId)
        return self._get("users/" + str(userId) + "/favorites", payloads)

    def createFavoriteToProduct(self, productId, annonymouse):
        data = self._makeDict(locals(), productId, annonymouse)
        return self._post("products/" + str(productId) + "/favorites", data)

    def getItemList(self):
        return self._get("items")

    def getMaterialList(self, limit=None, offset=None, userId=None):
        payloads = self._makeDict(locals(), limit, offset, userId)
        return self._get("materials", payloads)

    def createMaterial(
            self, texture, title, price=None, description=None, products=None):
        data = self._makeDict(
            locals(), texture, title, price, description, products)
        return self._post("materials", data)

    def updateMaterial(
            self, materialId, title=None, price=None, description=None,
            products=None):
        data = self._makeDict(
            locals(), materialId, title, price, description, products)
        return self._put("materials/" + str(materialId), data)

    def deleteMaterial(self, materialId):
        return self._delete("materials/" + str(materialId))

    # def createMaterialText(self, text, itemVariantId=None):
    #     data = self._makeDict(locals(), text, itemVariantId)
    #     return self._post("materials/text", data)

    def getProductList(self):
        return self._get("products")

    def searchProduct(self, limit=None, offset=None, q=None, itemId=None):
        payloads = self._makeDict(locals(), limit, offset, q, itemId)
        return self._get("products/search", payloads)

    def getProduct(self, productId):
        return self._get("products/" + str(productId))

    def getUserList(self, name=None, limit=None, offset=None):
        payloads = self._makeDict(locals(), name, limit, offset)
        return self._get("users", payloads)

    def getUser(self, userId):
        return self._get("users/" + str(userId))

    def getUserSelf(self):
        return self._get("user")

    def updateUserSelf(self):
        data = {}
        return self._put("user", data)

    def _makeDict(self, variableNames, *args):
        d = {}
        for item in args:
            if item is not None:
                for i in variableNames.keys():
                    if id(variableNames[i]) == id(item):
                        key = i
                        break
                d[key] = item
        return d

    def _get(self, endpoint, payloads=None):
        return requests.get(
            self.mainURL + endpoint,
            params=json.dumps(payloads),
            headers=self.getHeaders,
        )

    def _post(self, endpoint, data):
        return requests.post(
            self.mainURL + endpoint,
            data=json.dumps(data),
            headers=self.headers,
        )

    def _put(self, endpoint, data):
        return requests.put(
            self.mainURL + endpoint,
            data=json.dumps(data),
            headers=self.headers,
        )

    def _delete(self, endpoint):
        return requests.delete(
            self.mainURL + endpoint,
            headers=self.headers,
        )
