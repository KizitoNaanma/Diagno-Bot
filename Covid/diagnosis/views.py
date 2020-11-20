from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .forms import *
import numpy as np
from django.forms.formsets import formset_factory

import pickle
# Create your views here.
app_name = 'diagnosis'

with open('/home/kizito/Documents/Diagno/Covid/diagnosis/mod.pkl', 'rb') as f:
    df = pickle.load(f)
    rf_clf = pickle.load(f)
    symptoms_dict = pickle.load(f)

# class LandingView(TemplateView):
#     template_name = 'index.html'
def LandingView(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def PredictionView(request):
    TrialFormSet = formset_factory(TrialForm, formset=BaseTrialFormSet,extra=8)
    new_symptoms = []
    extra_forms=1
    message = ''
    input_vector = np.zeros(len(symptoms_dict))

    if request.method == 'POST':
        trial_formset = TrialFormSet(request.POST)

        if trial_formset.is_valid():
            new_symptoms = []

            for trial in trial_formset:
                symptom = trial.cleaned_data.get('symptom')
                if symptom:
                    new_symptoms.append(symptom)

            if 'additems' in request.POST and request.POST['additems'] == 'true':
                formset_dictionary_copy = request.POST.copy()
                formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
                trial_formset = TrialFormSet(formset_dictionary_copy)
            else:
                trial_formset = TrialFormSet()


            for i in new_symptoms:
                input_vector[symptoms_dict[i]] = 1


            message = rf_clf.predict([input_vector])[0]

    else:
        trial_formset = TrialFormSet()

    context = {'trial_formset':trial_formset,
                'message':message}

    return render(request, 'prediction.html', context)
