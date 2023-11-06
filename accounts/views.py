from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def communityMember(request):
    return render(request, 'communityM.html')

def communityMemberRegister(request):
    return render(request, 'communityRegister.html')