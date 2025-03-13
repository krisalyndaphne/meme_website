import requests

url = "https://api.apilayer.com/sentiment/analysis"
headers = {
    "apikey": "Enter your api key",
    "Content-Type": "application/json"
}
payload = {"text": "woah so frustrating i am angry"} //example ..// give ur own text

response = requests.post(url, headers=headers, json=payload)

status_code = response.status_code
if status_code == 200:
    result = response.json()  # Parse JSON directly
    print(f"Sentiment: {result['sentiment']}, Confidence: {result['confidence']}")
else:
    print(f"Error: {status_code}, {response.text}")
