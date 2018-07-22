import time

from django.core.management.base import BaseCommand

from features.orderbooks.tasks import save_order_books

# Time of sleep between every request
SLEEP_TIME = 3


class Command(BaseCommand):

    def _make_save_request(self):
        save_order_books()
        print("Salvo! Esperando " + str(SLEEP_TIME) + " segundo(s).")
        time.sleep(SLEEP_TIME)
        self.handle()

    def handle(self, *args, **options):
        print("Salvando dados...")
        self._make_save_request()