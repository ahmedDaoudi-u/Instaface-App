# calculate_engagement_rate.py
import pandas as pd

def calculate_engagement_rate(total_engagements, total_reach):
    engagement_rate = (total_engagements / total_reach) * 100
    return engagement_rate

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: engegement.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    df = pd.read_csv(csv_file_path)

    total_engagements = df['Likes Count'] + df['Comments Count'] + df['Shares Count']
    total_reach = df['Number of Fans'].sum()

    engagement_rate = calculate_engagement_rate(total_engagements.sum(), total_reach)
    print(engagement_rate)
