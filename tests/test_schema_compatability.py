import json
import jsonschema

from tests.vulndb_test import VulnDBTest

SCHEMA_FILENAME = "schema.json"


class TestAllFilesSchemaCompatability(VulnDBTest):
    """
    Basic test to make sure that all the files inside the db directory end
    with the json extension and have valid json content
    """
    def test_all_files_JSON_content(self):
        try:
            schema = json.loads(file(SCHEMA_FILENAME).read())
        except (ValueError, IOError) as e:
            self.fail(e)

        try:
            jsonschema.Draft4Validator.check_schema(schema)
        except jsonschema.SchemaError as e:
            self.fail(e)

        incompatible = []
        for _file, db_data in self.get_all_json():
            try:
                jsonschema.validate(db_data, schema)
            except jsonschema.ValidationError as e:
                incompatible.append((_file, e,))

        self.assertEqual(incompatible, [])
