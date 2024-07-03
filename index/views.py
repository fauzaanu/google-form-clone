from django.shortcuts import render

from forms.models import Form


def index(request):
    forms = Form.objects.filter(creator=request.user)
    return render(request, "forms/index.html", {
        "forms": forms
    })
