import os

from tests.vulndb_test import VulnDBTest


class TestReferences(VulnDBTest):
    """
    Ensure that every fix and description field has a corresponding
    markdown file, and that every markdown file is referenced by at
    least one vulnerability.
    """
    def get_references_for_language(self, language):
        desc_ids = set()
        referenced_desc_ids = set()
        fix_ids = set()
        referenced_fix_ids = set()

        for language_iter, db_path_file, db_data in self.get_all_json():

            if language_iter != language:
                continue

            desc_id = db_data['description']['$ref'].split('/')[-1]
            fix_id = db_data['fix']['guidance']['$ref'].split('/')[-1]

            referenced_desc_ids.add(desc_id)
            referenced_fix_ids.add(fix_id)

        description_path = os.path.join('db', language, 'description')
        fix_path = os.path.join('db', language, 'fix')

        for f in os.listdir(description_path):
            fpath = os.path.join(description_path, f)

            if not os.path.isfile(fpath):
                continue

            d_id = f.replace('.md', '').split('-')[0]
            desc_ids.add(d_id)

        for f in os.listdir(fix_path):
            fpath = os.path.join(fix_path, f)

            if not os.path.isfile(fpath):
                continue

            f_id = f.replace('.md', '').split('-')[0]
            fix_ids.add(f_id)

        return desc_ids, fix_ids, referenced_desc_ids, referenced_fix_ids

    def test_description_refs(self):
        for language in self.get_all_languages():
            desc_ids, _, referenced_desc_ids, _ = self.get_references_for_language(language)

            for desc_id in referenced_desc_ids:
                self.assertIn(
                    desc_id, desc_ids,
                    'description is missing: {}'.format(desc_id)
                )

            for desc_id in desc_ids:
                self.assertIn(
                    desc_id, referenced_desc_ids,
                    'description is not referenced: {}'.format(desc_id)
                )

    def test_fix_refs(self):
        for language in self.get_all_languages():
            _, fix_ids, _, referenced_fix_ids = self.get_references_for_language(language)

            for fix_id in referenced_fix_ids:
                self.assertIn(
                    fix_id, fix_ids,
                    'fix is missing: {}'.format(fix_id)
                )

            for fix_id in fix_ids:
                self.assertIn(
                    fix_id, referenced_fix_ids,
                    'fix is not referenced: {}'.format(fix_id)
                )
