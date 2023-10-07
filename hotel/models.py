from django.db import models

# Create your models here.
distance= [
    ('Flughafen','Flughafen'),
    ('Senzo Mall','Senzo Mall'),
    ('City Center','City Center'),
]
price = [
    ('Günstig','Günstig'),
    ('Mittel','Mittel'),
    ('Teuer','Teuer'),
]
Position = [
    ('Ausßer','Ausßer'),
    ('gut','gut'),
    ('sehr gut','sehr gut'),
]
status = [
    ('Erwachsene','Erwachsene'),
    ('Familien','Familien'),
    ('Familien mit Kinder','Familien mit Kinder'),
    ('Ehepaar','Ehepaar'),    
]
beach = [
    ('Privat','Privat'),
    ('Ohne Strand','Ohne Strand'),
    (' Strand mit Aquapark',' Strand mit Aquapark'),
]
food = [
    ('gut','gut'),
    (' sehr gut',' sehr gut'),
]

class Hotel(models.Model):
    der_Hotelname = models.CharField(max_length=50)
    Entfernung = models.CharField(max_length=50,choices= distance,null = True,blank=True)
    preis = models.CharField(max_length=50,choices= price,null = True,blank=True)
    Lage = models.CharField(max_length=50,choices= Position,null = True,blank=True)
    Passt = models.CharField(max_length=50,choices= status,null = True,blank=True)
    Strand = models.CharField(max_length=50,choices= beach,null = True,blank=True)
    Essen = models.CharField(max_length=50,choices= food,null = True,blank=True)
    Foto = models.ImageField(upload_to='hotel/%y/%m',blank=True,null=True)
    Staat_Stadt = models.CharField(max_length=50)
    
    
    
    
    
    
    
    def __str__(self):
        return self.der_Hotelname