from unittest import TestCase
from python_assignments.credit_card_validator2_OOPWise.credit_card_type import CreditCardType

from python_assignments.credit_card_validator2_OOPWise.credit_validator import CreditCard


class CreditCardValidatorTest(TestCase):

    def test_sum_of_the_doubled_second_digit_from_right_to_left_in_the_card_number(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_the_double_of_every_second_digit()

        self.assertEqual(37, credit_card.get_sum_of_doubled_digits())

    def test_sum_of_all_digits_in_the_odd_places_from_right_to_left_in_the_card_number(self):
        credit_card: CreditCard = CreditCard("4388576018402626")
        credit_card.sum_digits_in_odd_places()

        self.assertEqual(38, credit_card.get_sum_of_odd_digits())

    def test_invalid_card_number_length_raises_exception(self):
        credit_card: CreditCard = CreditCard("4388576018404567876562626")

        with self.assertRaises(ValueError):
            credit_card.validate_card_number_length()

    def test_credit_card_validity(self):
        credit_card: CreditCard = CreditCard("4388576018404567876562626")

        self.assertTrue(credit_card.is_valid())

    def test_credit_card_can_be_of_4_types_basis_the_first_digit_of_the_card_number(self):
        credit_card: CreditCard = CreditCard("4388576018410707")
        credit_card.set_card_type()

        self.assertEqual(CreditCardType.VISA_CARD, credit_card.get_card_type())

    def test_string_representation_of_the_validity_of_the_credit_card(self):
        credit_card: CreditCard = CreditCard("5591130100773414")
        credit_card.validate_card_number_length()
        credit_card.sum_digits_in_odd_places()
        credit_card.sum_the_double_of_every_second_digit()
        credit_card.set_card_type()
        expected: str = """        
        ****************************************
        **Credit Card Type: MASTER_CARD
        **Credit Card Number: 5591130100773414
        **Credit Card Digit Length: 16
        **Credit Card Validity Status: Valid
        ****************************************
        """
        self.assertEqual(expected, credit_card.__str__())
