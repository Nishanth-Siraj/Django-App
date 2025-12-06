>>> from app.models import Post
>>> posts = Post.objects.filter(title__icontains="Z")
>>> for post in posts:
...     print(post.title)
... 
z-post
>>> posts = Post.objects.filter(created_at__date="2025-11-24")
>>> for post in posts:
...     print(post.title)
... 
New Post
z-post
>>> posts = Post.objects.filter(created_at__date="2025-11-25")
>>> for post in posts:
...     print(post.title)
... 
>>> posts = Post.objects.filter(created_at__date__iexact="11-25")
>>> for post in posts:
...     print(post.title)
... 
>>> posts = Post.objects.filter(created_at__date__icontains="11-25")
>>> for post in posts:
...     print(post.title)
... 
>>> posts = Post.objects.filter(created_at__date="2025-11-25").order_by('-id')
>>> for post in posts:
...     print(post.title)
... 
>>> posts = Post.objects.filter(created_at__date__icontains="11-24")
>>> 
>>> for post in posts:
...     print(post.title)
... 
New Post
z-post
>>> 
>>> posts = Post.objects.filter(created_at__date="2025-11-25").order_by('-id')
>>> for post in posts:
...     print(post.title)
... 
>>> 
>>> posts = Post.objects.filter(created_at__date="2025-11-24").order_by('-id')
>>> for post in posts:
...     print(post.title)
... 
z-post
New Post
>>> posts = Post.objects.filter(created_at__date="2025-11-24").filter(title__icontains="z")
>>> for post in posts:
...     print(post.title)
... 
z-post

>>> from app.models import Post, Tags
>>> posts = Post.objects.prefetch_related('tags')
>>> for post in posts:
...     for tag in post.tags.all():
...             print(tag.tag)
... 
new tag
z tag
>>> 

>>> tags = Tags.objects.select_related('post')
>>> for tag in tags:
...     print(tag.post.title)
... 
z-post
New Post

>>> posts = Post.objects.prefetch_related(Prefetch('tags',queryset=Tags.objects.filter(tag__icontains="z")))
>>> for post in posts:
...     for pst in post.tags.all():
...             print(pst.name)
... 
>>> for post in posts:
...     for pst in post.tags.all():
...             print(pst.tag)
... 
z tag
>>> from app.models import Post, Tags
>>> posts = Post.objects.prefetch_related('tags')
>>> for post in posts:
...     for tag in post.tags.all().values('tag'):
...             print(tag)
... 
{'tag': 'new tag'}
{'tag': 'z tag'}
>>> 
>>> for post in posts:
...     for tag in post.tags.values_list('tag',flat=True):
...             print(tag)
... 
new tag
z tag
>>> 
>>> from app.models import Post, Tags
>>> from django.db.models import Prefetch
>>> posts = Post.objects.prefetch_related(Prefetch('tags',queryset=Tags.objects.filter(tag__icontains='Z')))
>>> for post in posts:
...     for tag in post.tags.values('post__title','tag'):
...             print(tag)
... 
{'post__title': 'z-post', 'tag': 'z tag'}
