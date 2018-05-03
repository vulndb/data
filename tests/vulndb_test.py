import os
import json
import unittest


class VulnDBTest(unittest.TestCase):
    maxDiff = None

    def get_all_json(self):
        for language in os.listdir('db'):
            for _file in os.listdir('db/%s' % language):
                if not _file.endswith('.json'):
                    continue

                file_name = os.path.join('db', language, _file)
                fp = file(file_name)
                data = json.loads(fp.read())

                yield language, file_name, data

    def get_all_languages(self):
        return os.listdir('db')

    def get_file_from_ref(self, language, file_type, file_ref):
        file_id = file_ref.split('/')[-1]

        with open(os.path.join('db', language, file_type, '%s.md' % file_id)) as ifile:
            data = ifile.read()

        return data

    def get_description(self, language, desc_ref):
        return self.get_file_from_ref(language, 'description', desc_ref)

    def get_fix(self, language, fix_ref):
        return self.get_file_from_ref(language, 'fix', fix_ref)
