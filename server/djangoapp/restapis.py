import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
    
        # For each dealer object
        for dealer in json_result:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
            id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
            short_name=dealer_doc["short_name"],
            st=dealer_doc["st"], zip=dealer_doc["zip"],state=dealer_doc["state"])
            results.append(dealer_obj)

    return results

def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    json_result = get_request(url,dealerId=dealerId)
    
    if json_result:
        for review_doc in jason_result:
            dealerReview_obj = DealerReview(
                dealership=review_doc["dealership"],
                name=review_doc["name"],
                purchase=review_doc["purchase"],
                review=review_doc["review"],
                purchase_date=review_doc["purchase_date"],
                car_make=review_doc["car_make"],
                car_model=review_doc["car_model"],
                car_year=review_doc["car-year"],
                sentiment="NULL",
                id=review_doc["id"])

            dealerReview_obj.sentiments(dealerReview_obj.review)
            results.append(dealer_Review_obj)


def get_dealer_by_id_from_cf(url, dealerId):
    # Call get_request with a URL parameter
    json_result = get_request(url,dealerId=dealerId)
    if json_result:
        # For each dealer object
        for dealer_doc in json_result:
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
            id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
            short_name=dealer_doc["short_name"],
            st=dealer_doc["st"], zip=dealer_doc["zip"],state=dealer_doc["state"])

    return dealer_obj
def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url,dealerId=dealerId)
    if json_result:
        # For each dealer object
        for review_doc in json_result:
            dealerReview_obj = DealerReview(
                dealership=review_doc["dealership"], 
                name=review_doc["name"], 
                purchase=review_doc["purchase"],
                review=review_doc["review"], 
                purchase_date=review_doc["purchase_date"], 
                car_make=review_doc["car_make"], 
                car_model=review_doc["car_model"],
                car_year=review_doc["car_year"], 
                sentiment="NULL", 
                id=review_doc["id"])

            
            results.append(dealerReview_obj)

    return results

def get_dealer_by_state_from_cf(url,state):
    results = []
    json_result = get_request(url, state=state)
    if json_result:
        for dealer in json_result:
            dealer_doc = dealer["doc"]
            dealer_obj = CarDealer(address=dealer_doc["address"],city=dealer_doc["city"], full_name=dealer+doc["full_name"],
            id=dealer_doc["id"], lat=dealer_doc["lat"],long=dealer_doc["long"],
            short_name=dealer_doc["short_name"],
            st=dealer_doc["st"],zip=dealer_doc["zip"], state=dealer_doc["state"])
            results.append(dealer_obj)
    return results
# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



