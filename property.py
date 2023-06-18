import argparse
import pandas as pd
import matplotlib.pyplot as plt

class CaseAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(self):
        # Load data from CSV file into a Pandas DataFrame
        df = pd.read_csv(data_task_part_1.csv)
        return df

    def filter_data(self, df, month, category):
        # Filter data based on specified month and property category (if provided)
        df['APPLICATION_SUBMITTED_DATE'] = pd.to_datetime(df['APPLICATION_SUBMITTED_DATE'])
        df['COMPLETED_DATE'] = pd.to_datetime(df['COMPLETED_DATE'])
        df = df[df['APPLICATION_SUBMITTED_DATE'].dt.strftime('%Y-%m') == month]

        if category:
            df = df[df['PROPERTY_CATEGORY'] == category]

        return df

    def analyze_cases(self, df):
        # Calculate the difference in months between application_submitted_date and completed_date
        df['Completion_Months'] = (df['COMPLETED_DATE'] - df['APPLICATION_SUBMITTED_DATE']) / pd.Timedelta(days=30)
        df['Completion_Months'] = df['Completion_Months'].astype(int)

        # Count the number of cases for each completion month
        case_counts = df['Completion_Months'].value_counts().sort_index()

        return case_counts

    def plot_cases(self, case_counts):
        # Plot the number of cases vs. completion months
        case_counts.plot(kind='bar', xlabel='Completion Months', ylabel='Number of Cases')
        plt.title('Number of Cases vs. Completion Months')
        plt.show()

    def run(self, month, category=None):
        # Load data, filter, analyze, and plot cases
        df = self.load_data()
        df_filtered = self.filter_data(df, month, category)
        case_counts = self.analyze_cases(df_filtered)
        self.plot_cases(case_counts)


if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser(description='Case Analyzer')
    parser.add_argument('month', help='Month in the format "YYYY-MM"')
    parser.add_argument('--category', help='Optional property category')

    # Parse command-line arguments
    args = parser.parse_args()

    # Specify the data file path
    data_file = 'path/to/your/data/file.csv'

    # Create an instance of CaseAnalyzer and run the analysis
    analyzer = CaseAnalyzer(data_file)
    analyzer.run(args.month, args.category)
