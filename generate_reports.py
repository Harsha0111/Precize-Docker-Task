import requests
import time

def fetch_top_downloaded_models():
    # Fetch data from Hugging Face model hub API
    response = requests.get("https://huggingface.co/api/models?sort=downloads")
    if response.status_code == 200:
        # Extract information about top downloaded models
        top_models = response.json()[:10]
        return top_models
    else:
        print("Failed to fetch data from Hugging Face model hub API.")
        return None

def print_top_downloaded_models(top_models):
    if top_models:
        print("Top 10 Downloaded Models:")
        for model in top_models:
            print(model)
    else:
        print("No data to print.")

while True:
    top_models = fetch_top_downloaded_models()
    print_top_downloaded_models(top_models)
    # Wait for 2 minutes before fetching data again
    time.sleep(120)
