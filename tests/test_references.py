from tests.vulndb_test import VulnDBTest


class TestReferences(VulnDBTest):
    """
    We don't want redundant references.  Test for the presence of a
    reference URL that contains a cve.mitre.org URL.  If an invalid
    reference is detected, simply remove the reference and add the
    CWE-ID to the "cwe" section of the vulnerability.
    """
    def test_no_redundant_cve_mitre_org_urls(self):
        invalid = []

        for language, db_path_file, db_data in self.get_all_json():
            reference_urls = set()

            reference_list = db_data.get('references', [])
            for reference in reference_list:
                reference_urls.add(reference['url'])

            for reference in reference_urls:
                if 'cwe.mitre.org' in reference:
                    invalid.append(reference.url)

        self.assertEqual(invalid, [])
