from core.use_case import BaseUseCase
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings


class UseCaseImage(BaseUseCase):
    """ЮзКейс для формирования картинки с кодом."""

    def __create_image(self, size, bg_color, message, font, font_color) -> Image:
        """Функция для создания изображений (центровка кода)."""
        W, H = size
        image = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(image)
        _, _, w, h = draw.textbbox((0, 0), message, font=font)
        draw.text(((W - w) / 2, (H - h) / 2), message, font=font, fill=font_color)
        return image

    def execute(self, code_for_file) -> Image:
        size = (300, 300)
        font = ImageFont.truetype(f"{settings.STATIC_DIR}/fonts/Roboto-Bold.ttf", 45)
        color_text = (35, 81, 247)
        img = self.__create_image(size, (255, 255, 255), code_for_file, font, color_text)
        img.save("code_for_user.png")
        return img
