from django.db import models


# Account Type Choices
class AccountTypes(models.Choices):
    ADMIN_ACCT = 'admin'
    TECHNICAL_ACCT = 'technical'
    USER_ACCT = 'user'
    