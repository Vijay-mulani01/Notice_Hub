from django.shortcuts import render
from Admin.models import Notice

def all_notices(request):
    notice=Notice.objects.all()
    context={'result':notice}
    return render(request, 'user/notice.html',context)
