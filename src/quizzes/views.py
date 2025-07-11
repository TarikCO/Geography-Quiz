from django.shortcuts import render
from account.models import Account
from django.http import JsonResponse
from .models import HighScore, Quiz2HighScore, Quiz3HighScore
import json

def quiz1_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/main/quiz1.html", context)


def quiz2_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/main/quiz2.html", context)


def quiz3_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/main/quiz3.html", context)


def quiz1_game_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/games/quiz1_game.html", context)


def quiz2_game_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/games/quiz2_game.html", context)


def quiz3_game_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/games/quiz3_game.html", context)


def quiz1_end_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/end/quiz1_end.html", context)


def quiz2_end_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/end/quiz2_end.html", context)


def quiz3_end_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/end/quiz3_end.html", context)





def quiz1_highscore_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "quizzes/highscores/quiz1_highscore.html", context)

def get_highscores_view(request):
    high_scores = HighScore.objects.order_by('-score')[:10]
    high_scores_data = [{'name': score.name, 'score': score.score} for score in high_scores]
    return JsonResponse({'highscores': high_scores_data})




def quiz2_highscore_view(request):
    context = {}
    quiz2_high_scores = Quiz2HighScore.objects.order_by('-score')[:10]
    accounts = Account.objects.all()
    context['quiz2_high_scores'] = quiz2_high_scores
    context['accounts'] = accounts

    return render(request, "quizzes/highscores/quiz2_highscore.html", context)

def get_quiz2_highscores_view(request):
    quiz2_high_scores = Quiz2HighScore.objects.order_by('-score')[:10]
    quiz2_high_scores_data = [{'name': score.name, 'score': score.score} for score in quiz2_high_scores]
    return JsonResponse({'highscores': quiz2_high_scores_data})




def quiz3_highscore_view(request):
    context = {}
    quiz3_high_scores = Quiz3HighScore.objects.order_by('-score')[:10]
    accounts = Account.objects.all()
    context['quiz3_high_scores'] = quiz3_high_scores
    context['accounts'] = accounts

    return render(request, "quizzes/highscores/quiz3_highscore.html", context)

def get_quiz3_highscores_view(request):
    quiz3_high_scores = Quiz3HighScore.objects.order_by('-score')[:10]
    quiz3_high_scores_data = [{'name': score.name, 'score': score.score} for score in quiz3_high_scores]
    return JsonResponse({'highscores': quiz3_high_scores_data})





def save_highscore_view(request, quiz_number):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        score = int(data.get('score'))

        if not request.user.is_authenticated and not name:
            return JsonResponse({'error': 'Please enter your name to save the score.'}, status=400)

        if request.user.is_authenticated:
            name = request.user.username

        if quiz_number == 1:
            HighScore.objects.create(name=name, score=score)
        elif quiz_number == 2:
            Quiz2HighScore.objects.create(name=name, score=score)
        elif quiz_number == 3:
            Quiz3HighScore.objects.create(name=name, score=score)

        return JsonResponse({'redirect': f'/quiz{quiz_number}_highscore/'})