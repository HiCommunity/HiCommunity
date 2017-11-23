from django.shortcuts import render
from users.utils.security import login_required


@login_required('admin')
def index(request, **kwargs):
    return render(request, 'hiadmin/index.html')
