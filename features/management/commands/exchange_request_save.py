import time

from django.core.management.base import BaseCommand

from features.orderbooks.tasks import save_order_books

# Time of sleep between every request
SLEEP_TIME = 1

# Time of sleep in the case of a exception detected
SLEEP_EXCEPTION_TIME = 10


class Command(BaseCommand):

    def _make_save_request(self):
        result = save_order_books()
        if not result:
            print("Erro! Esperando " + str(SLEEP_EXCEPTION_TIME) + " segundo(s). Mensagem: ")
            time.sleep(SLEEP_EXCEPTION_TIME)
            return;
        else:
            print("Salvo! Esperando " + str(SLEEP_TIME) + " segundo(s).")
            time.sleep(SLEEP_TIME)
            return;

    def handle(self, *args, **options):
        while True:
            print("Salvando dados...")
            self._make_save_request()
