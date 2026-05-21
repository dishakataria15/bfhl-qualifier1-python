import sys
import json
import requests

# Read the webhook payload from stdin
try:
      input_data = sys.stdin.read()
      payload = json.loads(input_data)
except Exception as e:
      print(f"Error reading input: {e}")
      sys.exit(1)

# Extract webhook url and token
webhook_url = payload.get("webhook")
token = payload.get("token")

if not webhook_url or not token:
      print("Missing webhook url or token in payload.")
      sys.exit(1)

print(f"Submitting qualifier solution to: {webhook_url}")

# Format the payload for submission
submit_payload = {
      "team_name": "dishakataria15",
      "github_url": "https://github.com/dishakataria15/bfhl-qualifier1-python"
}

headers = {
      "Authorization": f"Bearer {token}",
      "Content-Type": "application/json"
}

try:
      response = requests.post(webhook_url, json=submit_payload, headers=headers)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
except Exception as e:
      print(f"Error making request: {e}")
      sys.exit(1)
