from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Building, Choice, Question, SingleResponse
from .forms import ResponseForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    form = ResponseForm() 

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # get the default context data
        context['form'] = self.form
        return context

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class FormView(generic.DetailView):
    model = SingleResponse
    template_name = 'polls/form.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def thanks(request):
    return HttpResponse("Thanks!")

def post_new(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ResponseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save()
            bname = form.cleaned_data['building']
            bname.avg_temp()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')
    else:
        form = ResponseForm()
    return render(request, 'polls/form.html', {'form': form})

def plot_building(request,building_name):
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    srlist = SingleResponse.objects.filter(building__name=building_name)
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    for i in range(0,len(srlist)):
        x.append(srlist[i].temp)
    ax.hist(x)
    #fig.ylabel('Count')
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
