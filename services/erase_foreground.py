from typing import Dict, Any
import requests

def erase_foreground(
    api_key: str,
    image_data: bytes,
    content_moderation: bool = False
) -> Dict[str, Any]:

    url = "https://engine.prod.bria-api.com/v1/erase_foreground"

    headers = {
        "api_token": api_key,
        "Accept": "application/json"
    }

    files = {
        "image_file": ("image.png", image_data, "image/png")
    }

    data = {
        "content_moderation": str(content_moderation).lower()
    }

    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Erase foreground failed: {str(e)}")