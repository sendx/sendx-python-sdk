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

from sendx_python_sdk.api.getting_started_api import GettingStartedApi


class TestGettingStartedApi(unittest.TestCase):
    """GettingStartedApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GettingStartedApi()

    def tearDown(self) -> None:
        pass

    def test_identify_contact(self) -> None:
        """Test case for identify_contact

        Identify contact
        """
        pass

    def test_tracking_contact(self) -> None:
        """Test case for tracking_contact

        Add Tracking info
        """
        pass


if __name__ == '__main__':
    unittest.main()
