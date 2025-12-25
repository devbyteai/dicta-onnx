# dicta-onnx

Add diacritics to Hebrew text using [Dicta model](https://huggingface.co/dicta-il/dictabert-large-char-menaked)

See [model card](https://huggingface.co/dicta-il/dictabert-large-char-menaked) on HuggingFace 🤗

## Features

- Fast: 0.1s per sentnece (macOS M1) 🚀
- Batching: Supports multiple sentences at once 📚
- User friendly: Add diacritics with just 2 lines of code ✨
- Lightweight: Runs with onnx without heavy dependencies 🛠️
- Dual mode: Output niqqud male (fully marked) and niqqud haser 💡

## Install

```console
pip install -U dicta-onnx
```

## Usage

```python
from dicta_onnx import Dicta

# Model auto-downloads on first use (~1.2GB to ~/.cache/dicta/)
dicta = Dicta()

text = "שלום עולם"
result = dicta.add_diacritics(text)
print(result)  # שָׁלוֹם עוֹלָם
```

### Custom model path

```python
# Use environment variable
# export DICTA_MODEL_PATH=/path/to/dicta-1.0.onnx

# Or pass directly
dicta = Dicta(model_path="./dicta-1.0.onnx")
```

See more examples in [examples](examples) folder

## Play

You can play with dicta-onnx in this [HuggingFace Space](https://huggingface.co/spaces/thewh1teagle/add-diacritics-in-hebrew)

## Credits

Special thanks ❤️ to [dicta-il](https://huggingface.co/dicta-il/dictabert-large-char-menaked) for their amazing Hebrew diacritics model! ✨
