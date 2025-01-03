import requests

def test_web_app_connection(url):
    try:
        response = requests.get(url)
        print("Response from web app:", response.text)
    except Exception as e:
        print("Error connecting to web app:", e)
