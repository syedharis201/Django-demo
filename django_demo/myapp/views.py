from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def user_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return render(request, 'myapp/result.html', {'name': name, 'age': age})
    return render(request, 'myapp/form.html')
