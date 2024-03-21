# Project Overview

This documentation provides an overview of a small project aimed at generating insights from Facebook post data, calculating engagement rates, and analyzing various aspects of the data using visualisation.
# The Complete steps for each process:

## Process 1:
### Step 1 : Generate Long Token

1. **Generation of a Long-Term Access Token:**
   
   1.1. A long-term access token was generated using a short-lived token, an application ID, and an application secret. This long-term access token allows access to the Facebook API for an extended period.
### Step 2: Fetch data from Facebook using long token and generate the corresponding CSV file
2. **Retrieval of Facebook Posts and Storage of Data in a CSV File:**

The Long token will retrieve Facebook data, in our case the fields are:

**post ID, message, creation time, attachments, number of likes, reactions, shares, comments, views, and number of fans**.

3. **Calculation of Engagement Rate:**
   
   3.1. The Facebook page's engagement rate was calculated using the formula: `(Total Engagements / Total Reach) * 100`.
   
   3.2. Total engagements include likes, comments, and shares received by the posts, while total reach represents the number of people who have seen the posts.

4. **Analysis of Post Statistics:**
   
  We visualize information about the posts, including the total number of posts, average number of likes, shares, and comments per post, was generated.
   
5. **Analysis of Post Frequency and Engagement Trends:**
   
   5.1. The project visualized the frequency of posts over time to identify trends and patterns in the Facebook page's posting behavior.
   
   5.2. Engagement trends over time were examined to understand variations in engagement levels over different periods.
   
   5.3. Engagement by day of the week was analyzed to identify the most and least engaging days for the Facebook page.

6. **Analysis of Correlation Matrix:**
    
The correlation matrix was calculated to explore the relationships between likes, shares, and comments which will help understand the interdependencies between different engagement metrics.

7. **Identification of Most Engaging Words:**
    
Indentifaying the Words that attracted the most attention based on the content of the posts will help identifying key topics or themes that generated higher engagement.

8. **Identification of the Top Five Posts:**
    
The top five posts of the Facebook page were determined based on specific criteria such as the number of likes, shares, or comments ;meaning the most successful posts in terms of engagement.
## Process 2:
### Step 1 : Getting the CSV file from Looker-studio for Ads analysis(Facebook & Instagram)
Getting the appropriate fields for the CSV file : 

**Campaign Name , Facebook Page ID, Instagram Page ID, Start Date and Time of Ad Set, End Date and Time of Ad Set, Facebook Post ID , Instagram Post ID , Impressions , % Δ CPM (Cost Per Mille), % Δ.1 CPC (Cost Per Click), % Δ.2 Total Cost, % Δ.3 Start Date and Time of Ad Set.**

### Step 2: Fetch data from Facebook using long token and generate the corresponding CSV file

1. **Facebook and Instagram Campaign Insights:**
   
   Analyzes metrics like impressions, CPC, CPM, and cost to evaluate advertising effectiveness comprehensively.

2. **Evolution of Impressions Over Time:**
   
   Tracks impressions trends to understand campaign reach and visibility fluctuations over time.

3. **CPC (Cost Per Click) Over Time:**
   
   Examines CPC variations to gauge user engagement and campaign efficiency across intervals.

4. **CPM (Cost Per Mille) & CPC (Cost Per Click):**
   
   Explores CPM-CPC relationship to assess campaign cost-effectiveness and engagement balance.

5. **Variation of Impressions and CPC Over Time:**
    
   Simultaneously analyzes impressions and CPC trends to understand their combined impact.

6. **Distribution of Total Cost:**
    
   Illustrates cost allocation across campaign segments, revealing efficiency insights in resource utilization.

7. **Evolving Campaign Performance Over Time:**
    
   Provides a comprehensive view of campaign trends, assessing effectiveness across successive intervals.

8. **Evolution of Average Cumulative Impressions for Advertising Campaigns:**
    
   Tracks average impressions growth over time, indicating reach expansion or saturation levels.

# Video Demonstration

👉🏻[Watch Demo Video For The WebApp](https://www.youtube.com/watch?v=OEIvDY33yss)👈🏻

