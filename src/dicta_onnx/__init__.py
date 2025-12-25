from dicta_onnx.model import OnnxDiacritizationModel
import os
import re

# Model download URL from GitHub releases
MODEL_URL = "https://github.com/thewh1teagle/dicta-onnx/releases/download/model-files-v1.0/dicta-1.0.onnx"
DEFAULT_CACHE_DIR = os.path.expanduser("~/.cache/dicta")


def _get_model_path():
    """Find or download the dicta ONNX model."""
    # 1. Environment variable override
    env_path = os.environ.get('DICTA_MODEL_PATH')
    if env_path and os.path.exists(env_path):
        return env_path

    # 2. Check cache
    cache_path = os.path.join(DEFAULT_CACHE_DIR, "dicta-1.0.onnx")
    if os.path.exists(cache_path):
        return cache_path

    # 3. Download from GitHub releases
    import urllib.request
    os.makedirs(DEFAULT_CACHE_DIR, exist_ok=True)
    print(f"Downloading dicta model to {cache_path}...")
    urllib.request.urlretrieve(MODEL_URL, cache_path)
    print("Download complete.")
    return cache_path


class Dicta:
    def __init__(self, model_path: str = None):
        """
        Initialize the Dicta diacritization model.

        Parameters:
        - model_path (str, optional): Path to the ONNX model file. If not provided,
          the model will be auto-downloaded from GitHub releases to ~/.cache/dicta/
          You can also set the DICTA_MODEL_PATH environment variable.
        """
        if model_path is None:
            model_path = _get_model_path()
        self.model = OnnxDiacritizationModel(model_path)

    def add_diacritics(self, sentences: list | str, mark_matres_lectionis: str | None = None) -> str:
        """
        Adds niqqud (Hebrew diacritics) to the given text.

        Parameters:
        - sentences (list | str): A string or a list of strings to be processed. Each string should not exceed 2048 characters.
        - mark_matres_lectionis (str | None, optional): A string used to mark niqqud male. For example, if set to '|',
            "לִימּוּדָיו" will be returned as "לִי|מּוּדָיו". Default is None (no marking).

        Returns:
        - str: The text with added diacritics.
        """

        if isinstance(sentences, str):
            sentences = [sentences]
        result = self.model.predict(sentences, mark_matres_lectionis=mark_matres_lectionis)
        return result[0]

    def get_niqqud_male(self, text: str, mark_matres_lectionis: str):
        """
        Based on given mark character remove the mark character to keep it as niqqud male
        """
        return text.replace(mark_matres_lectionis, '')

    def get_niqqud_haser(self, text: str, mark_matres_lectionis: str):
        """
        Based on given mark_matres_lectionis remove the niqqud niqqud male character along with the mark character
        """
        return re.sub(r'.\|', '', text) # Remove {char}{matres_lectionis}
