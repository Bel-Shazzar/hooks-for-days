import unittest
from io import StringIO

from scripts import copied_lines_at_file_end


class TestCopiedLinesAtFileEnd(unittest.TestCase):
    def test_fix_file_no_copied_lines(self):
        file_content = "line 1\nline 2\nline 3\n"
        file_obj = StringIO(file_content)
        result = copied_lines_at_file_end.fix_file(file_obj)
        self.assertEqual(result, 0)
        self.assertEqual(file_obj.getvalue(), file_content)

    def test_fix_file_with_copied_lines(self):
        file_content = "line 1\nline 2\nline 3\nline 3\n"
        expected_content = "line 1\nline 2\nline 3\n"
        file_obj = StringIO(file_content)
        result = copied_lines_at_file_end.fix_file(file_obj)
        self.assertEqual(result, 1)
        self.assertEqual(file_obj.getvalue(), expected_content)

    def test_fix_file_with_multiple_copied_lines(self):
        file_content = "line 1\nline 2\nline 3\nline 3\nline 3\n"
        expected_content = "line 1\nline 2\nline 3\n"
        file_obj = StringIO(file_content)
        result = copied_lines_at_file_end.fix_file(file_obj)
        self.assertEqual(result, 1)
        self.assertEqual(file_obj.getvalue(), expected_content)

    def test_fix_file_with_ignore_empty_last_line(self):
        file_content = "line 1\nline 2\nline 3\nline 3\nline 3\n\n"
        expected_content = "line 1\nline 2\nline 3\n\n"
        file_obj = StringIO(file_content)
        result = copied_lines_at_file_end.fix_file(file_obj)
        self.assertEqual(result, 1)
        self.assertEqual(file_obj.getvalue(), expected_content)

    def test_ignore_file_with_empty_last_line(self):
        file_content = "line 1\nline 2\nline 3\n\n"
        expected_content = "line 1\nline 2\nline 3\n\n"
        file_obj = StringIO(file_content)
        result = copied_lines_at_file_end.fix_file(file_obj)
        self.assertEqual(result, 0)
        self.assertEqual(file_obj.getvalue(), expected_content)


if __name__ == "__main__":
    unittest.main()
