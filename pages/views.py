from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})
    #return HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": 123, 
        "my_list": [123, 4242, 12313, "Abc"]
    }
    return render(request, "contact.html", my_context)

def catalogue_view(request, *args, **kwargs):
    return render(request, "catalogue.html", {})