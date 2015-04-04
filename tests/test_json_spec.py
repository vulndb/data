import requests
import json
import os

from vulndb import DBVuln
from tests.vulndb_test import VulnDBTest

SEVERITIES = {'high', 'medium', 'low', 'informational'}


class TestAllFilesHaveValidSpec(VulnDBTest):

    def url_is_404(self, session, url):
        try:
            response = session.get(url)
        except KeyboardInterrupt:
            raise
        except:
            return True
        else:
            return response.status_code == 404

    def test_severity(self):
        invalid = []

        for _file, db_data in self.get_all_json():
            if db_data['severity'] not in SEVERITIES:
                invalid.append((_file, db_data['severity']))

        self.assertEqual(invalid, [])

    def test_lengths(self):
        invalid = []

        for _file, db_data in self.get_all_json():
            description = self.to_string(db_data['description'])
            if len(description) <= 30:
                invalid.append(_file)

            guidance = self.to_string(db_data['fix']['guidance'])
            if len(guidance) <= 30:
                invalid.append(_file)

        self.assertEqual(invalid, [])

    def test_url_is_not_404(self):
        all_urls = set()
        invalid = []

        for vuln_id in DBVuln.get_all_db_ids():
            db_vuln = DBVuln.from_id(vuln_id)

            if db_vuln.wasc:
                for wasc_id in db_vuln.wasc:
                    all_urls.add(db_vuln.get_wasc_url(wasc_id))

            if db_vuln.cwe:
                for cwe_id in db_vuln.cwe:
                    all_urls.add(db_vuln.get_cwe_url(cwe_id))

            for _, _, link in db_vuln.get_owasp_top_10_references():
                all_urls.add(link)

            for reference in db_vuln.references:
                all_urls.add(reference.url)

        session = requests.Session()
        for url in all_urls:
            if self.url_is_404(session, url):
                invalid.append(url)

        self.assertEqual(invalid, [])

    def test_id_match(self):
        invalid = []

        for vuln_id in DBVuln.get_all_db_ids():
            db_path_file = DBVuln.get_file_for_id(vuln_id)
            json_data = json.loads(file(db_path_file).read())
            json_id = json_data['id']

            db_file = os.path.split(db_path_file)[1]

            if not db_file.startswith('%s-' % json_id):
                invalid.append(db_file)

        self.assertEqual(invalid, [])

    def test_no_multiple_spaces(self):
        invalid = []

        for vuln_id in DBVuln.get_all_db_ids():
            db_vuln = DBVuln.from_id(vuln_id)

            if '  ' in db_vuln.fix_guidance:
                invalid.append((db_vuln.db_file, 'fix_guidance'))

            if '  ' in db_vuln.description:
                invalid.append((db_vuln.db_file, 'description'))

        self.assertEqual(invalid, [])
