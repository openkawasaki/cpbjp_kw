from django.shortcuts import render

# Create your views here.

# ----------------------------
def index(request):
    """
    index()
    """

    contexts = {}

    # 現在ログインしている?
    if request.user.is_authenticated:
        contexts['user'] = {"username": request.user.username, "user_id": request.user.id, "is_authenticated": True}


    # パラメータ設定
    contexts = {}

    return render(request, 'web/index.html', contexts)

