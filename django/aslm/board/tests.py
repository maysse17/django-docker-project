from django.test import TestCase
from adil.board.models import Board
from django.contrib.auth.models import User

# Create your tests here.


class BoardTestCase(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='user_test')
            print('user exist')
        except:
            print('user not exist created it')
            self.user = User(username='user_test',
                             password='test', email='a@gmail.com').save()

    # def tearDown(self):
    #     for board in Board.objects.all():
    #         board.delete()

    def test_create_board(self):
        board = Board(name='test', user=self.user).save()
        print(board)
