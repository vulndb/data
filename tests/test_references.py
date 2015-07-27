import re

from vulndb import DBVuln
from tests.vulndb_test import VulnDBTest

class TestReferences(VulnDBTest):

    def test_no_redundant_cve_mitre_org_urls(self):
        invalid = []

        for vuln_id in DBVuln.get_all_db_ids():
            db_vuln = DBVuln.from_id(vuln_id)

            for reference in db_vuln.references:
                if re.match('^http://cwe.mitre.org/data/definitions/[0-9]+\.html$', reference.url):
                    invalid.append(reference.url)

        self.assertEqual(invalid, [])
