import unittest
import os
import json

from vulndb import DBVuln


class VulnDBTest(unittest.TestCase):
    maxDiff = None

    def get_all_json(self):
        for _file in os.listdir('db'):
            yield _file, json.loads(file(os.path.join('db', _file)).read())

    def to_string(self, data):
        if isinstance(data, basestring):
            return data
        else:
            return ' '.join(data)

    def setUp(self):
        DBVuln.DB_PATH = 'db'

