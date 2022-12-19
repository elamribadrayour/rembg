from typing import Tuple

from PIL import Image
import streamlit
from rembg import remove


def remove_background(
    image: Image,
    color: Tuple
):
    """Replace background by a unified color."""
    outputs = Image.new('RGB', image.size, color)
    mask = remove(data=image)
    outputs.paste(mask, (0, 0), mask)
    return outputs


def load_image(image_file):
    """Load an image."""
    image = Image.open(image_file)
    return image


streamlit.markdown("## Upload an image")

image_file = streamlit.file_uploader(
    label="image uploader",
    label_visibility="collapsed",
)

streamlit.markdown("## Choose a background color")

columns = streamlit.columns(3)
with columns[1]:
    color = streamlit.color_picker(
        label="color picker",
        label_visibility="collapsed",
    ).lstrip('#')
    rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

if image_file is None:
    streamlit.stop()

image = load_image(image_file=image_file)
streamlit.markdown("## Input image")
streamlit.image(image)
output = remove_background(image, color=rgb_color)
streamlit.markdown("## Output image")
streamlit.image(output)
