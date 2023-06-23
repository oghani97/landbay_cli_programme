import argparse
import pandas as pd
import matplotlib.pyplot as plt


class MortgageDataDates:
    def __init__(self, data_file):
        self.data_file = data_file

    def filter_data(self, target_month, property_category=None):
        # The CSV Data is loaded in
        df = pd.read_csv(self.data_file)

        # Perform a filter query on data in order to only get results with desired month and property-category
        df_filtered = self.filter_cases(df, target_month, property_category)

        # Time difference between completed and submitted
        df_filtered['TimeToComplete'] = pd.to_datetime(df_filtered['COMPLETED_DATE']) - pd.to_datetime(df_filtered['APPLICATION_SUBMITTED_DATE'])
        df_filtered['TimeToComplete'] = df_filtered['TimeToComplete'].dt.days // 30  # Difference in months known as X in question

        # print(df_filtered['TimeToComplete'])

        # This then tallies up the X values and displays them in a new DF
        countMonthMatch = df_filtered['TimeToComplete'].value_counts().sort_index()

        # print(countMonthMatch)

        # Generate the plot
        self.generate_plot(countMonthMatch)

    def filter_cases(self, df, target_month, property_category):
        # Filter cases based on target month
        df_filtered = df[df['APPLICATION_SUBMITTED_DATE'].str.startswith(target_month)]

        # Filter cases based on property category if provided
        if property_category:
            df_filtered = df_filtered[df_filtered['PROPERTY_CATEGORY'] == property_category]

        return df_filtered

    def generate_plot(self, countMonthMatch):
        plt.plot(countMonthMatch.index, countMonthMatch.values, marker='X', linestyle='-', color='b')
        plt.xlabel('Time to Completion (Months)')
        plt.ylabel('Number of Cases')
        plt.title('Number of Completed Cases over Time')
        plt.grid(True)
        plt.show()


def main():
    parser = argparse.ArgumentParser(description='This is an application to find the time taken for an application to be completed given a particular month')
    parser.add_argument('target_month', type=str, help='Format "YYYY-MM"')
    parser.add_argument('property_category', type=str, help='Property Category - This can be left in order to perform a generic search*')
    args = parser.parse_args()

    mDDObject = MortgageDataDates('data_task_part_1.csv')
    mDDObject.filter_data(args.target_month, args.property_category)


if __name__ == '__main__':
    main()
