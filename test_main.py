import unittest
from unittest.mock import patch
from main import extract_newsletter, extract_report, process_data

class TestDataProcessing(unittest.TestCase):
    def test_extract_newsletter(self):
        upstream_data = {'newsletter': 'Test Newsletter'}
        self.assertEqual(extract_newsletter(upstream_data), 'Test Newsletter')

    def test_extract_report(self):
        upstream_data = {'report': 'Test Report'}
        self.assertEqual(extract_report(upstream_data), 'Test Report')

    def test_process_data(self):
        upstream_data = {'newsletter': 'Test Newsletter', 'report': 'Test Report'}
        newsletter, report = process_data(upstream_data)
        self.assertEqual(newsletter, 'Test Newsletter')
        self.assertEqual(report, 'Test Report')

    @patch('builtins.open')
    def test_main(self, mock_open):
        mock_open.return_value.__enter__.return_value = open('test_context.json', 'r')
        with open('test_context.json', 'w') as f:
            json.dump({'newsletter': 'Test Newsletter', 'report': 'Test Report'}, f)
        import sys
        import io
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # Redirect stdout
        from main import main
        main()
        sys.stdout = sys.__stdout__  # Reset stdout
        self.assertIn('Test Newsletter', capturedOutput.getvalue())
        self.assertIn('Test Report', capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main()