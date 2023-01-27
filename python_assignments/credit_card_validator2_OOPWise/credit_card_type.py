from enum import Enum


class CreditCardType(Enum):
    VISA_CARD = "4"
    MASTER_CARD = "5"
    AMERICAN_EXPRESS_CARD = "37"
    DISCOVER_CARD = "6"

    # def __init__(self, content: str):
    #     self.content = content

    # def generate_card_type(self, card_number: str):
    #     for self.value in CreditCardType:
    #         if card_number.__getitem__(0) == self.value.content:
    #             return self.value
