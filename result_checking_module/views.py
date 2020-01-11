from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RecruiterAnswerForm
from staff.models import Clan, Recruiter, Sith, DarkHand
from .models import Question, Test, RecruiterAnswer


def get_questions_dict():
    pass


def test_for_recruiters(request, clan_id):
    args = {}
    clan = Clan.objects.get(id=clan_id)
    user_id = request.session['user_id']
    recruiter = Recruiter.objects.get(id=user_id)
    test_obj = Test.objects.get(clan=clan)
    questions = Question.objects.filter(test=test_obj)
    form_questions = []
    args['test_title'] = test_obj.name
    answers_count = len(questions)
    if request.method == 'POST':
        answers_count = 0
        answers = []
        for i in range(len(questions)):
            answer = request.POST.get(str(i)+'-answer')
            if answer:
                answers_count += 1
                answers.append(answer == 'True')
        if answers_count == len(questions):
            for i in range(len(questions)):
                RecruiterAnswer(recruiter=recruiter, question=questions[i], answer=answers[i]).save()
            return redirect('thanks')
    if request.method == 'GET' or answers_count != len(questions):
        # user_type = request.session['user_type']
        for i in range(len(questions)):
            answer_form = RecruiterAnswerForm(
                auto_id='%s_' + str(i),
                prefix=str(i)
            )
            form_questions.append({
                'title': 'Question #' + str(i),
                'text': questions[i].text,
                'answer_form': answer_form
            })

    args['questions'] = form_questions
    return render(request, template_name='test_for_recruiter.html', context=args)


def thanks_view(request):
    return render(request, 'thanks.html')


def recruiters_for_sith(request):
    args = {}
    sith_id = request.session['user_id']
    sith = Sith.objects.get(id=sith_id)
    dark_hand_users = DarkHand.objects.values_list('recruiter__id', flat=True)
    recruiters_which_have_answer = []
    recruiters = Recruiter.objects.filter(planet__clan=sith.clan).exclude(id__in=dark_hand_users)
    for recruiter in recruiters:
        if RecruiterAnswer.objects.filter(recruiter=recruiter).exists():
            recruiters_which_have_answer.append(recruiter)
    args['recruiters'] = recruiters_which_have_answer
    return render(request, template_name='recruiters_for_sith.html', context=args)


def check_user_answers(request, recruiter_id):
    args = {}
    if request.method == 'POST':
        try:
            sith = Sith.objects.get(id=request.session['user_id'])
            rec = Recruiter.objects.get(id=recruiter_id)
            DarkHand(sith=sith, recruiter=rec).save()
            rec.send_notification('')
            return redirect('recruiters_for_sith')
        except IntegrityError:
            return redirect('recruiters_for_sith')
    answers = RecruiterAnswer.objects.filter(recruiter__id=recruiter_id)
    args['answers'] = answers
    return render(request, template_name='recruiter_answers.html', context=args)