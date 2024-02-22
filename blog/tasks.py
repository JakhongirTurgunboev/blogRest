from celery import shared_task

from .models import Blog


@shared_task()
def task_execute(job_params):

    blog = Blog.objects.get(pk=job_params["db_id"])

    #assignment.sum = assignment.first_term + assignment.second_term

    #assignment.save()