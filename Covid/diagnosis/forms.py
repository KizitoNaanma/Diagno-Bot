from django import forms
import pickle
from django.forms import BaseFormSet
from django.forms.formsets import formset_factory


with open('/home/kizito/Documents/Diagno/Covid/diagnosis/mod.pkl', 'rb') as f:
    df = pickle.load(f)
    rf_clf = pickle.load(f)
    symptoms_dict = pickle.load(f)

l1 = list(symptoms_dict.keys())

dict_zip = {
       'zipped1' : zip(l1,l1),
       'zipped2' : zip(l1, l1),
       'zipped3' : zip(l1, l1),
       'zipped4' : zip(l1, l1)
}






class TrialForm(forms.Form):
    symptom = forms.ChoiceField(choices=dict_zip['zipped1'],widget=forms.Select(attrs={'id':'firstname'}))

class BaseTrialFormSet(BaseFormSet):
    def clean(self):
        symptoms = []
        duplicates = False

        for form in self.forms:

            if form.cleaned_data:
                symptom = form.cleaned_data['symptom']

                if symptom:
                    if symptom in symptoms:
                        duplicates = True
                        symptoms.append(symptom)
                if duplicates:
                    raise forms.ValidationError(
                    'Symptom fields musst be unique',
                    code = 'duplicate_symptoms'
                    )

        return symptoms











class PredForm(forms.Form):
    symptom1 = forms.ChoiceField(choices=dict_zip['zipped1'])
    symptom2 = forms.ChoiceField(choices=dict_zip['zipped2'])
    symptom3 = forms.ChoiceField(choices=dict_zip['zipped3'])
    symptom4 = forms.ChoiceField(choices=dict_zip['zipped4'])
