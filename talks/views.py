from django.shortcuts import render


def talk_list(request):
    return render(request, 'talks/talk_list.html')
