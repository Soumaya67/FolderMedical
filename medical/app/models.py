import datetime
import token

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_medecin = models.BooleanField('Is medecin', default=False)
    is_infermier = models.BooleanField('Is infermier', default=False)
    def save(self, *args, **kwargs):
        # Call make_password before saving the user to hash the password
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Patient(models.Model):
    nom=models.CharField(max_length=45)
    date_naissance=models.DateField()
    age=models.IntegerField()
    origine=models.CharField(max_length=45)
    adresse=models.TextField(max_length=100)
    situation_familiale=models.CharField(max_length=45)
    entreprise=models.CharField(max_length=45)
    date_debut=models.DateField()
    service=models.CharField(max_length=45)
    poste_de_travail=models.CharField(max_length=45)
    risque=models.TextField(max_length=100)
    photo = models.ImageField(upload_to='user_photos/')
    #def __str__(self):
        #return self.nom +self.date_naissance+self.date_debut+self.age+self.origine+self.entreprise+self.adresse+self.poste_de_travail+self.situation_familiale+self.risque+self.service

##################################################"""

class Notes(models.Model):
    STATUS = (
        ("new", "NEWEST"),
        ("old", "OLDEST"),
        ("title", "TITLE"),
    )
    heading = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default="old")
    def __str__(self):
        return self.heading

###########Dossier medcial#######################"

class info(models.Model):
    singuins = (
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )

    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    groupe_singuins=models.CharField(max_length=3, choices=singuins, default='RAS')
    situation_militaire=models.CharField(max_length=40, default='RAS')
    maladies=models.CharField(max_length=40,default='RAS')
    intervention_chirurgicales = models.CharField(max_length=10, default='RAS')
    accidents = models.CharField(max_length=40, default='RAS')
    accidents_travail = models.CharField(max_length=40, default='RAS')
    maladies_prof = models.CharField(max_length=40, default='RAS')
    compagnes = models.CharField(max_length=40, default='RAS')
    blessures = models.CharField(max_length=40, default='RAS')
    IPP = models.CharField(max_length=40, default='RAS')
    ant_pere = models.CharField(max_length=40, default='RAS')
    ant_mere = models.CharField(max_length=40, default='RAS')
    ant_freres = models.CharField(max_length=40, default='RAS')
    ant_soeurs = models.CharField(max_length=40, default='RAS')
    ant_conjoint = models.CharField(max_length=40, default='RAS')
    ant_enfant = models.CharField(max_length=40, default='RAS')
    ant_professionneles = models.CharField(max_length=40, default='RAS')
    #vaccination
    variole=models.CharField(max_length=10,default='RAS')
    diphterie=models.CharField(max_length=10,default='RAS')
    tetanos=models.CharField(max_length=10,default='RAS')
    tab = models.CharField(max_length=10, default='RAS')
    tabdt= models.CharField(max_length=10, default='RAS')
    autres = models.CharField(max_length=10, default='RAS')
    serum = models.CharField(max_length=10, default='RAS')


