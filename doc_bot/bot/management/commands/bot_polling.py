from django.core.management.base import BaseCommand
from telegram.ext import Updater
from django.conf import settings
from bot.core import BotInfo


class Command(BaseCommand):
    help = 'Запускает polling telegram бота'

    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_BOT_KEY)
        bot_info = BotInfo()
        bot_info.set_dispatcher(updater)
        bot_info.set_job_queue(updater)
        updater.start_polling()
        self.stdout.write(self.style.SUCCESS('Successfully started pool boot'))