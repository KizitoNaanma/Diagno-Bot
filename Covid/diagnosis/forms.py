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

class DemoForm(forms.Form):
    demoSymp = forms.ChoiceField(choices=dict_zip['zipped1'])

DemoFormSet = formset_factory(DemoForm, extra=0)

class PractForm(forms.Form):
    practSymp = forms.CharField()

class BasePractForm(BaseFormSet):
    def cleaned_data(self):
        """
        Return a list of form.cleaned_data dicts for every form in self.forms.
        """
        if not self.is_valid():
            raise AttributeError("'%s' object has no attribute 'cleaned_data'" % self.__class__.__name__)

        return [form.cleaned_data for form in self.forms]


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
