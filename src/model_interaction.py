import requests
import json

def call_model(
    prompt,
    model="orca-mini",
    stream=False,
) :
    url = 'http://localhost:11434/api/generate'
    
    payload = {
    "model": model,
    "prompt": prompt,
    "stream": stream,
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try :
        response = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
        )
    except Exception as e :
        raise(e)
        
    return response.json()