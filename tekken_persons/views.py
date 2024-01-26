from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


# не полная инфа
def persons_list(request):
    if request.method == 'GET':
        persons = models.PersonGame.objects.all()
        return render(request, template_name='tekken_game/persons_list.html',
                      context={'persons': persons})


# подробная инфа
def persons_detail(request, id):
    if request.method == 'GET':
        person_id = get_object_or_404(models.PersonGame, id=id)
        return render(request, template_name='tekken_game/person_detail.html',
                      context={'person_id': person_id}
                      )


# Добавить персонажа
def create_person_view(request):
    if request.method == 'POST':
        form = forms.TekkenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен <a href="/">На главную</a> ')
    else:
        form = forms.TekkenForm()
    return render(request,
                  template_name='tekken_game/crud/create_person.html',
                  context={'form': form}
                  )


def create_person_review_view(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Отзыв добавлен <a href="/">На главную</a>')
    else:
        form = forms.ReviewForm()
        return render(request, template_name='tekken_game/crud/create_person_review.html', context={'form':form})


# Удаление
def delete_person_view(request, id):
        person_id = get_object_or_404(models.PersonGame, id=id)
        person_id.delete()
        return HttpResponse('Успешно удален <a href="/">На главную</a> ')


#Изменить
def edit_person_view(request, id):
    person_id = get_object_or_404(models.PersonGame, id=id)
    if request.method == 'POST':
        form = forms.TekkenForm(instance=person_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/">На главную</a> ')
    else:
        form = forms.TekkenForm(instance=person_id)
        return render(request,
           template_name='tekken_game/crud/edit_person.html',
           context={'form': form,
                    'person_id': person_id})