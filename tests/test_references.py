import re

from vulndb import DBVuln
from tests.vulndb_test import VulnDBTest

CVE_URL_PATTERN = '^http://cwe.mitre.org/data/definitions/[0-9]+\.html$'


class TestReferences(VulnDBTest):
    """
    We don't want redundant references.  Test for the presence of a
    reference URL that contains a cve.mitre.org URL.  If an invalid
    reference is detected, simply remove the reference and add the
    CWE-ID to the "cwe" section of the vulnerability.
    """
    def test_no_redundant_cve_mitre_org_urls(self):
        invalid = []

        for vuln_id in DBVuln.get_all_db_ids():
            db_vuln = DBVuln.from_id(vuln_id)

            for reference in db_vuln.references:
                if re.match(CVE_URL_PATTERN, reference.url):
                    invalid.append(reference.url)

        self.assertEqual(invalid, [])
