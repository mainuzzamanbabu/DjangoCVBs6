from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView
from classroom.forms import ContactForm
from classroom.models import Teacher
# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # .save()
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    #successfull url, not a template.html
    # success_url = "/classroom/thank_you/"
    success_url = reverse_lazy("classroom:thank_you")

    #What to do with the form?
    def form_valid(self,form):
        # form.save()
        print(form.cleaned_data)
        return super().form_valid(form)