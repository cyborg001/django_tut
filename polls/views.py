from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
            # 'latest_question_list':latest_question_list,
    #     }
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context,request))
    # output = ', '.join([q.question_text for q in latest_question_list]) 
    # return HttpResponse(output)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name =  'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
#     try:
#         question = Question.objects.get(pk=question_id)
#         print(question)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
    # question = get_object_or_404(Question,pk=question_id)
    # return render(request, 'polls/detail.html', {"question":question})
    # return HttpResponse("You're looking at question %s." % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    # question = get_object_or_404(Question, pk = question_id)
    # try:
    #     choices = question.choice_set.all()
    #     for n in choices:
    #         print(n.choice_text, f'votes = {n.votes}')
    #     print(choices)
    # except (KeyError,Choice.DoesNotExist):
    #     return render(request, 'polls:detail.html',{
    #         'question':question,
    #         'error_message': 'you didnt select a choice'
    #     })
    # else:
    #     return render(request, 'polls/results.html', {"question":question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    print(Choice)
    question = get_object_or_404(Question,pk= question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print('error')
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': 'you didnt select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        
    return HttpResponse("You're voting on question %s." % question_id)