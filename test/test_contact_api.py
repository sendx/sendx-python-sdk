# coding: utf-8

"""
    SendX REST API

    # Introduction The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sendx_python_sdk.api.contact_api import ContactApi


class TestContactApi(unittest.TestCase):
    """ContactApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContactApi()

    def tearDown(self) -> None:
        pass

    def test_create_contact(self) -> None:
        """Test case for create_contact

        Create a contact
        """
        pass

    def test_delete_contact(self) -> None:
        """Test case for delete_contact

        Delete Contact
        """
        pass

    def test_get_all_contacts(self) -> None:
        """Test case for get_all_contacts

        Get All Contacts
        """
        pass

    def test_get_contact_by_id(self) -> None:
        """Test case for get_contact_by_id

        Get Contact by ID
        """
        pass

    def test_unsubscribe_contact(self) -> None:
        """Test case for unsubscribe_contact

        Unsubscribe Contact
        """
        pass

    def test_update_contact(self) -> None:
        """Test case for update_contact

        Update Contact
        """
        pass


if __name__ == '__main__':
    unittest.main()
