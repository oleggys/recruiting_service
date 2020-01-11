from django.shortcuts import render, redirect

# Create your views here.
from .forms import RecruiterForm, SithForm
from .models import Clan


def index(request):
    return render(request, template_name='index.html')


def sith_auth(request):
    args = {}
    if request.method == 'POST':
        form = SithForm(request.POST)
        if form.is_valid():
            request.session['user_id'] = form.data.get('siths_select')
            return redirect('recruiters_for_sith')
        args['choice_sith_form'] = form
    if request.method == 'GET':
        args['choice_sith_form'] = SithForm()
    return render(request, template_name='sith_auth.html', context=args)


def recruiter_auth(request):
    args = {}
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            request.session['user_type'] = 'recruiter'
            clan_id = Clan.objects.get(planet=user.planet).id
            return redirect('test_for_recruiters', clan_id=clan_id)
        args['recruiter_registration_form'] = form
    if request.method == 'GET':
        args['recruiter_registration_form'] = RecruiterForm
    return render(request, template_name='recruiter_auth.html', context=args)
