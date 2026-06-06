import requests

PROJECT_ID = "79648956"
TRIGGER_TOKEN = "glptt-L5kjebEzFLJmNAVGuUGy"

url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/trigger/pipeline"

payload = {
    "token": TRIGGER_TOKEN,
    "ref": "main"
}

response = requests.post(url, data=payload)

print("Status:", response.status_code)
print(response.text)