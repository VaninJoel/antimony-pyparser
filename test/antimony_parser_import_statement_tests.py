import unittest
from antimony_parser import AntimonyParser


class AntimonyParserImportStatementTests(unittest.TestCase):
    parser = AntimonyParser()

    def check_import_statement_parses_correctly(self, filename_string: str) -> None:
        antimony_string = f"import \"{filename_string}\""
        print(f"checking string '{antimony_string}' passes")
        tree = self.parser.parse(antimony_string)
        assert len(tree.children) == 1
        token = tree.children[0]
        self.assertEqual(str(token), f"\"{filename_string}\"")

    def test_import_statement_in_home_directory(self):
        self.check_import_statement_parses_correctly("/home/model1.txt")

    def test_import_statement_in_alternate_directory(self):
        self.check_import_statement_parses_correctly("/home/myproject/arbitrary/depth/model1.txt")


if __name__ == '__main__':
    unittest.main()
