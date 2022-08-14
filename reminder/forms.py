from django import forms
from datetime import  datetime


class ReminderForm(forms.Form):

    email = forms.EmailField(max_length=100, required=True)
    text_reminder = forms.CharField(max_length=254, required=True)
    data_reminder = forms.DateTimeField(label='Data',
                                        initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        required=False
                                        )
