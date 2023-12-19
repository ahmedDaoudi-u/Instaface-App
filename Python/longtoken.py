import sys
import requests

def exchange_short_token_for_long(short_token, app_id, app_secret):
    url = f"https://graph.facebook.com/v17.0/oauth/access_token"
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': short_token
    }

    response = requests.get(url, params=params)
    data = response.json()

    long_token = data.get('access_token')
    expires_in = data.get('expires_in')

    return long_token, expires_in

if __name__ == '__main__':
    short_token = sys.argv[1]
    app_id = sys.argv[2]
    app_secret = sys.argv[3]

    long_token, expires_in = exchange_short_token_for_long(short_token, app_id, app_secret)

print('Long-lived Token:   ', long_token)
print('Expires In:   ', expires_in, 'Seconds ', "~ ", expires_in/2.628e+6 ,"Months",)
