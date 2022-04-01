from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from dentist_2_project.core.forms import AppointmentForm, DeleteAppointmentForm
from dentist_2_project.core.models import Appointment


def build_book_appointment(request):
    user = request.user
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            venue = form.cleaned_data['venue']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']

            form = form.save(commit=False)
            form.user = request.user
            name = form.user.profile.first_name
            phone = form.user.profile.phone
            email = form.user.email
            send_mail(f'Appointment from {name} at {date}{time} at {venue} with phone number: {phone} and email: {email}',
                      message, f'{email}', ['evgenikostadinov1987@gmail.com'],)

            form.save()
#            messages.success(request, 'appointment added')
            return redirect('show profile view')
    else:
        form = AppointmentForm(instance=user)

    context = {
        'form': form
    }

    return render(request, 'core/appointment.html', context)



def build_delete_appointment(request, pk):
    appoint = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAppointmentForm(request.POST, instance=appoint)
        if form.is_valid():
            form.save()
            return redirect('show index')
            messages.success(request, 'You Successfully DELETED your PASSED appointment!')
    else:
        form = DeleteAppointmentForm(instance=appoint)

    context = {
        'form': form,
        'appoint': appoint,
    }

    return render(request, 'core/appointment_delete.html', context)