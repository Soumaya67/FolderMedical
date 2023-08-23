import locale
from datetime import date

import pdfkit as pdfkit
from crispy_forms.layout import HTML
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.checks import Info
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from .form import NotesForm, PatientForm, InfoForm, SystematiqueForm, VisiteRepriseForm, SurveillanceForm, \
    LaboratoireForm
from .models import Notes, Patient, User, Analyse, systematique, info, surveillance, Laboratoire
from django.views.generic import DetailView


def login_view(request):
    msg = ''
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_medecin:
                    return redirect('medecin')
                elif user.is_infermier:
                    return redirect('infermier')
                else:
                    return redirect('admin')
            else:
                msg= 'username ou mot de ou mot de passe incorrecte'
    return render(request, 'registration/login.html', {'msg': msg})

def dashboard(request):
    patient_count = Patient.objects.count()

    medecin_count = User.objects.filter(is_medecin=True).count()

    infermier_count = User.objects.filter(is_infermier=True).count()

    nombre_visites = systematique.objects.filter(laboratoire__isnull=True).count()

    context = {
        'patient_count': patient_count,
        'medecin_count': medecin_count,
        'infermier_count': infermier_count,
        'nombre_visites': nombre_visites,
    }
    return render(request,'Medecin/dashboard.html',context)


def medecin(request):
    return render(request, 'Medecin/medecin.html')

def infermier(request):
    return render(request, 'infermier.html')

def admin(request):
    return render(request, 'admin.html')

def patient_list(request):
   # for i in range(10):
    #    Patient(None,f.name(),f.date(),f.random_int(min=0, max=100),f.name(),f.addres(),f.company(),f.date(),f.text(),f.text()).save()
    patients = Patient.objects.all()
    return render(request, 'Patient/patients.html', {'patients': patients})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None, request.FILES or None )
        if form.is_valid():
            print("Form data:", form.cleaned_data)  # Debug print to check form data
            form.save()
            return redirect('patients')
        else:
            print("Form errors:", form.errors)  # Debug print to check form errors
    else:
        form = PatientForm()

    return render(request, 'Patient/create_patient.html', {'form': form})

def update_patient(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method =='POST':
        form=PatientForm(request.POST or None, request.FILES or None ,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form=PatientForm(instance=patient)
    return render(request,'Patient/update_patient.html',{'form':form,'patient':patient})

def view_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(instance=patient)
    print("Patient PK:", patient.pk)
    return render(request, 'Patient/view_patient.html', {'form': form , 'patient':patient})



def delete_patient(request, pk):
    patient = get_object_or_404(Patient,pk=pk)
    patient.delete()
    return redirect('patients')


def home(request):
    return render(request, 'home.html')

def list_patients(request):
    contact_list = Patient.objects.all()
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

def search(request):
    if 'keyword' in request.GET:
        query = request.GET['keyword']
        patients = Patient.objects.filter(Q(nom__icontains=query) | Q(entreprise__icontains=query) |Q(service__icontains=query)|Q(poste_de_travail__contains=query))
    else:
        patients = Patient.objects.all()
    return render(request, 'Patient/patients.html', {'patients': patients,'query': query})

def list_pat(request):
    all_patients = Patient.object.all()
    paginator = Paginator(all_patients, 5)
    page = request.GET.get('page',1)
    try:
        patients=paginator.page(page)
    except PageNotAnInteger:
        patients=paginator.page(1)
    except EmptyPage:
        patients=paginator.page(paginator.num_pages)
    return render(request,'patients.html',{'patients':patients})




class PatientDetailView(DetailView):
    model = Patient
    template_name = 'view_patient.html'
    context_object_name = 'patient'

###########################################################


def inde(request):
    notes = Notes.objects.all()
    return render(request, "Notes/index.html", {"notes": notes})


def new_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "Notes/update.html", {"form": form})


def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "Notes/update.html", {"note": note, "form": form})


# def delete_note(request, pk):
def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "The note has been deleted")
        return redirect("index")
    return render(request, "Notes/delete.html", {"note": note, "form": form})


