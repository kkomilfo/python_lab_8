from django.shortcuts import render
from app.models import Patient, Doctor, HospitalStay

# Create your views here.
def project_page(request):
    # Fetch all data from the models
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    hospital_stays = HospitalStay.objects.all()

    # Pass the data to the template
    return render(request, 'app/project_page.html', {
        'patients': patients,
        'doctors': doctors,
        'hospital_stays': hospital_stays,
    })