class Analyse(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class systematique(models.Model):
    SANG_CHOICES = (
        ('GB', 'GB'),
        ('HB', 'HB'),
        ('plq', 'plq'),
        ('lympho', 'lympho'),
    )

    SITUATION_CHOICES = (
        ('apte', 'apte'),
        ('inapte', 'inapte'),
        ('inapte_temp', 'inapte temporairement'),
    )

    SURVEILLANCE_CHOICES = (
        ('1mois', '1 mois'),
        ('2mois', '2 mois'),
        ('3mois', '3 mois'),
        ('4mois', '4 mois'),
        ('5mois', '5 mois'),
        ('6mois', '6 mois'),
        ('7mois', '7 mois'),
        ('8mois', '8 mois'),
        ('9mois', '9 mois'),
        ('10mois', '10 mois'),
        ('11mois', '11 mois'),
        ('12mois', '12 mois'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    analyses = models.ManyToManyField(Analyse, blank=False)
    date= models.DateField(default=datetime.date.today)
    denture = models.CharField(max_length=20, default='RAS')
    audition_od = models.CharField(max_length=20, default='RAS')
    audition_og = models.CharField(max_length=20, default='RAS')
    vision_od = models.CharField(max_length=20, default='RAS')
    vision_og = models.CharField(max_length=20, default='RAS')
    taille = models.CharField(max_length=20, default='RAS')
    poids = models.CharField(max_length=20, default='RAS')
    per_thor = models.CharField(max_length=20, default='RAS')
    cap_resp = models.CharField(max_length=20, default='RAS')
    peau_phaneres = models.CharField(max_length=20, default='RAS')
    locomateur = models.CharField(max_length=20, default='RAS')
    dynamometre = models.CharField(max_length=20, default='RAS')
    respiratoire = models.CharField(max_length=20, default='RAS')
    radioscopique = models.CharField(max_length=20, default='RAS')
    vaisseaux = models.CharField(max_length=20, default='RAS')
    varices = models.CharField(max_length=20, default='RAS')
    coeur = models.CharField(max_length=20, default='RAS')
    gangalions = models.CharField(max_length=20, default='RAS')
    pouls = models.CharField(max_length=20, default='RAS')
    TA = models.CharField(max_length=20, default='RAS')
    abdomen = models.CharField(max_length=20, default='RAS')
    foie = models.CharField(max_length=20, default='RAS')
    bouche = models.CharField(max_length=20, default='RAS')
    rate = models.CharField(max_length=20, default='RAS')
    cicatrice = models.CharField(max_length=20, default='RAS')
    blenno = models.CharField(max_length=20, default='RAS')
    regles = models.CharField(max_length=20, default='RAS')
    neuro_psychisme = models.CharField(max_length=20, default='RAS')
    nervosisme = models.CharField(max_length=20, default='RAS')
    tremblement = models.CharField(max_length=20, default='RAS')
    equilibre = models.CharField(max_length=20, default='RAS')
    romberg = models.CharField(max_length=20, default='RAS')
    reflxes_oc = models.CharField(max_length=20, default='RAS')
    reflexes_trend = models.CharField(max_length=20, default='RAS')
    cutt = models.CharField(max_length=20, default='RAS')
    sedimenation = models.CharField(max_length=20, default='RAS')
    crachat = models.CharField(max_length=20, default='RAS')
    selle = models.CharField(max_length=20, default='RAS')
    urines = models.CharField(max_length=20, default='RAS')
    sang = models.CharField(max_length=20, choices=SANG_CHOICES, default='RAS')
    situation = models.CharField(max_length=20, choices=SITUATION_CHOICES, default='RAS')
    surveiller = models.CharField(max_length=20, choices=SURVEILLANCE_CHOICES, default='RAS')
    commentaire = models.TextField(max_length=100, default='RAS')



class VisiteReprise(models.Model):
    CHOICES = (
        ('apte', 'L\'employé est apte à reprendre son travail'),
        ('Inapte_t', 'L\'employé est Inapte temporairement à reprendre son travail'),
        ('Inapte_d', 'L\'employé est Inapte définitivement à reprendre son travail'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visites_reprise')
    choix = models.CharField(max_length=10, choices=CHOICES)
    date = models.DateField(default=datetime.date.today)
    texte_certificat = models.TextField()

    # Add other fields as needed

    def __str__(self):
        return f"{self.choix} - {self.date}"


class VisiteMedicaleSpontanee(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_visite = models.DateField()
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    tension_arterielle = models.CharField(max_length=20)
    symptomes = models.TextField()
    observations = models.TextField()

    def __str__(self):
        return self.patient.nom

class surveillance(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.date.today)
    taille=models.DecimalField(max_digits=8, decimal_places=3)
    poids=models.DecimalField(max_digits=8, decimal_places=3)
    T_A=models.DecimalField(max_digits=8, decimal_places=3)
    A_V=models.DecimalField(max_digits=8, decimal_places=3)
    pouls=models.DecimalField(max_digits=8, decimal_places=3)
    Glycemie=models.DecimalField(max_digits=8, decimal_places=3)
    Albumin=models.DecimalField(max_digits=8, decimal_places=3)
    Glucose=models.DecimalField(max_digits=8, decimal_places=3)
    Medecin_de_travail=models.CharField(max_length=20)

# models.py
class Laboratoire(models.Model):
    systematique = models.ForeignKey(systematique, on_delete=models.CASCADE)
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='analyses/')


