import time
import requests
import concurrent.futures

# image urls to download from
img_urls = ["https://images.unsplash.com/photo-1570051008600-b34baa49e751",
            "https://images.unsplash.com/photo-1586810724476-c294fb7ac01b",
            "https://images.unsplash.com/photo-1578645635737-6a88e706e0f1",
            "https://images.unsplash.com/photo-1593696954577-ab3d39317b97"]

# store start time
start = time.perf_counter()


def download_img(target_url):
    img_bytes = requests.get(target_url).content
    img_name = target_url.split("/")[3] + ".jpg"

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        return f"{img_name} was downloaded"


# without CM
"""
executor = concurrent.futures.ThreadPoolExecutor()
futures = [executor.submit(download_img, img_url) for img_url in img_urls]
"""

# with CM
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_img, img_url) for img_url in img_urls]

for f in concurrent.futures.as_completed(futures):
    print(f.result())

# store finish time
finish = time.perf_counter()
# calculate main script's runtime
print(f"\n *** Finished in {(finish - start)} seconds *** \n")
