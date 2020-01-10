from django import forms
from django.forms import modelformset_factory

from result_checking_module.models import Question, Test, RecruiterAnswer

ANSWERS = [
    ('0', False),
    ('1', True)
]


class RecruiterAnswerForm(forms.Form):
    answer = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

    class Meta:
        fields = ('answer',)
