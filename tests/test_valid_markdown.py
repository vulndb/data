from markdown import markdown
from tests.vulndb_test import VulnDBTest


class TestValidMarkdown(VulnDBTest):
    def test_valid_markdown(self):
        invalid = []

        for _file, db_data in self.get_all_json():
            description = self.get_description(db_data['description']['$ref'])
            try:
                markdown(description)
            except:
                invalid.append(_file)

            guidance = self.get_fix(db_data['fix']['guidance']['$ref'])
            try:
                markdown(guidance)
            except:
                invalid.append(_file)

        self.assertEqual(invalid, [])

