from django.http.response import HttpResponse
from django.shortcuts import render
from models import Member
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


@require_http_methods(["GET"])
def list(request):
    members = Member.objects.all()

    return render(request,'member/list.html',{"members":members})

@require_http_methods(["GET"])
def detail(request, username):
    try:
        member = Member.objects.get(sparcsid=username)
    except ObjectDoesNotExist:
        return HttpResponse(content="Member not found", status=404)
    data = model_to_dict(member)
    return render(request,'member/detail.html',{"member":data})