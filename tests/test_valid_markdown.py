from markdown import markdown
from tests.vulndb_test import VulnDBTest


class TestValidMarkdown(VulnDBTest):
    def test_valid_markdown(self):
        invalid = []

        for _file, db_data in self.get_all_json():
            description = self.to_string(db_data['description'])
            try:
                markdown(description)
            except:
                invalid.append(_file)

            guidance = self.to_string(db_data['fix']['guidance'])
            try:
                markdown(guidance)
            except:
                invalid.append(_file)

        self.assertEqual(invalid, [])

