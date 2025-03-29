import requests


url = "http://127.0.0.1:5000/predict"


test_queries = [
    "I want a refund for my last order.",
    "How do I change my billing address?",
    "My network is very slow. Please fix it!",
    "Thank you for the excellent service!",
    "I have an issue with my payment."
]

for query in test_queries:
    response = requests.post(url, json={"text": query})
    
    # Display the response
    if response.status_code == 200:
        print(f"Query: {query}")
        print(f"Predicted Category: {response.json()['category']}")
        print("-" * 50)
    else:
        print(f"Failed to get a response for: {query}")
