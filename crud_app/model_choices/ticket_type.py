from django.db import models


# Ticket Type Choices
class TicketType(models.Choices):
    SOFTWARE = 'software'
    HARDWARE = 'hardware'
    CONNECTION = 'connection'
    