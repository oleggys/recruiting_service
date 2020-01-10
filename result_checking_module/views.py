from django.shortcuts import render, redirect

# Create your views here.
from .forms import RecruiterAnswerForm
from staff.models import Clan, Recruiter
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
        print(request.POST)
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
    return render(request, 'test_for_recruiter.html', context=args)


def thanks_view(request):
    return render(request, 'thanks.html')