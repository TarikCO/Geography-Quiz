from django.urls import path
from .views import (
    quiz1_end_view, 
    quiz1_highscore_view, 
    save_highscore_view, 
    get_highscores_view, 
    get_quiz2_highscores_view,
    get_quiz3_highscores_view,
)

from quizzes.views import (
    quiz1_view, 
    quiz2_view,
    quiz3_view,
    quiz1_game_view,
    quiz2_game_view,
    quiz3_game_view,
    quiz1_end_view,
    quiz2_end_view,
    quiz3_end_view,
    quiz1_highscore_view,
    quiz2_highscore_view,
    quiz3_highscore_view,
)

urlpatterns = [
    path('quiz1/', quiz1_view, name="quiz1"),
    path('quiz2/', quiz2_view, name="quiz2"),
    path('quiz3/', quiz3_view, name="quiz3"),
    path('quiz1_game/', quiz1_game_view, name="quiz1_game"),
    path('quiz2_game/', quiz2_game_view, name="quiz2_game"),
    path('quiz3_game/', quiz3_game_view, name="quiz3_game"),
    path('quiz1_end/', quiz1_end_view, name='quiz1_end'),
    path('quiz2_end/', quiz2_end_view, name="quiz2_end"),
    path('quiz3_end/', quiz3_end_view, name="quiz3_end"),

    path('quiz1_highscore/', quiz1_highscore_view, name='quiz1_highscore'),
    path('get_highscores/', get_highscores_view, name='get_highscores'),

    path('quiz2_highscore/', quiz2_highscore_view, name='quiz2_highscore'),
    path('get_quiz2_highscores/', get_quiz2_highscores_view, name='get_quiz2_highscores'),

    path('quiz3_highscore/', quiz3_highscore_view, name="quiz3_highscore"),
    path('get_quiz3_highscores/', get_quiz3_highscores_view, name='get_quiz3_highscores'),

    path('save_highscore/<int:quiz_number>/', save_highscore_view, name='save_highscore'),
]

