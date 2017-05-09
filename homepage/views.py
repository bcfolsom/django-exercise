from django.template.response import TemplateResponse

import datetime

def homepage (request):
	context = {
		'page_title': 'HOME PAGE',
		'name': 'Brad',
		'now': datetime.datetime.now(),
	}
	return TemplateResponse(request, 'homepage.html', context)


def contact (request):
	context = {
		'page_title': 'HOME PAGE',
	}
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