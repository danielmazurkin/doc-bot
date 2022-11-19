from core.use_case import BaseUseCase
from PIL import Image, ImageDraw


class UseCaseImage(BaseUseCase):
    """ЮзКейс для формирования картинки с кодом."""

    def execute(self, text):
        img = Image.new('RGB', (512, 512), color='white')
        d = ImageDraw.Draw(img)
        d.text((150, 150), text, fill=(255, 255, 0))
        img.save("pil_red.png")
