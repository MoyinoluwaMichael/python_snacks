from python_assignments.credit_card_validator2_OOPWise.credit_card_type import CreditCardType


class CreditCard:

    def __init__(self, card_number: str):
        self.__card_number: str = card_number
        self.__sum_of_doubled_digits: int = 0
        self.__sum_of_odd_digits: int = 0
        self.__card_type: CreditCardType = None

    def sum_the_double_of_every_second_digit(self) -> None:
        result: int = 0
        for digit in range(len(self.__card_number) - 2, -1, -2):
            result = int(self.__card_number.__getitem__(digit)) * 2
            if result > 9:
                result -= 9
            self.__sum_of_doubled_digits += result

    def get_sum_of_doubled_digits(self) -> int:
        return self.__sum_of_doubled_digits

    def sum_digits_in_odd_places(self) -> None:
        for digit in range(len(self.__card_number) - 1, -1, -2):
            self.__sum_of_odd_digits += int(self.__card_number.__getitem__(digit))

    def get_sum_of_odd_digits(self) -> int:
        return self.__sum_of_odd_digits

    def validate_card_number_length(self) -> None:
        if len(self.__card_number) < 13 or len(self.__card_number) > 16:
            raise ValueError

    def is_valid(self) -> bool:
        print(self.__sum_of_doubled_digits + self.__sum_of_odd_digits)
        if (self.__sum_of_doubled_digits + self.__sum_of_odd_digits) % 10 == 0:
            return True
        else:
            return False

    def set_card_type(self) -> None:
        first_digit: str = self.__card_number.__getitem__(0)
        if first_digit == "4":
            self.__card_type = CreditCardType.VISA_CARD
        elif first_digit == "5":
            self.__card_type = CreditCardType.MASTER_CARD
        elif first_digit == "6":
            self.__card_type = CreditCardType.DISCOVER_CARD
        elif first_digit == "3" and self.__card_number.__getitem__(1) == "7":
            self.__card_type = CreditCardType.AMERICAN_EXPRESS_CARD

    def get_card_type(self) -> CreditCardType:
        return self.__card_type

    def __str__(self) -> str:
        status: str = ""
        if self.is_valid():
            status = "Valid"
        else:
            status = "Invalid"
        return f"""        
        ****************************************
        **Credit Card Type: {self.__card_type.name}
        **Credit Card Number: {self.__card_number}
        **Credit Card Digit Length: {len(self.__card_number)}
        **Credit Card Validity Status: {status}
        ****************************************
        """
