from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.forms import DateInput, SelectDateWidget, ModelForm

from .models import Patient, Notes, info, systematique, VisiteReprise, VisiteMedicaleSpontanee, Analyse, surveillance, \
    Laboratoire

User=get_user_model()
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'date_naissance', 'date_debut', 'age', 'origine', 'entreprise', 'adresse', 'poste_de_travail', 'situation_familiale', 'risque', 'service', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper le nom', 'style': 'width: 600px'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','style': 'width: 600px'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','style': 'width: 600px'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'taper l\'age','style': 'width: 600px'}),
            'origine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper l\'origine','style': 'width: 600px'}),
            'entreprise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper l\'entreprise','style': 'width: 600px'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'taper l\'adresse','style': 'width: 600px'}),
            'poste_de_travail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper la position','style': 'width: 600px'}),
            'situation_familiale': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper la situation familiale','style': 'width: 600px'}),
            'risque': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'taper les riques','style': 'width: 600px'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'taper le service','style': 'width: 600px'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class NotesForm(ModelForm):
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Enter Title"
    }))
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Enter Notes", "rows":"8"
    }))
    class Meta:
        model = Notes
        fields = ['heading', 'text']



class InfoForm(forms.ModelForm):
    class Meta:
        model = info
        fields = [ 'groupe_singuins', 'situation_militaire', 'maladies', 'intervention_chirurgicales', 'accidents', 'accidents_travail', 'maladies_prof', 'compagnes',
                  'blessures', 'IPP', 'ant_pere', 'ant_mere', 'ant_freres', 'ant_soeurs', 'ant_conjoint', 'ant_enfant', 'ant_professionneles', 'variole', 'diphterie', 'tetanos',
                  'tab', 'tabdt', 'autres', 'serum']
        labels = {
            'groupe_singuins': 'Groupe Sanguin',
            'situation_militaire': 'Situation Militaire',
            'maladies': 'Maladies',
            'intervention_chirurgicales': 'Interventions Chirurgicales',
            'accidents': 'Accidents',
            'accidents_travail': 'Accidents de Travail',
            'maladies_prof': 'Maladies Professionnelles',
            'compagnes': 'Compagnes',
            'blessures': 'Blessures',
            'IPP': 'IPP',
            'ant_pere': 'Antécédents Père',
            'ant_mere': 'Antécédents Mère',
            'ant_freres': 'Antécédents Frères',
            'ant_soeurs': 'Antécédents Sœurs',
            'ant_conjoint': 'Antécédents Conjoint',
            'ant_enfant': 'Antécédents Enfant',
            'ant_professionneles': 'Antécédents Professionnels',
            'variole': 'Variole',
            'diphterie': 'Diphtérie',
            'tetanos': 'Tétanos',
            'tab': 'Tab',
            'tabdt': 'Tab DT',
            'autres': 'Autres',
            'serum': 'Sérum',}
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your numero here',
            }),
            'groupe_singuins': forms.Select(attrs={
                'class': 'form-control',
            }),
            'situation_militaire':forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'maladies': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'intervention_chirurgicales': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'accidents': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'accidents_travail': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'maladies_prof': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'compagnes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'blessures': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'IPP': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_pere': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_mere': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_freres': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_soeurs': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_conjoint': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_enfant': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ant_professionneles': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'variole': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'diphterie': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tetanos': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tab': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tabdt': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'autres': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'serum': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class SystematiqueForm(forms.ModelForm):

    analyses = forms.ModelMultipleChoiceField(
            queryset=Analyse.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
            required=False
        )


    class Meta:
        model = systematique
        fields = ['analyses','date', 'denture', 'audition_od', 'audition_og', 'vision_od', 'vision_og', 'taille', 'poids', 'per_thor', 'cap_resp', 'peau_phaneres',
                  'locomateur', 'dynamometre', 'respiratoire', 'radioscopique', 'vaisseaux', 'varices', 'coeur', 'gangalions', 'pouls', 'TA', 'abdomen',
                  'foie', 'bouche', 'rate', 'cicatrice', 'blenno', 'regles', 'neuro_psychisme', 'nervosisme', 'tremblement', 'equilibre', 'romberg',
                  'reflxes_oc', 'reflexes_trend', 'cutt', 'sedimenation', 'crachat', 'selle', 'urines', 'sang', 'situation', 'surveiller', 'commentaire']

        widgets = {

            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'denture': forms.TextInput(attrs={'class': 'form-control'}),
            'audition_od': forms.TextInput(attrs={'class': 'form-control'}),
            'audition_og': forms.TextInput(attrs={'class': 'form-control'}),
            'vision_od': forms.TextInput(attrs={'class': 'form-control'}),
            'vision_og': forms.TextInput(attrs={'class': 'form-control'}),
            'taille': forms.TextInput(attrs={'class': 'form-control'}),
            'poids': forms.TextInput(attrs={'class': 'form-control'}),
            'per_thor': forms.TextInput(attrs={'class': 'form-control'}),
            'cap_resp': forms.TextInput(attrs={'class': 'form-control'}),
            'peau_phaneres': forms.TextInput(attrs={'class': 'form-control'}),
            'locomateur': forms.TextInput(attrs={'class': 'form-control'}),
            'dynamometre': forms.TextInput(attrs={'class': 'form-control'}),
            'respiratoire': forms.TextInput(attrs={'class': 'form-control'}),
            'radioscopique': forms.TextInput(attrs={'class': 'form-control'}),
            'vaisseaux': forms.TextInput(attrs={'class': 'form-control'}),
            'varices': forms.TextInput(attrs={'class': 'form-control'}),
            'coeur': forms.TextInput(attrs={'class': 'form-control'}),
            'gangalions': forms.TextInput(attrs={'class': 'form-control'}),
            'pouls': forms.TextInput(attrs={'class': 'form-control'}),
            'TA': forms.TextInput(attrs={'class': 'form-control'}),
            'abdomen': forms.TextInput(attrs={'class': 'form-control'}),
            'foie': forms.TextInput(attrs={'class': 'form-control'}),
            'bouche': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'cicatrice': forms.TextInput(attrs={'class': 'form-control'}),
            'blenno': forms.TextInput(attrs={'class': 'form-control'}),
            'regles': forms.TextInput(attrs={'class': 'form-control'}),
            'neuro_psychisme': forms.TextInput(attrs={'class': 'form-control'}),
            'nervosisme': forms.TextInput(attrs={'class': 'form-control'}),
            'tremblement': forms.TextInput(attrs={'class': 'form-control'}),
            'equilibre': forms.TextInput(attrs={'class': 'form-control'}),
            'romberg': forms.TextInput(attrs={'class': 'form-control'}),
            'reflxes_oc': forms.TextInput(attrs={'class': 'form-control'}),
            'reflexes_trend': forms.TextInput(attrs={'class': 'form-control'}),
            'cutt': forms.TextInput(attrs={'class': 'form-control'}),
            'sedimenation': forms.TextInput(attrs={'class': 'form-control'}),
            'crachat': forms.TextInput(attrs={'class': 'form-control'}),
            'selle': forms.TextInput(attrs={'class': 'form-control'}),
            'urines': forms.TextInput(attrs={'class': 'form-control'}),
            'analyses': forms.Select(attrs={'class': 'form-control'}),
            'sang': forms.Select(attrs={'class': 'form-control'}),
            'situation': forms.Select(attrs={'class': 'form-control'}),
            'surveiller': forms.Select(attrs={'class': 'form-control'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }



class VisiteRepriseForm(forms.ModelForm):
    class Meta:
        model = VisiteReprise
        fields = ['choix', 'texte_certificat']
        widgets = {
            'choix': forms.RadioSelect(choices=VisiteReprise.CHOICES),

            'texte_certificat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class VisiteMedicaleSpontaneeForm(forms.ModelForm):
    class Meta:
        model = VisiteMedicaleSpontanee
        fields = ['patient', 'date_visite', 'temperature', 'tension_arterielle', 'symptomes', 'observations']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control', 'style': 'width: 600px'}),
            'date_visite': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 600px'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the temperature', 'style': 'width: 600px'}),
            'tension_arterielle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la tension artérielle', 'style': 'width: 600px'}),
            'symptomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez les symptômes', 'style': 'width: 600px'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez les observations', 'style': 'width: 600px'}),
        }




class SurveillanceForm(forms.ModelForm):
    class Meta:
        model = surveillance
        fields = ['date','taille','poids','T_A','A_V','pouls','Glycemie','Albumin','Glucose','Medecin_de_travail']

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date','style': 'width: 600px'}),  # Utiliser un sélecteur de date
            'taille': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'poids': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'T_A': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'A_V': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'pouls': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Glycemie': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Albumin': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Glucose': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Medecin_de_travail': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nom du médecin de travail','style': 'width: 600px'}),
            # Utiliser un champ de texte avec un placeholder
        }


class LaboratoireForm(forms.ModelForm):
    class Meta:
        model = Laboratoire
        fields = ['fichier']
