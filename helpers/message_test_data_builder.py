__author__ = 'anton.skomarovskyi@gmail.com'


class MessageTestDataBuilder:

    def __init__(self):
        self.__msg_test_data = {}

    def with_type(self, message_type):
        """
        :type message_type: MessageType
        """
        self.__msg_test_data['type'] = message_type

        return self

    def with_name(self, name):
        self.__msg_test_data['name'] = name

        return self

    def with_email(self, email):
        self.__msg_test_data['mail'] = email

        return self

    def with_body(self, body):
        self.__msg_test_data['body'] = body

        return self

    def with_product(self, product):
        self.__msg_test_data['product'] = product

        return self

    def with_country_code2(self, country_code2):
        self.__msg_test_data['countryCode2'] = country_code2

        return self

    def with_lang(self, lang):
        self.__msg_test_data['lang'] = lang

        return self

    def with_not_valid_signature(self):
        # TODO: implement logic
        print("Have not implemented yet")

        return self

    def with_not_valid_email(self):
        # TODO: implement logic
        print("Have not implemented yet")

        return self

    def with_not_valid_body(self):
        # TODO: implement logic
        print("Have not implemented yet")

        return self

    def build(self):
        if len(self.__msg_test_data) != 0:
            # TODO: implement default logic of fields filling
            pass

        return self.__msg_test_data

class MessageType:
    MESSAGE = 'message'
    FEEDBACK = 'feedback'

class ProductType:
    SOFT_1 = 'soft1'
    SOFT_2 = 'soft2'
    SOFT_3 = 'soft3'
