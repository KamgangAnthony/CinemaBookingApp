import sqlite3

from PdfReport import PdfReport


class User:

    TAKEN_VALUE = 1

    def __init__(self, full_name, seat_number, card_type, card_number, card_cvc,
                 cardholder_name):
        self.cardholder_name = cardholder_name
        self.card_cvc = card_cvc
        self.card_number = card_number
        self.card_type = card_type
        self.seat_number = seat_number
        self.full_name = full_name



    def is_your_seat_taken(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        values = (self.seat_number,)
        cursor.execute("""
        SELECT "taken" FROM "Seat"
        WHERE "seat_id" = ?
        """, values)
        result = cursor.fetchall()
        if not result:
            return True

        result = result[0][0]
        connection.close()
        if result == 1:
            return True
        else:
            return False

    def are_your_banking_details_correct(self):
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        values = (self.cardholder_name, self.card_cvc, self.card_number, self.card_type)
        cursor.execute("""
        SELECT * FROM "Card"
        WHERE holder = ? AND cvc = ? AND number = ? AND type = ?
        """, values)
        result = cursor.fetchall()
        connection.close()
        if len(result) > 0:
            return True
        else:
            return False

    def get_price_of_seat(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        values = (self.seat_number,)
        cursor.execute("""
        SELECT "price" FROM "Seat"
        WHERE "seat_id" = ?
        """, values)
        result = cursor.fetchall()
        result = result[0][0]
        connection.close()
        return result

    def _deduct_price_from_balance(self):
        price = self.get_price_of_seat()
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        values = (self.card_number,)
        cursor.execute("""
                SELECT "balance" FROM "Card"
                WHERE "number" = ?
                """, values)
        balance = cursor.fetchall()
        balance = balance[0][0]
        balance_minus_price = balance - price
        connection.close()
        return balance_minus_price

    def update_balance_from_price_of_seat(self):
        new_balance = self._deduct_price_from_balance()
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        values = (new_balance, self.card_number)
        cursor.execute("""
        UPDATE "Card" SET "balance" = ? WHERE "number" = ?
        """, values)
        connection.commit()
        connection.close()

    def update_taken_value(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        values = (User.TAKEN_VALUE, self.seat_number)
        cursor.execute("""
                UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?
                """, values)
        connection.commit()
        connection.close()

while True:
    # first_user = User("Marry Smith", "B1", "Master Card", "23456789", "234", "Marry Smith")
    # first_user.update_balance_from_price_of_seat()
    # print(ans, type(ans))
    full_name = input("Your full name: ")
    seat_number = input("Preferred seat number: ")
    card_type = input("Your card type: ")
    card_number = input("Your card number: ")
    card_cvc = input("Your card cvc: ")
    cardholder_name = input("Card holder name: ")
    first_user = User(full_name, seat_number, card_type, card_number, card_cvc, cardholder_name)
    our_pdf_report = PdfReport()

    if(first_user.is_your_seat_taken()):
        print("Seat is taken!")
        break

    elif(not first_user.are_your_banking_details_correct()):
        print("There was a problem with your card!")
        break

    else:
        first_user.update_balance_from_price_of_seat()
        first_user.update_taken_value()
        our_pdf_report.generate(first_user)
        print("Purchase successful!")
        break