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



# def DemoView(request):
#     if request.method == "POST":
#         formset = DemoFormSet(request.POST)
#
#     else:
#         formset = DemoFormSet()
#     return render(request, 'demo.html', {'formset': formset})
#
# def PractView(request):
#     extra_forms = 2
#     PractFormSet = formset_factory(PractForm, extra=extra_forms)
#     PractSet = BaseDemoForm()
#     symptoms = []
#
#     if request.method == 'POST':
#
#         if 'additems' in request.POST and request.POST['additems'] == 'true':
#             formset_dictionary_copy = request.POST.copy()
#             formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
#             formset = PractFormSet(formset_dictionary_copy)
#             symptoms = PractSet.cleaned_data
#         else:
#             formset = PractFormSet(request.POST)
#             symptoms = PractSet.cleaned_data


        # symptoms = [form.cleaned_data for form in self.formset]
        # [form.cleaned_data for form in self.forms]
        # for form in formset:
        #     symptoms.append(form.cleaned_data)
        # symptoms = PractForm.cleaned_data
    # else:
    #     formset = PractFormSet()
    #     symptoms = PractSet.cleaned_data
    #
    # return render(request,'pract.html',{'formset':formset,'symptoms':symptoms})


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

    return render(request, 'trial.html', context)





# def PredictionView(request):
#     template_name = 'form.html'
#     message = ''
#     input_vector = np.zeros(len(symptoms_dict))
#
#     if request.method == 'POST':
#         form = PredForm(request.POST)
#
#         if form.is_valid():
#             sympton_1 = form.cleaned_data['symptom1']
#             sympton_2 = form.cleaned_data['symptom2']
#             sympton_3 = form.cleaned_data['symptom3']
#             sympton_4 = form.cleaned_data['symptom4']
#
#             psymptoms = [sympton_1, sympton_2, sympton_3, sympton_4]
#
#
#             input_vector[[symptoms_dict[sympton_1], symptoms_dict[sympton_2], symptoms_dict[sympton_3], symptoms_dict[sympton_4]]] = 1
#
#
#             message = rf_clf.predict([input_vector])[0]
#
#             context = {'form':form,
#                         'message':message}
#
#     else :
#         form = PredForm()
#         context = {
#             'form':form,
#             'message':message }
#
#     return render(request, template_name, context)
