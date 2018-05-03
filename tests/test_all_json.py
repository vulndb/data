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

        for language in os.listdir('db'):
            for _file in os.listdir('db/%s' % language):
                if os.path.isfile(_file) and not _file.endswith('.json'):
                    not_json.append(_file)

        self.assertEqual([], not_json)

    def test_all_files_JSON_content(self):
        not_json = []

        for language in os.listdir('db'):
            for _file in os.listdir('db/%s' % language):
                if not os.path.isfile(_file):
                    continue

                try:
                    json.loads(file(os.path.join('db', language, _file)).read())
                except:
                    not_json.append(_file)

        self.assertEqual([], not_json)
