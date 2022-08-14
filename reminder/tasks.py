from celery import shared_task

@shared_task
def reminder_update()