from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Building, SingleResponse
from .forms import ResponseForm, FoodForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    form = ResponseForm() 

    def get_queryset(self):
        """Return the last five published questions."""
        return Building.objects.order_by('-name')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # get the default context data
        context['form'] = self.form
        return context

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
            return HttpResponseRedirect('/')
    else:
        form = ResponseForm()
    return render(request, 'polls/form.html', {'form': form})

def post_new_food(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save()
            bname = form.cleaned_data['building']
            bname.food()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')
    else:
        form = FoodForm()
    return render(request, 'polls/form.html', {'form': form})

def _plot_building(request,building_name):
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    import matplotlib.pylab as plt
    building_name = building_name.replace('_',' ')
    srlist = SingleResponse.objects.filter(building__name=building_name)
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    for i in range(0,len(srlist)):
        x.append(srlist[i].temp)
    colors = ['#10788e','#5fc8e8','#94bc46','#ef8e27','#ec5a29','#ec5a29']
    n,bins,patches = ax.hist(x,bins=[-2,-1,0,1,2,3])#,color=colors)
    ax.set_xticks([-1.5,-.5,0.5,1.5,2.5])
    ax.set_xticklabels(['Cold','Cool','Just Right','Warm', 'Hot'])
    ax.set_ylabel('Count',fontsize=15)
    ax.set_title(building_name+": votes", fontsize=20)
    for p in range(0,5):
        plt.setp(patches[p],'facecolor',colors[p])

    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def plot_building(request,building_name):
    building_name = building_name.replace('_',' ')
    srlist = SingleResponse.objects.filter(building__name=building_name).order_by('-timestamp')
    rooms = srlist.values('room').distinct()
    num = len(srlist)
    cold,cool,jr,warm,hot=0,0,0,0,0
    for i in range(0,len(srlist)):
        t= srlist[i].temp
        if t== -2:
            cold += 1
        elif t== -1:
            cool += 1
        elif t== 0:
            jr +=1
        elif t== 1:
            warm += 1
        else:
            hot +=1
    temps = [cold,cool,jr,warm,hot]
    return render(request, 'polls/building.html',{'building':building_name,'srlist':srlist,'temps':temps,'num':num,'rooms':rooms})
