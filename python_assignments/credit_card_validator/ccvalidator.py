import enum

from python_assignments.credit_card_validator.credit_card_type import CreditCardType


class CCValidator:
    credit_card_type: CreditCardType
    credit_card_number: str
    credit_card_number_in_list = []
    credit_card_digit_length: int
    credit_card_status: str

    def confirm_validity(self, card_number: str):
        try:
            self.__validate(card_number)
        except ValueError:
            print("The length of your card number should be between 13 and 16")
        else:
            self.credit_card_number = card_number
            self.credit_card_digit_length = len(card_number)
            self.set_credit_card_number_in_list(self, card_number)
            self.__set_credit_card_type(self)
            self.__check_validity(self, self.__add_doubled_second_digit(self), self.__add_digits_in_odd_places(self))

    @staticmethod
    def __validate(card_number: str):
        if len(card_number) < 13 or len(card_number) > 16:
            raise ValueError

    def __add_doubled_second_digit(self):
        total = 0
        for i in range(len(self.credit_card_number) - 2, -1, -2):
            num = int(self.credit_card_number_in_list[i])
            num = (num * 2) % 9
            self.credit_card_number_in_list[i] = num
            total += num
        return total

    def set_credit_card_number_in_list(self, card_number):
        for i in range(self.credit_card_digit_length):
            self.credit_card_number_in_list.append(int (card_number.__getitem__(i)))

    def __add_digits_in_odd_places(self):
        total = 0
        for i in range(self.credit_card_digit_length -1, -1, -2):
            total += int (self.credit_card_number_in_list[i])
        return total

    def __set_credit_card_type(self):
        if self.credit_card_number_in_list[0] == 4:
            self.credit_card_type = CreditCardType.VISACARDS
        elif self.credit_card_number_in_list[0] == 5:
            self.credit_card_type = CreditCardType.MASTERCARDS
        elif self.credit_card_number_in_list[0] == 3 and self.credit_card_number_in_list[1] == 7:
            self.credit_card_type = CreditCardType.AMERICANEXPRESSCARD
        elif self.credit_card_number_in_list[0] == 6:
            self.credit_card_type = CreditCardType.DISCOVERCARDS

    def __check_validity(self, first_number: int, second_number: int):
        result = first_number + second_number
        if result % 10 == 0:
            self.credit_card_status = "Valid"
        else:
            self.credit_card_status = "Invalid"
        self.__display_result(self)

    def __display_result(self):
        print(f"""
        ************************************************************
        {'**Credit Card Type: ' + str (self.credit_card_type.name)}
        {'**Credit Card Number: ' + self.credit_card_number}
        {'**Credit Card Digit Length: '+ str(self.credit_card_digit_length)}
        {'**Credit Card Validity Status: '+ self.credit_card_status}
        ************************************************************
                        """)
