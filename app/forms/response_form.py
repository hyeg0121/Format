import json

from django import forms


class SurveyResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey')
        super().__init__(*args, **kwargs)

        for question in survey.questions.all():
            if question.question_type == 'SINGLE_CHOICE':
                options = json.loads(question.options)
                self.fields[str(question.id)] = forms.ChoiceField(
                    choices=[(option, option) for option in options],
                    widget=forms.RadioSelect,
                    label=question.title
                )
            elif question.question_type == 'SUBJECTIVE':
                self.fields[str(question.id)] = forms.CharField(
                    widget=forms.Textarea,
                    required=True,
                    label=question.title
                )
