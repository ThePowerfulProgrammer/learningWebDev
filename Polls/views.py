from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
from django.views import generic
# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("Polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context,request))

class IndexView(generic.ListView):
    template_name = "Polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        # Return the last 5 published questions (excluding those set to be published in the future)
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
    

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "Polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "Polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"Polls/results.html", {"question":question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "Polls/results.html"
    
    
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"Polls/detail.html", 
                      {
                          "question":question,
                          "error_message":"You did not select a choice",
                      }
                      
                      )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("Polls:results",args=(question.id,)))
