import numpy as np
import cv2
import os

def predict(img: np.ndarray, model_path: str) -> np.ndarray:

    model_path = os.path.abspath(model_path)
    model = np.load(model_path)
    img = (img - model[0]) / model[1]
    return img


def train(img: np.ndarray, save_model_path: str) -> None:

    save_model_path = os.path.abspath(save_model_path)
    parameters = np.array([np.mean(img), np.std(img)])
    np.save(save_model_path, parameters)