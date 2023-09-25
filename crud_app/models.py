from django.db import models

from .model_choices.account_types import AccountTypes
from .model_choices.branches import Branches
from .model_choices.status import Status
from .model_choices.ticket_type import TicketType


class Account(models.Model):
    """
        Accounts Model For Registration and Login
    """
    
    # Columns
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    account_type = models.CharField(
        max_length=10,
        default=AccountTypes.USER_ACCT,
        choices=AccountTypes.choices,
    )
    account_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.username}: {self.account_type}'
        
    
    # Filter out account type to "user" if not within the account type 
    # choices enumeration
    def save(self, *args, **kwargs):
        if self.account_type not in dict(AccountTypes.choices).keys():
            self.account_type = AccountTypes.USER_ACCT
            
        super().save(*args, **kwargs)
        

class Ticket(models.Model):
    """
        Ticket Request Model
    """
    
    # Columns
    ticket_id = models.BigIntegerField(primary_key=True)
    account_type = models.ForeignKey(Account, on_delete=models.CASCADE)
    ticket_created = models.DateTimeField(auto_now_add=True)
    ticket_details = models.CharField(max_length=200)
    
    branches = models.CharField(
        max_length=50,
        default=Branches.Juan_Sumulong,
        choices=Branches.choices,
    )
    
    status = models.CharField(
        max_length=20,
        default=Status.PENDING,
        choices=Status.choices,
    )
    
    ticket_type = models.CharField(
        max_length=10,
        default=TicketType.SOFTWARE,
        choices=TicketType.choices,
    )
    
    problem = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Ticket Request No.: {self.ticket_id}"
    

class Equipment(models.Model):
    """
        Equipment model
    """
    
    # Columns
    ticket_request = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    
    owner = models.CharField(max_length=50)
    equipments = models.CharField(max_length=100)
    details = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.equipments
    