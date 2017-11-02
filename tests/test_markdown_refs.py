import json
import os
from tests.vulndb_test import VulnDBTest, DBVuln


class TestReferences(VulnDBTest):
    """
    Ensure that every fix and description field has a corresponding
    markdown file, and that every markdown file is referenced by at
    least one vulnerability.
    """
    def setUp(self):
        super(TestReferences, self).setUp()
        self.desc_ids = set()
        self.referenced_desc_ids = set()
        self.fix_ids = set()
        self.referenced_fix_ids = set()
        for f in os.listdir(DBVuln.DB_PATH):
            fpath = os.path.join(DBVuln.DB_PATH, f)
            if not os.path.isfile(fpath):
                continue
            with open(fpath) as ifile:
                data = json.load(ifile)
            desc_id = data['description']['$ref'].split('/')[-1]
            self.referenced_desc_ids.add(desc_id)
            fix_id = data['fix']['guidance']['$ref'].split('/')[-1]
            self.referenced_fix_ids.add(fix_id)
        for f in os.listdir(os.path.join(DBVuln.DB_PATH, 'description')):
            fpath = os.path.join(DBVuln.DB_PATH, 'description', f)
            if not os.path.isfile(fpath):
                continue
            f_id = f.replace('.md', '').split('-')[0]
            self.desc_ids.add(f_id)
        for f in os.listdir(os.path.join(DBVuln.DB_PATH, 'fix')):
            fpath = os.path.join(DBVuln.DB_PATH, 'fix', f)
            if not os.path.isfile(fpath):
                continue
            f_id = f.replace('.md', '').split('-')[0]
            self.fix_ids.add(f_id)

    def test_description_refs(self):
        for desc_id in self.referenced_desc_ids:
            self.assertIn(
                desc_id, self.desc_ids,
                'description is missing: {}'.format(desc_id)
            )
        for desc_id in self.desc_ids:
            self.assertIn(
                desc_id, self.desc_ids,
                'description is not referenced: {}'.format(desc_id)
            )

    def test_fix_refs(self):
        for fix_id in self.referenced_fix_ids:
            self.assertIn(
                fix_id, self.fix_ids,
                'fix is missing: {}'.format(fix_id)
            )
        for fix_id in self.fix_ids:
            self.assertIn(
                fix_id, self.referenced_fix_ids,
                'fix is not referenced: {}'.format(fix_id)
            )
