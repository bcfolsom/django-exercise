from django.template.response import TemplateResponse
from django import forms
from django import http
from django.core.mail import send_mail

import datetime

class NameForm (forms.Form):
	your_name = forms.CharField(label="Your Name", max_length=100)
	your_email = forms.CharField(label="Your Email", max_length=50)
	your_question = forms.CharField(label="Your Question", max_length=200)

def homepage (request):
	context = {
		'page_title': 'HOME PAGE',
		'name': 'Brad',
		'now': datetime.datetime.now(),
	}
	return TemplateResponse(request, 'homepage.html', context)


def contact_me (request):
	form = NameForm(request.POST or None)
	
	if request.method == "POST":
		if form.is_valid():
			send_mail(
			    form.cleaned_data['your_name'],
			    form.cleaned_data['your_email'] + "\n\n" + form.cleaned_data['your_question'],
			    'brad@bradfolsom.com',
			    ['bcfolsom@gmail.com'],
			    fail_silently=False,
			)
			return http.HttpResponseRedirect('/thanks')
		print(form.errors)
	context = {
		'form': form
	}
	return TemplateResponse(request, 'contact_me.html', context)


def thanks (request):
	context = {}
	return TemplateResponse(request, 'thanks.html', context)


def contact (request):
	context = {}
	return TemplateResponse(request, 'contact.html', context)


def django_layout (request):
	context = {
		'page_title': 'Django Layout',
	}
	return TemplateResponse(request, 'django_layout.html', context)


def products (request):
	context = {
		'page_title': 'HOME PAGE',
	}
	return TemplateResponse(request, 'products.html', context)


def blog (request):
	context = {
		'page_title': 'HOME PAGE',
	}
	return TemplateResponse(request, 'blog.html', context)


# def hello (request):
# 	your_name = request.POST.get('your_name', 'Default Name')
# 	context = {
# 		'your_name': your_name
# 	}
# 	return TemplateResponse(request, 'hello.html', context)



def hello (request):
	form = NameForm(request.POST or None)
	
	if request.method == "POST":
		if form.is_valid():
			print(form.cleaned_data['your_name'])
			return http.HttpResponseRedirect('thanks')
	context = {
		'form': form
	}
	return TemplateResponse(request, 'hello.html', context)



