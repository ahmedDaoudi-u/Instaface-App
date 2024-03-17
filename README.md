## Video Demonstration

[Watch Demo Video For The WebApp](https://www.youtube.com/watch?v=OEIvDY33yss)

## Project Overview

This documentation provides an overview of a small project aimed at generating insights from Facebook post data, calculating engagement rates, and analyzing various aspects of the data.

### Completed Steps

1. **Generation of a Long-Term Access Token:**
   
   1.1. A long-term access token was generated using a short-lived token, an application ID, and an application secret. This long-term access token allows access to the Facebook API for an extended period.

2. **Retrieval of Facebook Posts and Storage of Data in a CSV File:**
   
   2.1. The project retrieved Facebook post data using the generated long-term access token.
   
   2.2. Data for each post, including post ID, message, creation time, attachments, number of likes, reactions, shares, comments, views, and number of fans, was stored in a CSV file.
   
   2.3. Each column in the CSV file corresponds to a specific data field mentioned above.

3. **Calculation of Engagement Rate:**
   
   3.1. The Facebook page's engagement rate was calculated using the formula: `(Total Engagements / Total Reach) * 100`.
   
   3.2. Total engagements include likes, comments, and shares received by the posts, while total reach represents the number of people who have seen the posts.

4. **Analysis of Post Statistics:**
   
   4.1. Information about the posts, including the total number of posts, average number of likes, shares, and comments per post, was generated.
   
   4.2. The distribution of shares, likes, and comments was analyzed to understand their patterns.

5. **Analysis of Post Frequency and Engagement Trends:**
   
   5.1. The project visualized the frequency of posts over time to identify trends and patterns in the Facebook page's posting behavior.
   
   5.2. Engagement trends over time were examined to understand variations in engagement levels over different periods.
   
   5.3. Engagement by day of the week was analyzed to identify the most and least engaging days for the Facebook page.

6. **Analysis of Correlation Matrix:**
    
   6.1. The correlation matrix was calculated to explore the relationships between likes, shares, and comments.
   
   6.2. This analysis helps understand the interdependencies between different engagement metrics.

7. **Identification of Most Engaging Words:**
    
   7.1. Words that attracted the most attention based on the content of the posts were extracted.
   
   7.2. This analysis helps identify key topics or themes that generated higher engagement.

8. **Identification of the Top Five Posts:**
    
   8.1. The top five posts of the Facebook page were determined based on specific criteria such as the number of likes, shares, or comments.
   
   8.2. This information provides insights into the most successful posts in terms of engagement.

