from django.shortcuts import get_object_or_404, render, render_to_response

# Create your views here.

from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from broadcast.models import Areas, Employees, TimeList, ApplyInfos
from polls.models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	output = ', '.join([p.question_text for p in latest_question_list])
#	return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
		'lastest_question_list': latest_question_list,
	})
    return HttpResponse(template.render(context))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
#    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
#    response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
#    return HttpResponse(response % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
#    return HttpResponse("You're voting on question %s." % question_id)

def login(request):
    return render(request, 'broadcast/login.html')

def check(request):
    if request.method == 'POST':
#        uf = UserForm(request.POST)
#        if uf.is_valid():
        #Get User ID and PWD from <form>
        userid = request.POST['userid'].strip()
        password = request.POST['password'].strip()
        #Check the data from <form> with Database
        check_login = Employees.objects.filter(employee_id = userid, employee_pwd = password)
        if check_login:
            emp = Employees.objects.get(employee_id = userid)
            apin = ApplyInfos.objects.filter(employee_id = userid)
            return render_to_response('broadcast/success.html', {'user': emp, 'apins': apin})
        else:
            return HttpResponseRedirect(reverse('broadcast:login'))

#    return render_to_response('broadcast/success.html',{'username':username})
#    else:
#        uf = UserForm()
#    return render_to_response('broadcast/login.html')
#    return HttpResponseRedirect(reverse('broadcast:success', args=(p.id,)))
#    return render(request, 'broadcast/success.html',{'username':userid})
    return render(request, 'broadcast/success.html', {'userid':userid})

def new_apply_html(request):
    return render(request, 'broadcast/login.html')

def new_apply(request):
    
    from blog.models import Blog
    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()
