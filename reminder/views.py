from django.shortcuts import render

from .forms import ReminderForm


def reminder(request):

    if "submit" in request.GET:
        reminder_form = ReminderForm(request.GET)
        if reminder_form.is_valid():
            email = reminder_form.cleaned_data["email"]
            text_reminder = reminder_form.cleaned_data["text_reminder"]
            data_reminder = reminder_form.cleaned_data["data_reminder"]
    else:
        reminder_form = ReminderForm()
    return render(
        request,
        "reminder/reminder.html",
        {"reminder_form": reminder_form, }
    )
