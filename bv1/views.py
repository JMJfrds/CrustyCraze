from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.urls import reverse_lazy
from bv1.forms import ContactForm, SignUpForm
from bv1.models import ContactModel


class HomeView(TemplateView):
    template_name = 'bv1/index.html'


class AboutView(TemplateView):
    template_name = 'bv1/about.html'


class ServiceView(TemplateView):
    template_name = 'bv1/service.html'


class ProductView(TemplateView):
    template_name = 'bv1/product.html'


class TeamView(TemplateView):
    template_name = 'bv1/team.html'


from django.views.generic import TemplateView
from .models import ContactModel
from .forms import SignUpForm

class TestimonialView(TemplateView):
    template_name = 'bv1/testimonial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactModel.objects.exclude(message__isnull=True).exclude(message__exact='').order_by('-id')[:5]
        context['form'] = SignUpForm()  # form ni ham shu yerda contextga qo‘shamiz
        return context

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact_url")
        else:
            # Agar xato bo‘lsa, contacts + form qaytadan render qilinadi
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)



class SuccessView(TemplateView):
    template_name = 'bv1/success.html'


class ContactView(View):
    template_name = 'bv1/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            print(f"Form is valid: {contact}")
            return redirect("success")
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, self.template_name, {'form': form})
