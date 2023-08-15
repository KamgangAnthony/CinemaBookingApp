# CinemaBookingApp
This Cinema Booking App allows users to book cinema seats by providing their personal and banking details. The app is connected to two database files: banking.db and cinema.db. Upon successful booking, a PDF file is generated containing the user's name, a random ticket ID, the price, and the seat number.

## A Cinema Booking App - README

### Overview

A Cinema Booking App is an application that allows users to book cinema seats by providing their personal and banking details. The app is connected to two database files: `banking.db` and `cinema.db`. Upon successful booking, a PDF file is generated containing the user's name, a random ticket ID, the price, and the seat number.

### Objects

- **User**
  - Attributes: `full_name`, `seat_number`, `card_type`, `card_number`, `card_cvc`, `cardholder_name`
  - Methods: `is_seat_taken()`, `are_banking_details_correct()`, `get_price_of_seat()`, `_deduct_price_from_balance()`, `update_balance_from_price_of_seat()`, `update_taken_value()`

- **PdfReport**
  - Attributes: N/A
  - Methods: `generate(User user)`

### Description

The app takes in the full name of the user, their preferred seat number, card type, card number, card CVC, and cardholder name. It is connected to two database files:

1. `banking.db` with columns: `type`, `number`, `cvc`, `holder`, `balance`
2. `cinema.db` with columns: `seat_id`, `taken`, `price`

When the user submits their information, the program checks if the seat is available and if the banking details are correct. If the purchase is successful, a sample PDF file called "sample.pdf" is generated with the following information:

- Title: "Your Digital Ticket"
- Name: The user's name
- Ticket ID: A random string of 8 letters
- Price: The price of the seat
- Seat Number: The seat number

The program checks the price for the selected seat in the `cinema.db` file and deducts it from the balance of the card in the `banking.db` file. Then, it updates the 'taken' value for that seat to 1 in the `cinema.db` file.

If the user inputs a seat that is already taken, the program displays "seat is taken!" and no money is deducted from the balance.

If the user inputs a card number, card type, card CVC, or cardholder name that is not in the `banking.db` file, the program outputs: "There was a problem with your card!"

### Database Explanation

The app uses two SQLite databases:

1. `banking.db`: Stores the user's banking details, including card type, card number, card CVC, cardholder name, and balance.
2. `cinema.db`: Stores the cinema seat information, including seat ID, whether the seat is taken, and the price of the seat.

### User Object

The User object contains the user's personal and banking information. It has several methods to check if the seat is taken, verify banking details, get the price of the seat, deduct the price from the balance, update the balance, and update the 'taken' value for the seat.

### PDF Report Object

The PdfReport object is responsible for generating a PDF file with the user's booking information. It has a `generate(User user)` method that takes a User object as input and creates a PDF file with the user's name, a random ticket ID, the price, and the seat number.

### App Description

The Cinema Booking App is designed to provide a seamless booking experience for users. They can input their personal and banking details, and the app will check if the seat is available and if the banking details are correct. If the purchase is successful, a PDF file containing the user's booking information is generated. The app ensures that users can only book available seats and that their banking details are accurate before processing the transaction.
