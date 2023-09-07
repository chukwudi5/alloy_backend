from dotenv import load_dotenv
import requests
import os
load_dotenv()

def get_alloy_summary(request):
    api_url = 'https://sandbox.alloy.co/v1/evaluations'
    data = request

    username = os.getenv('WORKFLOW_TOKEN')
    password = os.getenv('WORKFLOW_SECRET')
    auth = (username, password)
    
    try:
        response = requests.post(api_url, data=data, auth=auth)
        if response.status_code == 201:
            result = response.json
    except requests.exceptions.RequestException as e:
        #Handle error
        print(e)

    return result.summary.outcome