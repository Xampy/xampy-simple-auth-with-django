from django import forms 
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'nom',
            'prenom',
            'email',

            'password',
        ]

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder': 'nom de fammile...'
            }
        )
        self.fields['prenom'].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder' : ''
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )

        self.fields['password'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )