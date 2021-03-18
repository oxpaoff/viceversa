from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    get_text = request.GET['usertext']
    amount = 0
    for i in get_text.split(' '):
        amount += 1
    text = 'Original text has {0} words'.format(amount)
    reversed_text = get_text[::-1]

    return render(request, 'reverse.html', {'reverse': reversed_text, 'use': get_text, 'number':
        text})
