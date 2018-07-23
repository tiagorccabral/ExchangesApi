import time

from django.core.management.base import BaseCommand

from features.orderbooks.tasks import save_order_books

# Time of sleep between every request
SLEEP_TIME = 1

# Time of sleep in the case of a exception detected
SLEEP_EXCEPTION_TIME = 10


class Command(BaseCommand):

    def _make_save_request(self):
        try:
            save_order_books()
        except TimeoutError as e:
            time.sleep(SLEEP_EXCEPTION_TIME)
            print("Erro! Esperando " + str(SLEEP_EXCEPTION_TIME) + " segundo(s). Mensagem: " + str(e))
            save_order_books()
        print("Salvo! Esperando " + str(SLEEP_TIME) + " segundo(s).")
        time.sleep(SLEEP_TIME)
        self.handle()

    def handle(self, *args, **options):
        print("Salvando dados...")
        self._make_save_request()