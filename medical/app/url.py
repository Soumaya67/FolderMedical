from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view, admin, dashboard, patient_list, home, update_patient, create_patient, \
    delete_patient, view_patient

urlpatterns = [
         path('patients/', patient_list, name='patients'),
         path('dashboard/', dashboard, name='dashboard'),
         path('home/', home, name='home'),
         path('', views.login_view, name='login_view'),
         path('admin/', views.admin, name='admin'),
         path('medecin/', views.medecin, name='medecin'),
         path('infermier/', views.infermier, name='infermier'),
         path('create/', create_patient, name='create_patient'),
         path('update/<int:pk>/', update_patient, name='update_patient'),
         path('delete/<int:pk>/', delete_patient, name='delete_patient'),
         path('view/<int:pk>/', view_patient, name='view_patient'),
         path('logout/', auth_views.LogoutView.as_view(), name='logout'),
         path('inde/', views.inde, name='index'),
         path('new_note', views.new_note, name='new'),
         path('note/<str:pk>', views.note_detail, name='note'),
         path('delete_note/<str:pk>', views.delete_note, name='delete'),
         path('search_result/', views.search, name='search'),
         path('dossier/', views.dossier, name='dossier'),
         path('ajouterdossier/', views.patients_without_info_view, name='ajouterdossier'),
         path('add_dossier/', views.patients_with_info_view, name='add_dossier'),
         path('add_info/<int:patient_id>/', views.add_info, name='add_info'),
         path('menu1/', views.menu1_view, name='menu1'),
         path('menu3/', views.menu3_view, name='menu3'),
       #################VMR######################################"
         path('Vmr/', views.reprise_list, name='Vmr'),
         path('ajouter_visite_reprise/<int:patient_id>/', views.visite_reprise, name='ajouter_visite_reprise'),
         path('list_visite_reprise/<int:patient_id>', views.liste_visites_par_patient, name='list_reprise'),
         path('detail_visite_reprise/<int:patient_id>/<str:date_visite>/', views.detail_visite_reprise, name='detail_visite_reprise'),

    ###################VMS###########################################
         path('Vms', views.sys_list, name='Vms'),
         path('liste_visite_par_patient/<int:patient_id>', views.liste_visite_par_patient, name='liste_visite_par_patient'),
         path('ajouter_vms/<int:patient_id>', views.ajouter_vms, name='ajouter_vms'),
         path('liste_analyses/', views.liste_analyses, name='liste_analyses'),
         path('detail_vms/<int:patient_id>/<str:date_visite>/', views.detail_vms, name='detail_vms'),
         path('delete_vms/<int:pk>/<str:date_visite>/', views.delete_vms, name='delete_vms'),
    ####################surveillance######################################
         path('fiche_médicale', views.surveillance_list, name='fiche_médicale'),
         path('add_surveillance/<int:patient_id>/',views.add_surveillance, name='ajouter_surveillance'),
         path('detail_surveillance/<int:patient_id>/<str:date_visite>/', views.detail_surveillance, name='detail_surveillance'),
         path('liste_surveillance_par_patient/<int:patient_id>/', views.liste_surveillance_par_patient, name='liste_surveillance_par_patient'),
         path('patients_sans_laboratoire', views.patients_sans_laboratoire, name='liste_labo'),
         path('scanner_view/<int:visite_id>/<int:analyse_id>/', views.scanner_view, name='scanner_view'),
         path('upload_laboratoire/<int:visite_id>/', views.upload_laboratoire, name='upload_laboratoire'),

    #######################dossier########################################
         path('view_patient_dossier/<int:pk>/', views.view_patient_dossier, name='view_patient_dossier'),
         path('liste_vms_par_patient/<int:pk>/', views.liste_vms_par_patient, name='liste_vms_par_patient'),
         path('detail_of_vms/<int:patient_id>/<str:date_visite>/', views.detail_of_vms, name='detail_of_vms'),
         path('detail_vmr/<int:patient_id>/<str:date_visite>/', views.detail_vmr, name='detail_vmr'),
         path('liste_vmr_par_patient/<int:pk>/', views.liste_vmr_par_patient, name='liste_vmr_par_patient'),
         path('liste_surv_par_patient/<int:pk>/', views.liste_surv_par_patient, name='liste_surv_par_patient'),
         path('detail_sur/<int:patient_id>/<str:date_visite>/', views.detail_surv, name='detail_surv'),
         path('view_info/<int:pk>/', views.view_info, name='view_info'),




    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


