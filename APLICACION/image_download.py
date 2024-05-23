import os
import requests

def download_image(image_url, folder_path):
    if image_url != 'N/A':
        image_filename = os.path.join(folder_path, os.path.basename(image_url))
        with requests.get(image_url, stream=True) as img_response:
            if (img_response.status_code == 200):
                with open(image_filename, 'wb') as img_file:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        img_file.write(chunk)
        return image_filename
    return 'N/A'
