```python
import requests
from get_influencer_data import influencer_id

# Define the payment gateway API endpoint
PAYMENT_GATEWAY_API = "https://api.paymentgateway.com"

def process_payment(influencer_id):
    # Get influencer data
    influencer_data = get_influencer_data(influencer_id)

    # Prepare the payment data
    payment_data = {
        "amount": influencer_data["payment_amount"],
        "currency": "USD",
        "source": influencer_data["payment_source"],
        "description": f"Payment for influencer {influencer_id}"
    }

    # Send a POST request to the payment gateway API
    response = requests.post(f"{PAYMENT_GATEWAY_API}/payments", data=payment_data)

    # Check the response status
    if response.status_code == 200:
        print(f"Payment for influencer {influencer_id} processed successfully.")
    else:
        print(f"Failed to process payment for influencer {influencer_id}.")
```