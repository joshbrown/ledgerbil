#!/usr/bin/python

"""supports unit testing by capturing streams"""

from unittest import TestCase
import sys

# noinspection PyCompatibility
from StringIO import StringIO


__author__ = 'Scott Carpenter'
__license__ = 'gpl v3 or greater'
__email__ = 'scottc@movingtofreedom.org'


class Redirector(TestCase):

    def setUp(self):
        super(Redirector, self).setUp()
        self.savestdout = sys.stdout
        self.redirect = StringIO()
        sys.stdout = self.redirect

        self.savestderr = sys.stderr
        self.redirecterr = StringIO()
        sys.stderr = self.redirecterr

    def tearDown(self):
        self.redirect.close()
        sys.stdout = self.savestdout

        self.redirecterr.close()
        sys.stderr = self.savestderr
