import argparse
import pandas as pd
import matplotlib.pyplot as plt
# coding: utf-8


# Function to parse custom date format
def parse_custom_date(date_str):
    months = {
        'janv.': '01',
        'févr.': '02',  # Unicode escape sequence for 'févr.'
        'mars': '03',
        'avr.': '04',
        'mai': '05',
        'juin': '06',
        'juil.': '07',
        'août.': '08',  # Unicode escape sequence for 'août'
        'sept.': '09',
        'oct.': '10',
        'nov.': '11',
        'déc.': '12'  # Unicode escape sequence for 'déc.'
    }
    day, month_abbr, year = date_str.split(' ')
    month = months.get(month_abbr, '')
    return f'{day} {month} {year}'

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description='Analyzing and plotting data from CSV file')
    parser.add_argument('csv_file', help='Path to the CSV file to be analyzed')
    args = parser.parse_args()

    # Read the CSV file into a DataFrame
    data = pd.read_csv(args.csv_file)

    # Convert the date column to datetime format using the custom function
    data['AdSet Start Time'] = data['AdSet Start Time'].apply(parse_custom_date)
    data['AdSet Start Time'] = pd.to_datetime(data['AdSet Start Time'], format='%d %m %Y')
    plt.figure(figsize=(7, 8))

    # Create a scatter plot for impressions over time
    plt.plot(data['AdSet Start Time'], data['Impressions'])
    plt.xlabel('AdSet Start Time')
    plt.ylabel('Impressions')
    plt.title('Impressions Over Time')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary

    # Save the plot to a file
    plot_file_path = 'uploads/plot10.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    # Create the second plot for CPC over time
    plt.figure(figsize=(7, 8))
    plt.plot(data['AdSet Start Time'], data['CPC'])
    plt.xlabel('AdSet Start Time')
    plt.ylabel('CPC')
    plt.title('CPC Over Time')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary

    # Save the second plot to a file
    plot_file_path = 'uploads/plot11.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    plt.plot(data['CPM'], data['CPC'], 'o', markersize=3)
    plt.xlabel('CPM')
    plt.ylabel('CPC')
    plt.title('CPM vs. CPC')
    plt.savefig('uploads/plot12.png', format='png')
    plt.close()


    data['AdSet Start Time'] = pd.to_datetime(data['AdSet Start Time'])

# Create a line plot for % change in impressions and CPC over time
    data.plot(x='AdSet Start Time', y=['% Δ', '% Δ.2'], kind='line', marker='o', linestyle='-', figsize=(6, 6))
    plt.xlabel('AdSet Start Time')
    plt.ylabel('% Change')
    plt.title('% Change in Impressions and CPC Over Time')
    plt.legend(['% Δ Impressions', '% Δ CPC'])
    plot_file_path = 'uploads/plot13.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()


    data['Total Cost'].plot(kind='hist', bins=10, figsize=(6, 6))
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.xlabel('Total Cost')
    plt.ylabel('Frequency')
    plt.title('Distribution of Total Cost')
    plot_file_path = 'uploads/plot14.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()





    data['AdSet Start Time'] = pd.to_datetime(data['AdSet Start Time'], errors='coerce').dropna()

    # Calculate the total impressions count for each ad
    data['Total Impressions'] = data['Impressions']

    # Get the latest year
    latest_year = data['AdSet Start Time'].dt.year.max()

    # Filter the data to include only the latest year
    latest_year_data = data[data['AdSet Start Time'].dt.year == latest_year]

    # Calculate the average impressions for the previous years
    average_impressions = data['Total Impressions'].mean()

    # Create a scatter plot for impressions over time
    plt.figure(figsize=(7, 10))
    plt.plot(data['AdSet Start Time'], data['Total Impressions'], label='Impressions')
    plt.scatter(latest_year_data['AdSet Start Time'], latest_year_data['Total Impressions'], color='red', label='Latest Year Data')
    plt.axhline(y=average_impressions, color='green', linestyle='--', label='Average ')

    plt.xlabel('AdSet Start Time')
    plt.ylabel('Impressions')
    plt.title('Impressions Over Time for Ads')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary

    # Set x-axis limits to include only the latest year
    plt.xlim(pd.Timestamp(f'{latest_year}-01-01'), pd.Timestamp(f'{latest_year+1}-01-01') - pd.Timedelta(days=1))
    plt.annotate(f'Average: {average_impressions:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', ha='right', color='green', fontsize=12)

    plt.legend()

    plot_file_path = 'uploads/plot15.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()








    # Assuming you have already read the ads data into the DataFrame ads_df
    data['AdSet Start Time'] = pd.to_datetime(data['AdSet Start Time'])

# Calculate the total impressions count for each ad
    data['Total Impressions'] = data['Impressions']

    # Sort the data by 'AdSet Start Time' before calculating the accumulated impressions
    data.sort_values(by='AdSet Start Time', inplace=True)

    # Create a list to hold the average accumulated impressions for each day
    average_accumulated_impressions = []

    # Calculate the accumulated impressions and average for each day
    for index, row in data.iterrows():
        data_up_to_day = data.iloc[:index + 1]
        accumulated_impressions = data_up_to_day['Total Impressions'].sum()
        average_accumulated_impressions.append(accumulated_impressions / (index + 1))

    # Create a new DataFrame with 'AdSet Start Time' and 'Average Accumulated Impressions'
    average_accumulated_ads_df = pd.DataFrame({
        'AdSet Start Time': data['AdSet Start Time'],
        'Average Accumulated Impressions': average_accumulated_impressions
    })

    # Calculate the overall average impressions
    overall_average = sum(average_accumulated_impressions) / len(average_accumulated_impressions)

    # Plot the average accumulated impressions for the entire period
    plt.figure(figsize=(7, 10))
    plt.plot(average_accumulated_ads_df['AdSet Start Time'], average_accumulated_ads_df['Average Accumulated Impressions'])
    plt.axhline(y=overall_average, color='green', linestyle='--', label='Overall Average')

    plt.xlabel('AdSet Start Time')
    plt.ylabel('Average Accumulated Impressions Count')
    plt.title('Average Accumulated Impressions Over the Entire Period for Ads')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary

    # Annotate the overall average value
    plt.annotate(f'Overall Avg: {overall_average:.2f}', xy=(0.70, 0.85), xycoords='axes fraction', color='green')

    plt.legend()  # Rotate x-axis labels if necessary
    plot_file_path = 'uploads/plot16.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()







    # Convert the date column to datetime format using the custom function







    # Display the second plot to the interactive plot window
    plt.show()

if __name__ == "__main__":
    main()
