# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

def analyze_data(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)


    # Perform analysis
    total_posts = len(df)
    average_likes = df['Likes Count'].mean().round(2)
    average_shares = df['Shares Count'].mean().round(2)
    average_comments = df['Comments Count'].mean().round(2)

    # Create a histogram of likes
    plt.figure(figsize=(5, 3))
    sns.histplot(df['Likes Count'], bins=20)
    plt.xlabel('Number of Likes')
    plt.ylabel('Frequency')
    plt.title('Distribution of Likes')
    plt.tight_layout()

    # Save the plot to a temporary file
    plot_file_path = 'uploads/plot.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()


    plt.figure(figsize=(5, 4))
    sns.histplot(df['Shares Count'], bins=20)
    plt.xlabel('Number of Shares')
    plt.ylabel('Frequency')
    plt.title('Distribution of Shares')

    plot_file_path = 'uploads/plot1.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()


    plt.figure(figsize=(5, 4))
    sns.histplot(df['Comments Count'], bins=20)
    plt.xlabel('Number of Comments')
    plt.ylabel('Frequency')
    plt.title('Distribution of Comments')

    plot_file_path = 'uploads/plot2.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    plt.figure(figsize=(4, 3))
    df['Created Time'] = pd.to_datetime(df['Created Time'],errors='coerce')
    df.plot(x='Created Time', y=['Likes Count', 'Shares Count', 'Comments Count'], kind='line')
    plt.xlabel('Date')
    plt.ylabel('Engagement Count')
    plt.title('Engagement Trends over Time')
    plt.legend()
    plot_file_path = 'uploads/plot3.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    df['Created Time'] = pd.to_datetime(df['Created Time'],errors='coerce')
    df['Day of Week'] = df['Created Time'].dt.weekday
    engagement_by_day = df.groupby('Day of Week')[['Likes Count', 'Shares Count', 'Comments Count']].sum()
    plt.figure(figsize=(2, 1))
    engagement_by_day.plot(kind='bar')
    plt.xlabel('Day of Week')
    plt.ylabel('Engagement Count')
    plt.title('Engagement by Day of the Week')
    plt.legend()
    plot_file_path = 'uploads/plot4.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()


    # Heatmap of correlation matrix
    plt.figure(figsize=(6, 6))
    correlation_matrix = df[["Likes Count", "Shares Count", "Comments Count"]].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plot_file_path = 'uploads/plot5.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    df['Total Engagement'] = df['Likes Count']*1 + df['Shares Count']*4 + df['Comments Count']*2
    df.plot(x='Created Time', y='Total Engagement', kind='line')
    plt.xlabel('Date')
    plt.ylabel('Total Engagement Count')
    plt.title('Total Engagement Trends over Time')
    plt.legend()
    plot_file_path = 'uploads/plot6.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()

    df['Created Time'] = pd.to_datetime(df['Created Time'], errors='coerce').dropna()

    # Calculate the total engagement count for each row
    df['Total Engagement'] = df['Likes Count'] + df['Shares Count']*4 + df['Comments Count']*2

    # Get the latest year
    latest_year = df['Created Time'].dt.year.max()

    # Filter the data to include only the latest year
    latest_year_data = df[df['Created Time'].dt.year == latest_year]

    # Calculate the average engagement for the previous years

    average_engagement = df['Total Engagement'].mean()

    # Create a scatter plot for engagement over time
    plt.figure(figsize=(7, 10))
    plt.plot(df['Created Time'], df['Total Engagement'], label='Engagement')
    plt.scatter(latest_year_data['Created Time'], latest_year_data['Total Engagement'], color='red', label='Latest Year Data')
    plt.axhline(y=average_engagement, color='green', linestyle='--', label='Average of Previous Years')

    plt.xlabel('Created Time')
    plt.ylabel('Engagement Count')
    plt.title('Engagement Over Time')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary

    # Set x-axis limits to include only the latest year
    plt.xlim(pd.Timestamp(f'{latest_year}-01-01'), pd.Timestamp(f'{latest_year+1}-01-01') - pd.Timedelta(days=1))
    plt.annotate(f'Average: {average_engagement:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', ha='right', color='green', fontsize=12)

    plt.legend()
    plot_file_path = 'uploads/plot7.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()






    df['Created Time'] = pd.to_datetime(df['Created Time'],errors='coerce')

    # Calculate the total engagement count for each row
    df['Total Engagement'] = df['Likes Count'] + df['Shares Count'] + df['Comments Count']

    # Sort the data by 'Created Time' before calculating the accumulated engagement
    df.sort_values(by='Created Time', inplace=True)

    # Create a new DataFrame to hold accumulated engagement for each day
    day_accumulation_df = pd.DataFrame(columns=['Created Time', 'Accumulated Engagement'])

    # Calculate the accumulated engagement for each day in the entire period
    df['Accumulated Engagement'] = df['Total Engagement'].cumsum()

    plt.figure(figsize=(6, 8))
    plt.plot(df['Created Time'], df['Accumulated Engagement'])
    plt.xlabel('Created Time')
    plt.ylabel('Accumulated Engagement Count')
    plt.title('Accumulated Engagement Over the Entire Period')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary
    plot_file_path = 'uploads/plot8.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()


    # Assuming you have already read the data into the DataFrame df
    df['Created Time'] = pd.to_datetime(df['Created Time'],errors='coerce')

    # Calculate the total engagement count for each row
    df['Total Engagement'] = df['Likes Count'] + df['Shares Count'] + df['Comments Count']

    # Sort the data by 'Created Time' before calculating the accumulated engagement
    df.sort_values(by='Created Time', inplace=True)

    # Create a list to hold the average accumulated engagement for each day
    average_accumulated_engagement = []

    # Calculate the accumulated engagement and average for each day
    for index, row in df.iterrows():
        data_up_to_day = df.iloc[:index + 1]
        accumulated_engagement = data_up_to_day['Total Engagement'].sum()
        average_accumulated_engagement.append(accumulated_engagement / (index + 1))

    # Create a new DataFrame with 'Created Time' and 'Average Accumulated Engagement'
    average_accumulated_df = pd.DataFrame({
        'Created Time': df['Created Time'],
        'Average Accumulated Engagement': average_accumulated_engagement
    })

    # Plot the average accumulated engagement for the entire period
    plt.figure(figsize=(6, 8))
    plt.plot(average_accumulated_df['Created Time'], average_accumulated_df['Average Accumulated Engagement'])
    plt.xlabel('Created Time')
    plt.ylabel('Average Accumulated Engagement Count')
    plt.title('Average Accumulated Engagement Over the Entire Period')
    plt.xticks(rotation=88)  # Rotate x-axis labels if necessary
    plot_file_path = 'uploads/plot9.png'
    plt.savefig(plot_file_path, format='png')
    plt.close()















    # Prepare the analysis results as a dictionary
    analysis_results = {
        'total_posts': total_posts,
        'average_likes': average_likes,
        'average_shares': average_shares,
        'average_comments': average_comments,
    }

    # Convert the analysis_results dictionary to a JSON string
    analysis_results_json = json.dumps(analysis_results)

    # Print the JSON string (will be captured by the PythonShell in Node.js)
    print(analysis_results_json)

if __name__ == "__main__":
    import sys
    csv_file_path = sys.argv[1]
    analyze_data(csv_file_path)
