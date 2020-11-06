from django.shortcuts import render
from django.views.generic import TemplateView
import pickle
# Create your views here.

with open('mod.pkl', 'rb') as f:
    df = pickle.load(f)
    rf_clf = pickle.load(f)
    symptoms_dict = pickle.load(f)

# class LandingView(TemplateView):
#     template_name = 'index.html'
def LandingView(request):
    template_name = 'index.html'
    return render(request, template_name)

# def pred(request)
