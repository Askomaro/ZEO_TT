import json
from wheel.signatures import assertTrue

import requests

from helpers.message_test_data_builder import MessageTestDataBuilder, MessageType, ProductType


__author__ = 'anton.skomarovskyi@gmail.com'


class TestSendMessageToSupport:
    _SCHEMA = 'http://'
    _HOST = 'mkapistage.mackeeper.com'
    _URL_PATH = '/v1/sendMessageToSupport'

    def setup_method(self):
        self._url = "%s%s%s" % (self._SCHEMA, self._HOST, self._URL_PATH)

    def test_receives_status_code_0_if_operation_is_successful(self):
        # Filling with some valid data
        payload = MessageTestDataBuilder() \
            .with_body("") \
            .with_country_code2("") \
            .with_email("") \
            .with_lang("") \
            .with_name("") \
            .with_product(ProductType.SOFT_1) \
            .with_type(MessageType.FEEDBACK) \
            .build()

        sut = requests.post(self._url, payload)
        sut_response_json = json.loads(sut.text)

        assertTrue(sut_response_json['statusCode'] == 0,
                   'Expects to receive "0" status code.')

    def test_receives_status_code_1_if_operation_is_failed(self):
        payload = MessageTestDataBuilder() \
            .with_not_valid_signature() \
            .build()

        sut = requests.post(self._url, payload)
        sut_response_json = json.loads(sut.text)

        assertTrue(sut_response_json['statusCode'] == 1,
                   'Expects to receive "1" status code.')

    def test_receives_status_code_2_if_operation_is_failed(self):
        payload = MessageTestDataBuilder() \
            .with_not_valid_email() \
            .build()

        sut = requests.post(self._url, payload)
        sut_response_json = json.loads(sut.text)

        assertTrue(sut_response_json['statusCode'] == 2,
                   'Expects to receive "2" status code.')

    def test_receives_status_code_3_if_operation_is_failed(self):
        payload = MessageTestDataBuilder() \
            .with_not_valid_body() \
            .build()

        sut = requests.post(self._url, payload)
        sut_response_json = json.loads(sut.text)

        assertTrue(sut_response_json['statusCode'] == 3,
                   'Expects to receive "3" status code.')

    def test_receives_status_code_4_if_operation_is_failed(self):
        # Implement some logic here in order to being thrown 'sending message exception'
        payload = MessageTestDataBuilder().build()

        sut = requests.post(self._url, payload)
        sut_response_json = json.loads(sut.text)

        assertTrue(sut_response_json['statusCode'] == 4,
                   'Expects to receive "4" status code.')
