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






# class PractForm(forms.Form):
#     symptom = forms.CharField()



class TrialForm(forms.Form):
    symptom = forms.CharField()

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





# filename = 'finalized_model.sav'
# pickle.dump(model, open(filename, 'wb'))
#
# # some time later...
#
# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)
