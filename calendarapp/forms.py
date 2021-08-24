from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['titulo', 'descricao', 'inicio', 'final']
        # datetime-local is a HTML5 input type
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event description'
            }),
            'inicio': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'final': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
        }
        # exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['inicio'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['final'].input_formats = ('%Y-%m-%dT%H:%M',)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['user']
