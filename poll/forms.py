from django import forms
from poll.models import Polls


class PollsForm(forms.ModelForm):

    class Meta:
        model = Polls
        fields = ['poll_title', 'option1', 'option2', 'option3', 'option4', 'option5']
        widgets={
            'poll_title': forms.TextInput(attrs={'class':'inputs'}),
            'option1': forms.TextInput(attrs={'class':'inputs'}),
            'option2': forms.TextInput(attrs={'class':'inputs'}),
            'option3': forms.TextInput(attrs={'class':'inputs'}),
            'option4': forms.TextInput(attrs={'class':'inputs'}),
            'option5': forms.TextInput(attrs={'class':'inputs'})

        }