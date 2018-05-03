import requests
import os

from tests.vulndb_test import VulnDBTest
from nose.plugins.attrib import attr
from vulndb import DBVuln
from vulndb.constants.owasp import OWASP_TOP10_2010_URL_FMT, OWASP_TOP10_2013_URL_FMT

SEVERITIES = {'high', 'medium', 'low', 'informational'}


class TestAllFilesHaveValidSpec(VulnDBTest):

    def test_severity(self):
        invalid = []

        for language, _file, db_data in self.get_all_json():
            if db_data['severity'] not in SEVERITIES:
                invalid.append((_file, db_data['severity']))

        self.assertEqual(invalid, [])

    def test_lengths(self):
        invalid = []

        for language, _file, db_data in self.get_all_json():
            description = self.get_description(language, db_data['description']['$ref'])
            if len(description) <= 30:
                invalid.append(_file)

            guidance = self.get_fix(language, db_data['fix']['guidance']['$ref'])
            if len(guidance) <= 30:
                invalid.append(_file)

        self.assertEqual(invalid, [])

    def test_id_match(self):
        invalid = []

        for language, db_path_file, db_data in self.get_all_json():
            json_id = db_data['id']

            db_file = os.path.split(db_path_file)[1]

            if not db_file.startswith('%s-' % json_id):
                invalid.append(db_file)

        self.assertEqual(invalid, [])

    def test_no_multiple_spaces(self):
        invalid = []

        for language, db_path_file, db_data in self.get_all_json():
            description = self.get_description(language, db_data['description']['$ref'])
            guidance = self.get_fix(language, db_data['fix']['guidance']['$ref'])

            if '  ' in guidance:
                invalid.append((db_path_file, 'fix_guidance'))

            if '  ' in description:
                invalid.append((db_path_file, 'description'))

        self.assertEqual(invalid, [])

    @attr('slow')
    def test_url_is_not_404(self):
        all_urls = set()
        invalid = []

        for language, db_path_file, db_data in self.get_all_json():

            cwe_list = db_data.get('cwe', [])
            for cwe_id in cwe_list:
                all_urls.add(DBVuln.get_cwe_url(cwe_id))

            reference_list = db_data.get('references', [])
            for reference in reference_list:
                all_urls.add(reference['url'])

            owasp_top_10 = db_data.get('owasp_top_10', {})
            for version, risk_id_list in owasp_top_10.iteritems():
                for risk_id in risk_id_list:
                    owasp_url = self.get_owasp_url(version, risk_id)
                    all_urls.add(owasp_url)

        session = requests.Session()
        for url in all_urls:
            if self.url_is_404(session, url):
                invalid.append(url)

        self.assertEqual(invalid, [])

    def get_owasp_url(self, owasp_version, risk_id):
        owasp_version = int(owasp_version)

        # Just return one of them, 2013 release has priority over 2010
        if owasp_version == 2013:
            return OWASP_TOP10_2013_URL_FMT % risk_id

        if owasp_version == 2010:
            return OWASP_TOP10_2010_URL_FMT % risk_id

        raise NotImplementedError

    def url_is_404(self, session, url):
        try:
            response = session.get(url)
        except KeyboardInterrupt:
            raise
        except:
            return True
        else:
            return response.status_code == 404
