from django.shortcuts import render
from users.utils.security import login_required, role_restrict


@login_required
@role_restrict('admin')
def index(request, **kwargs):
    return render(request, 'hiadmin/index.html')
