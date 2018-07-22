from django_cron import CronJobBase, Schedule

from features.orderbooks.tasks import save_order_books


def SaveExchangeDataJob():

    save_order_books()


class RequestExchangesDataJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'orderbooks.save_exchanges_orderbook_data'    # identifier code

    def do(self):
        save_order_books()