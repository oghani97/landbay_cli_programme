import unittest
from io import StringIO
import sys
from property import CaseAnalyzer

class CaseAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a sample data file for testing
        self.data = StringIO("""CASE_NUMBER,STATUS,APPLICATION_SUBMITTED_DATE,COMPLETED_DATE,CANCELLATION_DATE,BROKER_ID,BROKER_FIRM_ID,LOAN_AMOUNT,PROPERTY_CATEGORY
        1,Completed,2022-01-01,2022-03-01,,123,456,100000,Residential
        2,Completed,2022-01-01,2022-02-01,,123,456,200000,Commercial
        3,Completed,2022-01-01,2022-05-01,,456,789,150000,Residential
        4,Completed,2022-02-01,2022-04-01,,456,789,300000,Residential
        5,Completed,2022-03-01,2022-03-15,,789,123,250000,Commercial
        6,Completed,2022-03-01,2022-04-01,,789,123,400000,Residential
        """)

    def test_analyze_cases_with_category(self):
        # Redirect stdout for capturing the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Create an instance of CaseAnalyzer and run the analysis
        analyzer = CaseAnalyzer(self.data)
        analyzer.run('2022-03', 'Residential')

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Retrieve the captured output
        output = captured_output.getvalue()

        # Assert the expected output
        expected_output = "Number of Cases vs. Completion Months\n\n2: 1\n3: 1\n"
        self.assertEqual(output.strip(), expected_output.strip())

    def test_analyze_cases_without_category(self):
        # Redirect stdout for capturing the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Create an instance of CaseAnalyzer and run the analysis
        analyzer = CaseAnalyzer(self.data)
        analyzer.run('2022-03')

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Retrieve the captured output
        output = captured_output.getvalue()

        # Assert the expected output
        expected_output = "Number of Cases vs. Completion Months\n\n1: 1\n2: 1\n"
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()