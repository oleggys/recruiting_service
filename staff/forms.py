from django import forms
from staff.models import Recruiter


class RecruiterForm(forms.ModelForm):

    class Meta:
        model = Recruiter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RecruiterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'dd/mm/yyyy'
