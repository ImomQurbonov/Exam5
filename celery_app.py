from celery import Celery
from skrip import skrin_photo
from web_scraping import get_information

celery = Celery(
    'main',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


@celery.task
def send_information_for_three_hours():
    skrin_photo()
    return get_information()


celery.conf.beat_schedule = {
    'send_information_for_three_hours': {
        'task': 'celery_app.send_information_for_three_hours',
        'schedule': 10800.0
    }
}