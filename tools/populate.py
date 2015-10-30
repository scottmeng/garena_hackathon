from hackathon.models import Question
from hackathon.models import AnswerHistory
from django.contrib.auth.models import User

def pDB():
    #add question and answer history
    user = User.objects.get(pk=1)
    q = Question(1, "test question", user.pk, "yes", "no", create_time="2015-11-11")
    q.save()
    a = AnswerHistory(1, user.pk, q.pk, AnswerHistory.LEFT)
    a.save()

    q = Question(2, "is Burning the best in DOTA2", user.pk, "yes", "no", create_time="2015-11-11")
    q.save()
    a = AnswerHistory(3, user.pk, q.pk, AnswerHistory.LEFT)
    a.save()

if __name__ == "__main__":
    populateDB()