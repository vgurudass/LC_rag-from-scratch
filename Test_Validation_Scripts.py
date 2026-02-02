import requests
import os

api_key = "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"
X_TENANT_ID = "Workspace 1"
headers = {"X-API-Key": api_key, "X-Tenant-ID": X_TENANT_ID}

try:
    response = requests.get(
        "https://api.smith.langchain.com/api/v1/sessions",
        headers=headers,
        timeout=5
    )
    if response.status_code == 200:
        print("✓ LangSmith API key is working!")
    else:
        print(f"✗ API key error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"✗ Connection error: {e}")