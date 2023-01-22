
from python_assignments.credit_card_validator.credit_card_type import CreditCardType


class CcValidator:
    __credit_card_number: str
    __credit_card_number_in_list = []
    __credit_card_digit_length: int
    __credit_card_status: str
    __card_type: CreditCardType

    def confirm_validity(self, card_number: str):
        try:
            self.__validate(card_number)
        except ValueError:
            print("The length of your card number should be between 13 and 16")
        else:
            self.__credit_card_number = card_number
            self.__credit_card_digit_length = len(card_number)
            self.__set_card_number_in_list()
            self.__set_card_type()
            self.__check_validity(self.__add_doubled_second_digit(), self.__add_digits_in_odd_places())

    @staticmethod
    def __validate(card_number: str):
        if len(card_number) < 13 or len(card_number) > 16:
            raise ValueError

    def __add_doubled_second_digit(self):
        total = 0
        for i in range(len(self.__credit_card_number) - 2, -1, -2):
            num = int(self.__credit_card_number_in_list[i])
            num = (num * 2) % 9
            self.__credit_card_number_in_list[i] = num
            total += num
        return total

    def __set_card_number_in_list(self):
        for i in range(self.__credit_card_digit_length):
            self.__credit_card_number_in_list.append(int(self.__credit_card_number.__getitem__(i)))

    def __add_digits_in_odd_places(self):
        total = 0
        for i in range(self.__credit_card_digit_length - 1, -1, -2):
            total += int(self.__credit_card_number_in_list[i])
        return total

    def __set_card_type(self):
        if self.__credit_card_number_in_list[0] == 4:
            self.__card_type = CreditCardType.VISACARDS
        elif self.__credit_card_number_in_list[0] == 5:
            self.__card_type = CreditCardType.MASTERCARDS
        elif self.__credit_card_number_in_list[0] == 3 and self.__credit_card_number_in_list[1] == 7:
            self.__card_type = CreditCardType.AMERICANEXPRESSCARD
        elif self.__credit_card_number_in_list[0] == 6:
            self.__card_type = CreditCardType.DISCOVERCARDS

    def __check_validity(self, first_number: int, second_number: int):
        result = first_number + second_number
        if result % 10 == 0:
            self.credit_card_status = "Valid"
        else:
            self.credit_card_status = "Invalid"
        self.__display_result()

    def __display_result(self):
        print(f"""
        ****************************************************
        **Credit Card Type: {self.__card_type.name}
        **Credit Card Number: {self.__credit_card_number}
        **Credit Card Digit Length: {str(self.__credit_card_digit_length)}
        **Credit Card Validity Status: {self.credit_card_status}
        ****************************************************
                        """)
