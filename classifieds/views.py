from django.shortcuts import render, get_object_or_404
from .models import ExecutiveProfile

def exec_list(request):
    execs = ExecutiveProfile.objects.order_by("-created_at")
    return render(request, "classifieds/exec_list.html", {"execs": execs})

def exec_detail(request, pk):
    obj = get_object_or_404(ExecutiveProfile, pk=pk)
    return render(request, "classifieds/exec_detail.html", {"exec": obj})
