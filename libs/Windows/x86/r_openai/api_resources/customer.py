from r_openai.openai_object import OpenAIObject


class Customer(OpenAIObject):
    @classmethod
    def get_url(self, customer, endpoint):
        return f"/customer/{customer}/{endpoint}"

    @classmethod
    def create(cls, customer, endpoint, **params):
        instance = cls()
        return instance.request("post", cls.get_url(customer, endpoint), params)
