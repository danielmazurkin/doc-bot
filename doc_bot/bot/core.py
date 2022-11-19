

class BotInfo:

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
