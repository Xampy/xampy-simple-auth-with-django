from django.shortcuts import render, redirect

from .forms import MemberForm
from .models import Member

# Create your views here.
def login(request):
	#Get the form data

	errors = "dfdfdf"
	user = None

	if request.method == 'POST':
		data = request.POST
		
		print(data)

		lastname = data['lastname']
		firstname = data['firstname']
		password = data['password']

		#Find a record with the given credential
		try:
			user = Member.objects.get(
						nom=lastname, 
						prenom=firstname, 
						password=password
			)

			return redirect(pending)
		except Exception as e:
			errors  = "Pas de membres avec ces paramètres"
		

		

		
	context = {
		'errors': errors,
	}

	return render(request, 'net_amis/auth/login.html.twig', context);


def register(request):


	form = MemberForm(request.POST or None)
	if form.is_valid():
		print(form)
		form.save()

		return redirect(pending)

		print('\n User saved with success')
	else:
		print("\nRegister form not valid to be saved")

	context = {
		'form': form
	}

	return render(request, 'net_amis/auth/register.html.twig', context);

def pending(request):

	context = {
		
	}

	return render(request, 'net_amis/auth/pending.html.twig', context);