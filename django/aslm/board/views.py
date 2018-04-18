from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from board.forms import BoardCreationForm
from django.urls.base import reverse_lazy
from board.models import Board


# Create your views here.


class CreateBoardView(LoginRequiredMixin, FormView):
    """
    Class view to create board
    """

    form_class = BoardCreationForm
    template_name = 'board/create_board.html'
    success_url = reverse_lazy('board:show')

    def get_context_data(self, **kwargs):
        """
        Return context to be used by template
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = {'board_create': {'is_active': True}}
        return context

    def get_form_kwargs(self):
        """
        Return the keyword arguments for instantiating the form.
        :return:
        """
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """
        Save board when form is valid
        :param form:
        :return:
        """
        form.save()
        return super().form_valid(form)


class ShowBoardsView(LoginRequiredMixin, TemplateView):
    template_name = 'board/show_board.html'

    def get_context_data(self, **kwargs):
        """
        Return context to be used by template
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = {'board_show': {'is_active': True}}
        return context


class ListBoardsView(ListView):
    """
    Class view to show boards list using django pagination
    """
    model = Board
    paginate_by = 5
    ordering = '-created_at'
    paginate_by_kwarg = 'rpp'

    def get_rpp(self):
        """
        Return number of elements per page
        :return:
        """
        return self.request.GET.get(self.paginate_by_kwarg, self.paginate_by)

    def get(self, request, *args, **kwargs):
        """
        Return list of boards
        :param request: request
        :param args:
        :param kwargs:
        :return:
        """
        self.object_list = self.get_queryset()
        self.paginate_by = self.get_rpp()
        context = self.get_context_data()
        count = self.object_list.count()
        boards = []
        for board in context.get('object_list'):
            boards.append({
                'name': board.name,
                'description': board.description,
                'createdAt': board.created_at,
                'user': board.user.get_full_name()
            })
        return JsonResponse({'boards': boards, 'count': count})


