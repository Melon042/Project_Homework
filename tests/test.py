import os
import sys
from src.widget import mask_account_card

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "accounts_cards_data.txt")


with open(file_path, "r", encoding="utf-8") as file:
    test_inputs = [line.strip() for line in file]


for input in test_inputs:
    print(mask_account_card(input))
