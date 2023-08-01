from services.database import DatabaseUsers

class Curr_converter:

    def __init__(self):
        self.database = DatabaseUsers()

    def convert_usd_to_byn(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        return amount * usd_rate

    def convert_usd_to_eur(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        eur_rate = self.database.get_previous_rate('EUR')
        return amount * (usd_rate / eur_rate)

    def convert_usd_to_rub(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        rub_rate = self.database.get_previous_rate('RUB')
        return amount * (usd_rate / (rub_rate / 100))

    def convert_eur_to_byn(self, amount):
        eur_rate = self.database.get_previous_rate('EUR')
        return amount * eur_rate

    def convert_eur_to_usd(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        eur_rate = self.database.get_previous_rate('EUR')
        return amount * (eur_rate / usd_rate)

    def convert_eur_to_rub(self, amount):
        eur_rate = self.database.get_previous_rate('EUR')
        rub_rate = self.database.get_previous_rate('RUB')
        return amount * (eur_rate / (rub_rate / 100))

    def convert_rub_to_byn(self, amount):
        rub_rate = self.database.get_previous_rate('RUB')
        return amount * (rub_rate / 100)

    def convert_rub_to_usd(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        rub_rate = self.database.get_previous_rate('RUB')
        return amount * ((rub_rate / 100) / usd_rate)

    def convert_rub_to_eur(self, amount):
        eur_rate = self.database.get_previous_rate('EUR')
        rub_rate = self.database.get_previous_rate('RUB')
        return amount * ((rub_rate / 100) / eur_rate)

    def convert_byn_to_usd(self, amount):
        usd_rate = self.database.get_previous_rate('USD')
        return amount / usd_rate

    def convert_byn_to_eur(self, amount):
        eur_rate = self.database.get_previous_rate('EUR')
        return amount / eur_rate

    def convert_byn_to_rub(self, amount):
        rub_rate = self.database.get_previous_rate('RUB')
        return amount / (rub_rate / 100)

    def convert(self, amount, from_currency, to_currency):
        currency_converter = {
            ('USD', 'BYN'): self.convert_usd_to_byn,
            ('USD', 'EUR'): self.convert_usd_to_eur,
            ('USD', 'RUB'): self.convert_usd_to_rub,
            ('EUR', 'BYN'): self.convert_eur_to_byn,
            ('EUR', 'USD'): self.convert_eur_to_usd,
            ('EUR', 'RUB'): self.convert_eur_to_rub,
            ('RUB', 'BYN'): self.convert_rub_to_byn,
            ('RUB', 'USD'): self.convert_rub_to_usd,
            ('RUB', 'EUR'): self.convert_rub_to_eur,
            ('BYN', 'USD'): self.convert_byn_to_usd,
            ('BYN', 'EUR'): self.convert_byn_to_eur,
            ('BYN', 'RUB'): self.convert_byn_to_rub,
        }

        conversion_function = currency_converter.get((from_currency, to_currency))
        if conversion_function:
            converted_amount = conversion_function(amount)
            return round(converted_amount, 2)
        else:
            return "Unknown conversion"
