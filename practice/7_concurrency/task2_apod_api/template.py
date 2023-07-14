import os
import requests
from concurrent.futures import ThreadPoolExecutor

API_KEY = "NkcqMmE1Vy24Y4p3gyvu4j6jqGoi43dZXl6VKfLz"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    """
    Get APOD metadata for a range of dates
    """
    metadata = []
    url = f"{APOD_ENDPOINT}?api_key={api_key}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        metadata = response.json()
    return metadata


def download_image(entry):
    """
    Download an image from the given URL and save it to the specified output path
    """
    date = entry['date']
    url = entry['url']
    output_path = os.path.join(OUTPUT_IMAGES, f"{date}.jpg")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)


def download_apod_images(metadata: list):
    """
    Download APOD images concurrently
    """
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    with ThreadPoolExecutor() as executor:
        executor.map(download_image, (entry for entry in metadata if entry.get('media_type') == 'image'))


def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()