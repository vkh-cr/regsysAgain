
import datetime
import urllib.request
import json

from .models import Payment
from secret.bank_api_token import TOKEN

BANK_URL = 'https://www.fio.cz/ib_api/rest/periods/%s/2018-08-25/2018-08-31/transactions.json' % TOKEN

def download_statement_json():
    # TODO try in 30 secs again on http exception
    with urllib.request.urlopen(BANK_URL) as response:
        return response.read()

def json_to_payments(json_str):
    j = json.loads(json_str)
    transactions = j['accountStatement']['transactionList']['transaction']
    return map(json_to_one_payment, transactions)

def json_to_one_payment(j):
    d = json_to_dict(j)
    # TODO check for presence of fields
    return Payment(
        d['Datum'],
        d['Objem'],
        d['Protiúčet'],
        d['Kód banky'],
        d['Název protiúčtu'],
        d['VS'],
        d['SS'],
        j
    )

def json_to_dict(transaction):
    # TODO convert to dict eg { 'colName': 'colValue', ... }

def process_payment(payment):
    # TODO code this
    # find registration
    # if none
    #    error
    #    exit
    #
    # if reg.status is waiting for payment:
    #      change status
    #      send email
    #      exit
    #
    # error
