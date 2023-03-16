from django.db import models
from django.contrib.auth.models import User

class Uczen(models.Model):
    class Klasy(models.TextChoices):
        JAN = "1", "1LOA"
        FEB = "2", "1LOB"
        MAR = "3", "2LO"
    user1 = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.CharField(max_length=10,choices=Klasy.choices,default=Klasy.JAN)

    def __str__(self):
        return f'{self.user1.first_name}'

class Nauczyciel(models.Model):
    class Klasy(models.TextChoices):
        JAN = "1", "1LOA"
        FEB = "2", "1LOB"
        MAR = "3", "2LO"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.CharField(max_length=10,choices=Klasy.choices,default=Klasy.JAN)

    def __str__(self):
        return f'{self.user.first_name}'    

class Poprawa(models.Model):
    class Przedmiot(models.TextChoices):
        Biologia =  "Biologia"
        Chemia =  "Chemia"
        Filozofia = "Filozofia"
        Fizyka =  "Fizyka"
        Geografia=  "Geografia"
        Historia =  "Historia"
        Historia_i_teraźniejszość =  "Historia i teraźniejszość"
        Informatyka =  "Informatyka"
        Język_angielski =  "Język angielski"
        Języka_polski =  "Języka polski"
        Język_hiszpański =  "Język hiszpański"
        Język_niemiecki =  "Język niemiecki"
        Matematyka =  "Matematyka"
        Projekt_społeczny =  "Projekt społeczny"
        Religia =  "Religia"
        Wychowanie_fizyczne =  "Wychowanie fizyczne"
        
    user1 = models.ForeignKey(Uczen, null=True,on_delete=models.SET_NULL)
    temat =models.CharField(max_length=50)
    przedmiot = models.CharField(max_length=60,choices=Przedmiot.choices,default=Przedmiot.Chemia)
    nauczyciel = models.ForeignKey(Nauczyciel, null=True,on_delete=models.SET_NULL)
    data  = models.CharField(max_length=50, default='')
    def __str__(self):
        return f'{self.user1}'