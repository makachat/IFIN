from django.http import Http404
class Post:

    POSTS = [
        {'id': '1', 'title': 'First post', 'body': 'This is my content of first Post'},
        {'id': '2', 'title': 'Second post', 'body': 'This is my content of Second Post'},
        {'id': '3', 'title': 'third post', 'body': 'This is my content of third post'}
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404('Sorry, post #{} not found'.format(id))
