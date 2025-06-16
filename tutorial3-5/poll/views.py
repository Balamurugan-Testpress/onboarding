from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from poll.models import Choice, Question
from django.utils import timezone
from django.db.models import F
# Create your views here.
from django.views import generic
from django.utils import timezone

def index(request):
    content = {"a":[1,2,34]}
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list,"a" : content["a"]}
    return render(request,"poll/index.html",context)

# admin@gmail.com   123  admin


def detail(request, question_id):
    question = get_object_or_404(
        Question,
        pk=question_id,
        pub_date__lte=timezone.now()
    )
    return render(request, "poll/detail.html", context={"question": question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    max_votes = 0
    top_choice = None

    for choice in question.choice_set.all():
        if choice.votes > max_votes:
            max_votes = choice.votes
            top_choice = choice

    return render(request, 'poll/result.html', {
        "question": question,
        "top_choice": top_choice,
        "max_votes": max_votes
    })


def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "poll/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        selected_choice.refresh_from_db() 
        print(selected_choice.votes)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))
    


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
    



class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]