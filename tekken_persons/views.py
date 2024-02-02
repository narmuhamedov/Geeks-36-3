from django.shortcuts import get_object_or_404
from . import models, forms
from django.http import JsonResponse
from django.views import generic


class PersonsListView(generic.ListView):
    model = models.PersonGame
    template_name = 'tekken_game/persons_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return self.model.objects.all()


# подробная инфа
class PersonDetailView(generic.DetailView):
    template_name = 'tekken_game/person_detail.html'
    context_object_name = 'person_id'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonGame, id=person_id)


# Добавить персонажа
class CreatePersonView(generic.CreateView):
    template_name = 'tekken_game/crud/create_person.html'
    form_class = forms.TekkenForm
    success_url = '/'
    queryset = models.PersonGame.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonView, self).form_valid(form=form)


#добавить отзыв новый вариант
class CreatePersonReviewView(generic.CreateView):
    model = models.Review
    form_class = forms.ReviewForm
    template_name = 'tekken_game/crud/create_person_review.html'
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonReviewView, self).form_valid(form=form)




# Удаление
class DeletePersonView(generic.DeleteView):
    template_name = 'tekken_game/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.PersonGame, id=person_id)


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
