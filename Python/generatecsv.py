import requests
import csv
import sys


def fetch_page_fan_count(page_name, access_token):
    url = 'https://graph.facebook.com/' + page_name

    params = {
        'access_token': access_token,
        'fields': 'fan_count',
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'fan_count' not in data:
        return 0

    return data['fan_count']

def fetch_all_posts(page_name, access_token):
    url = 'https://graph.facebook.com/' + page_name

    params = {
        'access_token': access_token,
        'fields': 'id',
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'id' not in data:
        return []

    page_id = data['id']

    url = 'https://graph.facebook.com/{}/feed'.format(page_id)

    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time,attachments,likes.summary(true),shares,comments.summary(true),views',
        'limit': 100  # Adjust the limit as needed, 100 is the maximum allowed per request
    }

    posts = []

    while True:
        response = requests.get(url, params=params)
        data = response.json()

        if 'data' not in data:
            break

        posts.extend(data['data'])

        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
        else:
            break

    return posts

def save_posts_to_csv(posts, csv_file, num_fans):
    fieldnames = ['Post ID', 'Message', 'Created Time', 'Attachments', 'Likes Count', 'Reactions', 'Shares Count', 'Comments Count', 'Views Count', 'Number of Fans']

    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for post in posts:
            post_id = post['id']
            message = post.get('message', '')
            created_time = post.get('created_time', '')
            attachments = post.get('attachments', {}).get('data', [])
            likes_count = post['likes']['summary']['total_count']

            # Check if 'data' key exists in 'likes'
            if 'data' in post['likes']:
                reactions = [reaction['type'] for reaction in post['likes']['data'] if 'type' in reaction]
            else:
                reactions = []

            shares_count = post['shares']['count'] if 'shares' in post else 0
            comments_count = post['comments']['summary']['total_count']
            views_count = post.get('views', {}).get('count', 0)

            writer.writerow({
                'Post ID': post_id,
                'Message': message,
                'Created Time': created_time,
                'Attachments': attachments,
                'Likes Count': likes_count,
                'Reactions': reactions,
                'Shares Count': shares_count,
                'Comments Count': comments_count,
                'Views Count': views_count,
                'Number of Fans': num_fans
            })

def main():
    if len(sys.argv) != 3:
        print("Usage: python your_python_script.py <page_name> <access_token>")
        sys.exit(1)

    page_name = sys.argv[1]
    access_token = sys.argv[2]
    csv_file = 'data.csv'

    num_fans = fetch_page_fan_count(page_name, access_token)
    all_posts = fetch_all_posts(page_name, access_token)

    save_posts_to_csv(all_posts, csv_file, num_fans)

    print("Posts saved to CSV successfully.")

if __name__ == "__main__":
    main()
