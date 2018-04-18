from django import forms
from board.models import Board


class BoardCreationForm(forms.ModelForm):
    """
    A form that creates a board
    """
    class Meta:
        model = Board
        fields = ("name", "description")

    def __init__(self, *args, **kwargs):
        """
        Init BoardCreationForm
        :param args:
        :param kwargs:
        """
        if 'request' in kwargs:
            self.request = kwargs['request']
            kwargs.pop('request')
            super().__init__(*args, **kwargs)
        else:
            raise ValueError('Request parameter must be set to instantiate {}'.format(self.__class__.name))

    def save(self, commit=True):
        board = super().save(commit=False)
        board.user = self.request.user
        if commit:
            board.save()
        return board