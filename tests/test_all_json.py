import unittest
import json
import os


class TestAllFilesAreJSON(unittest.TestCase):
    """
    Basic test to make sure that all the files inside the db directory end
    with the json extension and have valid json content
    """
    maxDiff = None

    def test_all_files_JSON(self):
        not_json = []

        for _file in os.listdir('db'):
            if not _file.endswith('.json'):
                not_json.append(_file)

        self.assertEqual(not_json, [])

    def test_all_files_JSON_content(self):
        not_json = []

        for _file in os.listdir('db'):
            try:
                json.loads(file(os.path.join('db', _file)).read())
            except:
                not_json.append(_file)

        self.assertEqual(not_json, [])
