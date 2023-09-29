from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_id(task_id):
        return Tasks.objects.get(id=task_id) if Tasks.objects.filter(id=task_id) else None\


    @staticmethod
    def delete_by_id(task_id):
        if Tasks.get_by_id(task_id) is None:
            return False
        Tasks.objects.get(id=task_id).delete()
        return True

    @staticmethod
    def create(title, description):
        if len(title) > 255:
            return None

        task = Tasks()
        task.title = title
        task.description = description

        task.save()
        return task

    def update(self, title=None, description=None):
        if title is not None:
            self.title = title

        if description is not None:
            self.description = description

        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return list(Tasks.objects.all())
