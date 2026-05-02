from playwright.sync_api import Playwright

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}


class APIUtils:

    def getToken(self, playwright: Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail":"rahulshetty@gmail.com", "userPassword": "Iamking@000"})
        assert response.ok
        responseBody = response.json()
        print("getToken = {}".format(responseBody))
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     },
                                            params={'id':12345})
        response_body = response.json()
        print("Create Order = {}".format(response_body))
        orderId = response_body["orders"][0]
        return orderId