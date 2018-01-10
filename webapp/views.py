from django.views import generic
from django.views.generic import View
from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm

import json


class HomePage(generic.TemplateView):
    template_name = "webapp/home.html"


class ListOfUsers(generic.ListView):
    template_name = "webapp/listings.html"
    context_object_name = "all_users"

    def get_queryset(self):
        return User.objects.all()


class UserFormView(View):
    form_class = CreateUserForm
    template_name = "webapp/add.html"

    # Displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Handles Form submission
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            user.save()

            response_data = {'status': 1, 'message': 'User Successfully added'}

        else:
            response_data = {'status': 0, 'message': form.errors}

        return HttpResponse(json.dumps(response_data), content_type="application/json")




