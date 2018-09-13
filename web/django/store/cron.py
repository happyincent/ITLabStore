from django_cron import CronJobBase, Schedule

from .views import updateDB

class CronJob_updateDB(CronJobBase):
    RUN_EVERY_MINS = 15
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
    code = 'store.cron.CronJob_updateDB'

    def do(self):
        updateDB()