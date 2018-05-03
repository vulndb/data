from markdown import markdown
from tests.vulndb_test import VulnDBTest


class TestValidMarkdown(VulnDBTest):
    def test_valid_markdown(self):
        invalid = []

        for language, _file, db_data in self.get_all_json():
            description = self.get_description(language, db_data['description']['$ref'])
            try:
                markdown(description)
            except:
                invalid.append(_file)

            guidance = self.get_fix(language, db_data['fix']['guidance']['$ref'])
            try:
                markdown(guidance)
            except:
                invalid.append(_file)

        self.assertEqual(invalid, [])

