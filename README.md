This documentation provides an overview of the steps involved in this small project. The project's goal is to generate insights from Facebook post data, calculate engagement rates, and analyze various aspects of the data. The following steps have been completed:

1. **Generation of a Long-Term Access Token:**
   1.1. A long-term access token was generated using a short-lived token, an application ID, and an application secret. This long-term access token allows access to the Facebook API for an extended period.

2. **Retrieval of Facebook Posts and Storage of Data in a CSV File:**
   2.1. The project retrieved Facebook post data using the generated long-term access token.
   2.2. The obtained data for each post, including the post ID, message, creation time, attachments, number of likes, reactions, shares, comments, views, and number of fans, was stored in a CSV file.
   2.3. Each column in the CSV file corresponds to a specific data field mentioned above.

3. **Calculation of Engagement Rate:**
   3.1. The Facebook page's engagement rate was calculated using the formula:
   4. `(Total Engagements / Total Reach) * 100`.
   4.1. Total engagements include likes, comments, and shares received by the posts, while total reach represents the number of people who have seen the posts.

5. **Analysis of Post Statistics:**
   5.1. The project generated information about the posts, including the total number of posts, the average number of likes, shares, and comments per post.
   5.2. The distribution of shares, likes, and comments was analyzed to understand their patterns.

6. **Analysis of Post Frequency and Engagement Trends:**
   6.1. The project visualized the frequency of posts over time to identify trends and patterns in the Facebook page's posting behavior.
   6.2. Engagement trends over time were examined to understand variations in engagement levels over different periods.
   6.3. Engagement by day of the week was analyzed to identify the most and least engaging days for the Facebook page.

7. **Analysis of Correlation Matrix:**
   7.1. The correlation matrix was calculated to explore the relationships between likes, shares, and comments.
   7.2. This analysis helps understand the interdependencies between different engagement metrics.

8. **Identification of Most Engaging Words:**
   8.1. The project extracted words that attracted the most attention based on the content of the posts.
   8.2. This analysis helps identify key topics or themes that generated higher engagement.

9. **Identification of the Top Five Posts:**
   9.1. The project determined the top five posts of the Facebook page based on specific criteria such as the number of likes, shares, or comments.
   9.2. This information provides insights into the most successful posts in terms of engagement.