def search_page(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        notes = Notes.objects.filter(heading__icontains=search_text) | Notes.objects.filter(text__icontains=search_text)

        return render(request, "Notes/search.html", {"notes": notes})


#########################Dossier medical##################################
def dossier(request):
    return render(request, "dossier/dossier.html")


def patients_without_info_view(request):

    patients_without_info = Patient.objects.filter(info__isnull=True)
    print(patients_without_info)

    context = {
        'patients_without_info': patients_without_info
    }

    return render(request, 'dossier/AjouterDossier.html', context)

def patients_with_info_view(request):

    patients_with_info = Patient.objects.filter(info__isnull=False)
    context = {
        'patients_with_info': patients_with_info
    }

    return render(request, 'dossier/patient_dossier.html', context)

def add_dossier(request):
    return render(request, 'Medecin/medecin.html')



def add_info(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.patient = patient
            info.save()
            return redirect('ajouterdossier')
    else:
        form = InfoForm()
    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'dossier/menu_content1.html', context)

def menu1_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            print("Form data:", form.cleaned_data)
            form.save()
            return redirect('menu1')
        else:
            print("Form errors:", form.errors)
    else:
        form = InfoForm()
    return render(request, 'dossier/menu_content1.html',{'form':form})



def menu3_view(request):
    if request.method == 'POST':
        form = SystematiqueForm(request.POST)
        if form.is_valid():
            print("Form data:", form.cleaned_data)
            form.save()
            return redirect('add_dossier')
        else:
            print("Form errors:", form.errors)
    else:
        form = SystematiqueForm()
    return render(request, 'dossier/VMR.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, VisiteReprise

################################### VMR #################################################################



def visite_reprise(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
    if request.method == 'POST':
        form = VisiteRepriseForm(request.POST)
        if form.is_valid():
            visite = form.save(commit=False)
            visite.patient = patient
            visite.save()
            return redirect('list_reprise', patient_id=patient_id)
            messages.success(request, "La visite de reprise a été enregistrée avec succès.")
        else:
            messages.error(request, "Veuillez remplir tous les champs requis.")
    else:
        form = VisiteRepriseForm(initial={'patient': patient})

    return render(request, 'dossier/VMR/ajouter_vmr.html', {'form': form, 'patient': patient})


def reprise_list(request):
    patients = Patient.objects.all()
    return render(request, 'dossier/VMR/VMR.html', {'patients': patients})

def liste_visites_par_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    visites = patient.visites_reprise.all()

    return render(request, 'dossier/VMR/liste_visite.html', {'patient': patient, 'visites': visites})


def detail_visite_reprise(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(VisiteReprise, patient=patient, date=date_visite)
    visites_patient_date = VisiteReprise.objects.filter(patient=patient, date=date_visite)

    return render(request, 'dossier/VMR/voir_visite.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})

######################analyse#############

def liste_analyses(request):
    analyses = Analyse.objects.all()
    data = [{'id': analyse.id, 'nom': analyse.nom} for analyse in analyses]
    return JsonResponse(data, safe=False)
###############################VMS########################



def ajouter_vms(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = SystematiqueForm(request.POST)
        if form.is_valid():
            new_date = form.cleaned_data['date']
            if systematique.objects.filter(patient=patient, date=new_date).exists():
                form.add_error('date', 'une visite dans la meme date existe déja.')
            else:
                new_systematique = form.save(commit=False)
                new_systematique.patient = patient
                new_systematique.save()


                selected_analyses = form.cleaned_data['analyses']
                new_systematique.analyses.set(selected_analyses)

                return redirect('liste_visite_par_patient', patient_id=patient_id)
        else:
            print("Form errors:", form.errors)
    else:
        form = SystematiqueForm(initial={'patient': patient})

    return render(request, 'dossier/VMS/ajouter_VMS.html', {'form': form, 'patient': patient})

def sys_list(request):
    patients = Patient.objects.all()
    return render(request, 'dossier/VMS/VMS.html', {'patients': patients})

def liste_visite_par_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    visites = patient.systematique_set.all()  # Utilisez la relation "systematique_set" pour récupérer les visites
    url = reverse('liste_visite_par_patient', args=[patient.id])
    return render(request, 'dossier/VMS/liste_vms.html', {'patient': patient, 'visites': visites})

def detail_vms(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(systematique, patient=patient, date=date_visite)
    visites_patient_date = systematique.objects.filter(patient=patient, date=date_visite)

    return render(request, 'dossier/VMS/voir_vms.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})


def delete_vms(request, patient_id, visite_id):
    visite = get_object_or_404(systematique, pk=visite_id, patient_id=patient_id)
    if request.method == 'POST':
        visite.delete()
        return redirect('liste_visite_par_patient', patient_id=patient_id)
    return render(request, 'dossier/VMS/supprimer_visite.html', {'visite': visite})



##################################dossier##################################
def view_info(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    info_instance = get_object_or_404(info, patient=patient)
    return render(request, 'dossier/view_info.html', {'patient': patient, 'info': info_instance})




def view_patient_dossier(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(instance=patient)
    print("Patient PK:", patient.pk)
    return render(request, 'dossier/patient.html', {'form': form , 'patient':patient})

def liste_vms_par_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    visites = patient.systematique_set.all()  # Utilisez la relation "systematique_set" pour récupérer les visites
    url = reverse('liste_visite_par_patient', args=[patient.id])

    return render(request, 'dossier/list_vms.html', {'patient': patient, 'visites': visites})

def detail_of_vms(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(systematique, patient=patient, date=date_visite)
    visites_patient_date = systematique.objects.filter(patient=patient, date=date_visite)
    return render(request, 'dossier/vms.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})



def detail_vmr(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(VisiteReprise, patient=patient, date=date_visite)


    visites_patient_date = VisiteReprise.objects.filter(patient=patient, date=date_visite)

    return render(request, 'dossier/vmr.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})

def liste_vmr_par_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    visites = patient.visites_reprise.all()

    return render(request, 'dossier/list_vmr.html', {'patient': patient, 'visites': visites})


def liste_surv_par_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    visites = patient.surveillance_set.all()  # Utilisez la relation "systematique_set" pour récupérer les visites
    url = reverse('liste_visite_par_patient', args=[patient.id])

    return render(request, 'dossier/list_surveillance.html', {'patient': patient, 'visites': visites})

def detail_surv(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(surveillance, patient=patient, date=date_visite)

    visites_patient_date = surveillance.objects.filter(patient=patient, date=date_visite)

    return render(request, 'dossier/surv.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})

##################labo#################""""

def patients_sans_laboratoire(request):
    visites_sans_laboratoire = systematique.objects.filter(laboratoire__isnull=True)
    return render(request, 'dossier/Laboratoire/list_labo.html', {'visites_sans_laboratoire': visites_sans_laboratoire})

def ajouter_resultat_laboratoire(request, visite_id, analyse_id):
    laboratoire = Laboratoire.objects.filter(systematique_id=visite_id, analyse_id=analyse_id).first()
    if laboratoire:
        fichier_path = laboratoire.fichier.path
        response = FileResponse(open(fichier_path, 'rb'))
        return response
    return HttpResponse("Aucun fichier de laboratoire trouvé.")

def scanner_view(request, visite_id, analyse_id):
    visite = get_object_or_404(systematique, pk=visite_id)
    analyse = get_object_or_404(Analyse, pk=analyse_id)
    try:
        laboratoire = Laboratoire.objects.get(systematique=visite, analyse=analyse)
    except Laboratoire.DoesNotExist:
        laboratoire = None

    context = {
        'visite': visite,
        'analyse': analyse,
        'laboratoire': laboratoire
    }

    return render(request, 'dossier/Laboratoire/list_labo.html', context)


def upload_laboratoire(request, visite_id):
    visite = systematique.objects.get(pk=visite_id)
    analyses_with_files = []

    if request.method == 'POST':
        all_analyses_uploaded = True

        for analyse in visite.analyses.all():
            fichier_name = f'fichier_{analyse.pk}'
            if fichier_name in request.FILES:
                fichier = request.FILES[fichier_name]
                analyses_with_files.append(analyse)
            else:
                all_analyses_uploaded = False

        if all_analyses_uploaded and len(analyses_with_files) == visite.analyses.count():
            for analyse in analyses_with_files:
                fichier_name = f'fichier_{analyse.pk}'
                fichier = request.FILES[fichier_name]
                Laboratoire.objects.create(systematique=visite, analyse=analyse, fichier=fichier)
            return redirect('fiche_médicale')  # Replace with the actual URL
        else:
            error_message = "Merci de scanner tous les fichiers"
            context = {
                'visite': visite,
                'error_message': error_message,
            }
            return render(request, 'dossier/Laboratoire/ajouter_scan.html', context)


    context = {
        'visite': visite,
    }


    return render(request, 'dossier/Laboratoire/ajouter_scan.html', context)

#####################################surveillance###############################################


def add_surveillance(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = SurveillanceForm(request.POST)
        if form.is_valid():
            new_date = form.cleaned_data['date']
            if surveillance.objects.filter(patient=patient, date=new_date).exists():
                form.add_error('date', 'une visite dans la meme date existe déja.')
            else:
                new_surveillance = form.save(commit=False)
                new_surveillance.patient = patient
                new_surveillance.save()
                return redirect('liste_surveillance_par_patient', patient_id=patient_id)

    else:
        form = SurveillanceForm(initial={'patient': patient})

    return render(request,  'dossier/surveillance/add_surveillance.html', {'form': form, 'patient': patient})


def surveillance_list(request):
    patients = Patient.objects.all()
    return render(request, 'dossier/surveillance/surveillance.html', {'patients': patients})

def liste_surveillance_par_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    visites = patient.surveillance_set.all()  # Utilisez la relation "systematique_set" pour récupérer les visites
    url = reverse('liste_visite_par_patient', args=[patient.id])

    return render(request, 'dossier/surveillance/list_surveillance.html', {'patient': patient, 'visites': visites})

def detail_surveillance(request, patient_id, date_visite):
    patient = get_object_or_404(Patient, pk=patient_id)
    visite = get_object_or_404(surveillance, patient=patient, date=date_visite)

    visites_patient_date = surveillance.objects.filter(patient=patient, date=date_visite)

    return render(request, 'dossier/surveillance/voir_surv.html',
                  {'visite': visite, 'visites_patient_date': visites_patient_date})



