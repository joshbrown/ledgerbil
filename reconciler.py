#!/usr/bin/python

from __future__ import division
from __future__ import print_function

from datetime import date
from dateutil.relativedelta import relativedelta


__author__ = 'Scott Carpenter'
__license__ = 'gpl v3 or greater'
__email__ = 'scottc@movingtofreedom.org'


class Reconciler(object):

    def __init__(self, ledgerfile, account):
        self.ledgerfile = ledgerfile
        self.account = account

    def run(self):

        count = 0
        for thing in self.ledgerfile.get_things():
            if not thing.rec_account_matches \
                    or thing.thing_date > date.today() + relativedelta(days=4) \
                    or thing.rec_status == '*':

                continue
            count += 1
            print(
                '{number:-4}. {date} {code:>7} {payee} '
                '{amount} {status:1}  |{number:-4} '
                '{thing_num:-6}'.format(
                    number=count,
                    date=thing.get_date_string(),
                    code=thing.transaction_code,
                    payee=get_colored_payee(thing.payee),
                    amount=get_colored_amount(thing.rec_amount),
                    status=thing.rec_status,
                    thing_num=thing.thing_number
                )
            )


def get_colored_amount(amount):
    if amount < 0:
        color = '\033[0;31m'  # red
    else:
        color = '\033[0;32m'  # green

    return '{start}${amount:10.2f}{end}'.format(
        start=color,
        amount=amount,
        end='\033[0m'
    )


def get_colored_payee(text):
    # cyan
    return '{start}{payee:40}{end}'.format(
        start='\033[0;36m',
        payee=text,
        end='\033[0m'
    )