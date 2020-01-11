from django import forms
from staff.models import Recruiter, Sith


class RecruiterForm(forms.ModelForm):

    class Meta:
        model = Recruiter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RecruiterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'dd/mm/yyyy'


class SithForm(forms.Form):
    siths_select = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required': True}))

    def __init__(self, *args, **kwargs):
        super(SithForm, self).__init__(*args, **kwargs)
        sith_objs = [[obj.id, obj.name] for obj in Sith.objects.all()]
        self.fields['siths_select'].choices = sith_objs
