from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic


class PersonsListView(generic.ListView):
    model = models.PersonGame
    template_name = 'tekken_game/persons_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return self.model.objects.all()


# def persons_list(request):
#     if request.method == 'GET':
#         persons = models.PersonGame.objects.all()
#         return render(request, template_name='tekken_game/persons_list.html',
#                       context={'persons': persons})


# подробная инфа
class PersonDetailView(generic.DetailView):
    template_name = 'tekken_game/person_detail.html'
    context_object_name = 'person_id'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonGame, id=person_id)


# def persons_detail(request, id):
#     if request.method == 'GET':
#         person_id = get_object_or_404(models.PersonGame, id=id)
#         return render(request, template_name='tekken_game/person_detail.html',
#                       context={'person_id': person_id}
#                       )


# Добавить персонажа
class CreatePersonView(generic.CreateView):
    template_name = 'tekken_game/crud/create_person.html'
    form_class = forms.TekkenForm
    success_url = '/'
    queryset = models.PersonGame.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonView, self).form_valid(form=form)


# def create_person_view(request):
#     if request.method == 'POST':
#         form = forms.TekkenForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/">На главную</a> ')
#     else:
#         form = forms.TekkenForm()
#     return render(request,
#                   template_name='tekken_game/crud/create_person.html',
#                   context={'form': form}
#                   )

class CreatePersonReviewView(generic.CreateView):
    template_name = 'tekken_game/crud/create_person_review.html'
    form_class = forms.ReviewForm
    success_url = '/'
    queryset = models.Review.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonReviewView, self).form_valid(form=form)


# def create_person_review_view(request):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Отзыв добавлен <a href="/">На главную</a>')
#     else:
#         form = forms.ReviewForm()
#         return render(request, template_name='tekken_game/crud/create_person_review.html', context={'form': form})
#

# Удаление
class DeletePersonView(generic.DeleteView):
    template_name = 'tekken_game/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonGame, id=person_id)


# def delete_person_view(request, id):
#     person_id = get_object_or_404(models.PersonGame, id=id)
#     person_id.delete()
#     return HttpResponse('Успешно удален <a href="/">На главную</a> ')


# Изменить
class EditPersonView(generic.UpdateView):
    template_name = 'tekken_game/crud/edit_person.html'
    form_class = forms.TekkenForm
    success_url = '/'
    queryset = models.PersonGame.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditPersonView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonGame, id=person_id)


# def edit_person_view(request, id):
#     person_id = get_object_or_404(models.PersonGame, id=id)
#     if request.method == 'POST':
#         form = forms.TekkenForm(instance=person_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/">На главную</a> ')
#     else:
#         form = forms.TekkenForm(instance=person_id)
#         return render(request,
#                       template_name='tekken_game/crud/edit_person.html',
#                       context={'form': form,
#                                'person_id': person_id})


class SearchView(generic.ListView):
    template_name = 'tekken_game/persons_list.html'
    context_object_name = 'persons'
    paginate_by = '5'

    def get_queryset(self):
        return models.PersonGame.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

