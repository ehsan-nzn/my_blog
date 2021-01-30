from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            # return HttpResponse("shod")
            return redirect("articles:articles_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", context={"form": form})
