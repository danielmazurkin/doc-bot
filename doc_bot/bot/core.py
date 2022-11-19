from telegram.ext import CommandHandler
from bot.handlers import start_callback


class BotInfoWorker:

    def __init__(self):
        self.dp = None
        self.jq = None

    def get_dispatcher(self):
        """Получить диспетчер бота."""
        return self.dp

    def set_dispatcher(self, updater):
        """Установить диспетчер бота."""
        self.dp = updater.dispatcher

    def get_job_queue(self):
        """Получить очередь задач."""
        return self.jq

    def set_job_queue(self, updater):
        """Установить очередь задач."""
        self.jq = updater.job_queue

    def setup_handlers(self):
        """Устанавливает обработчики."""
        dp = self.get_dispatcher()
        dp.add_handler(CommandHandler("start", start_callback))

