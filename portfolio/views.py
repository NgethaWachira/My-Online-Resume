from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request=request, template_name='portfolio/home.html')

def about(request):
	return render(request, 'portfolio/about.html')

def resume(request):
	return render(request, 'portfolio/resume.html')

def apps(request):
	return render(request, 'portfolio/apps.html')

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('name')
			messages.success(request, f'Your message has been sent successfully, {name}')
			return redirect("portfolio:portfolio-home")

				#send an email
		send_mail(
			name, # subject
			message, # message
			email, # sender
			['jngethawachira@gmail.com'], # recipient(s)
			fail_silently = False
			)

	else:
		form = ContactForm()
	return render(request, 'portfolio/contact.html', context={'form': form})