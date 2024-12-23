# coding: utf-8

"""
    SendX REST API

    # Introduction SendX is an email marketing product. It helps you convert website visitors to customers, send them promotional emails, engage with them using drip sequences and craft custom journeys using powerful but simple automations. The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendx.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sendx_python_sdk.models.customfield_customfield_id_delete200_response import CustomfieldCustomfieldIdDelete200Response

class TestCustomfieldCustomfieldIdDelete200Response(unittest.TestCase):
    """CustomfieldCustomfieldIdDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomfieldCustomfieldIdDelete200Response:
        """Test CustomfieldCustomfieldIdDelete200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomfieldCustomfieldIdDelete200Response`
        """
        model = CustomfieldCustomfieldIdDelete200Response()
        if include_optional:
            return CustomfieldCustomfieldIdDelete200Response(
                message = 'Custom Field deleted successfully.'
            )
        else:
            return CustomfieldCustomfieldIdDelete200Response(
        )
        """

    def testCustomfieldCustomfieldIdDelete200Response(self):
        """Test CustomfieldCustomfieldIdDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()