from django.shortcuts import render, redirect

# Create your views here.
from staff.forms import RecruiterForm


def index(request):
    return render(request, template_name='index.html')


def sith_auth(request):
    return render(request, template_name='sith_auth.html')


def recruiter_auth(request):
    args = {}
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            request.session['user_type'] = 'recruiter'
            return redirect('index')
        args['recruiter_registration_form'] = form
    if request.method == 'GET':
        args['recruiter_registration_form'] = RecruiterForm
    return render(request, template_name='recruiter_auth.html', context=args)
