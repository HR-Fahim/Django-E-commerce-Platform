from django.shortcuts import redirect, render

from .forms import CreateUserForm

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    context = {'form': CreateUserForm()}

    return render(request, 'account/registration/register.html', context=context)