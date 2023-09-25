from django.db import models


# Status Choices
class Status(models.Choices):
    PENDING = 'Pending'
    ON_GOING = 'Ongoing'
    COMPLETE = 'Complete'
    