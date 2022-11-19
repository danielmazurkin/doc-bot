from abc import abstractmethod


class BaseUseCase:
    """Базовый класс юзкейза."""

    @classmethod
    @abstractmethod
    def execute(cls, *args, **kwargs):
        """Основной метод юзкейза."""
        ...
