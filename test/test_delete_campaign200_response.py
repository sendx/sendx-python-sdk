# coding: utf-8

"""
    SendX REST API

    # Introduction The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sendx_python_sdk.models.delete_campaign200_response import DeleteCampaign200Response

class TestDeleteCampaign200Response(unittest.TestCase):
    """DeleteCampaign200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteCampaign200Response:
        """Test DeleteCampaign200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteCampaign200Response`
        """
        model = DeleteCampaign200Response()
        if include_optional:
            return DeleteCampaign200Response(
                id = 56,
                message = ''
            )
        else:
            return DeleteCampaign200Response(
        )
        """

    def testDeleteCampaign200Response(self):
        """Test DeleteCampaign200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
