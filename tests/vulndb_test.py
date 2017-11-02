import unittest
import os
import json

from vulndb import DBVuln


class VulnDBTest(unittest.TestCase):
    maxDiff = None

    def get_all_json(self):
        for _file in os.listdir('db'):
            if _file.endswith('.json'):
                yield _file, json.loads(file(os.path.join('db', _file)).read())

    def _get_file(self, file_type, file_ref):
        file_id = file_ref.split('/')[-1]
        with open(os.path.join(DBVuln.DB_PATH, file_type, file_id+'.md')) as ifile:
            data = ifile.read()
        return data

    def get_description(self, desc_ref):
        return self._get_file('description', desc_ref)

    def get_fix(self, fix_ref):
        return self._get_file('fix', fix_ref)

    def to_string(self, data):
        if isinstance(data, basestring):
            return data
        else:
            return ' '.join(data)

    def setUp(self):
        DBVuln.DB_PATH = 'db'

