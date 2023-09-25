from django.db import models


# Branch Choices
class Branches(models.Choices):
    Juan_Sumulong = "Juan Sumulong Campus"
    Apolinario_Mabini = "Apolinario Mabini Campus"
    Andres_Bonifacio = "Andres Bonifacio Campus"
    Jose_Abad = "Jose Abad Campus"
    Jose_Rizal = "Jose Rizal Campus"
    Elisa_Esguerra = "Elisa Esguerra Campus"
    Plaridel = "Plaridel Campus"
    