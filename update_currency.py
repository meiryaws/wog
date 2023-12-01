import os
import os.path as op
import urllib.request
from datetime import date
from currency_converter import ECB_URL, CurrencyConverter
def UpdateCurrency():
    filename = f"ecb_{date.today():%Y%m%d}.zip"
    if not op.isfile(filename):
        urllib.request.urlretrieve(ECB_URL, filename)
    c = CurrencyConverter(filename)
    os.remove (filename)
    return c
