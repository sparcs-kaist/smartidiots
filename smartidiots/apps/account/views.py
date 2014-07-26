from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import LoginForm

def login(request):
    next = request.GET.get('next','')
    error_message = ''
    login_form = LoginForm().as_p()
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                #return HttpResponseRedirect('/')
                return render_to_response('tmp.html', {'id': user.username}, context_instance=RequestContext(request))
            else:
                error_message = 'This user is not activated.'
        else:
            error_message = 'Username or password does not match.'

    return render_to_response('login.html', {
            'section': 'login',
            'title': u'SPARCS Member Login',
            'next': next,
            'login_form': login_form,
            'error_message': error_message,
        }, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
