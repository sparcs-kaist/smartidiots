from django.shortcuts import render
from models import Member
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def listView(request):
    members = Member.objects.all()

    return render(request,'member/list.html',{"members":members})