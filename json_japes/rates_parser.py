import json

class RatesParser:
    def __init__(self, rates_filepath):
        rates_info = self._open_json_file(rates_filepath)
        self.base = rates_info["base"]
        self.date = rates_info["date"]
        self.rates = rates_info["rates"]
        self.aud = self.rates["AUD"]
        self.gbp = self.rates["GBP"]
        self.usd = self.rates["USD"]

    def _open_json_file(self, filepath) -> dict:
        with open(filepath) as rates:
            return json.load(rates)

rp = RatesParser('exchange_rates.json')
# rates_info = (rp._open_json_file("exchange_rates.json"))
# print(rates_info)
# print(rates_info["rates"]["AUD"])

print(rp.gbp)
