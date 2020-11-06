from django import forms
import pickle

with open('mod.pkl', 'rb') as f:
    df = pickle.load(f)

symps = list(df.columns)

class PredForm(form.Form):
    symptom = forms.ChoiceField(choices=symps)
