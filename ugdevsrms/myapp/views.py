from django.shortcuts import render
# Create your views here.
def my_view(request):
    return render(request, 'mytemplate.html')
def signIn_view(request):
    return render(request, 'signIn.html')
def signUp_view(request):
    return render(request, 'signUp.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')
def profile_view(request):
    return render(request, 'profile.html')
def editprofile_view(request):
    return render(request, 'editprofile.html')
def changepassword_view(request):
    return render(request, 'changepassword.html')
