from django import forms
from .models import Appointment, Service, Master

class AppointmentForm(forms.ModelForm):
    appointment_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Дата та час запису"
    )

    class Meta:
        model = Appointment
        fields = ['service', 'master', 'client_name', 'client_phone', 'appointment_datetime']
