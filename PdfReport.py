import webbrowser
import os
from fpdf import FPDF
import random
import string


class PdfReport:
    """
    Creates a Pdf report file that contains data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def generate(self, user):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.jpg", w=30, h=30)

        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Name:", border=1)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=40, txt=user.cardholder_name, border=1, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Ticket ID:", border=1)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=40, txt=self._generate_random_string(8), border=1, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Price", border=1)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=40, txt=str(user.get_price_of_seat()), border=1, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Seat Number", border=1)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=40, txt=str(user.seat_number), border=1, ln=1)

        pdf.output("sample.pdf")

        webbrowser.open("sample.pdf")

    def _generate_random_string(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

#
# class FileSharer:
#
#     def __init__(self, filepath, api_key="Acf5ay8PdTnW8Ck8d2Piaz"):
#         self.filepath = filepath
#         self.api_key = api_key
#
#     def share(self):
#         client = Client(self.api_key)
#         new_filelink = client.upload(filepath = self.filepath)
#         return new_filelink.url
