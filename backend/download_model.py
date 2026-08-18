import os
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "road_damage_detector.h5"
)

MODEL_URL = os.getenv("MODEL_URL")


def download_model():

    os.makedirs(MODEL_DIR, exist_ok=True)

    if os.path.exists(MODEL_PATH):
        print("Model already exists.")
        return

    if not MODEL_URL:
        raise RuntimeError(
            "MODEL_URL environment variable is not set."
        )

    print("Downloading CNN model...")

    urllib.request.urlretrieve(
        MODEL_URL,
        MODEL_PATH
    )

    print("Model downloaded successfully.")


if __name__ == "__main__":
    download_model()