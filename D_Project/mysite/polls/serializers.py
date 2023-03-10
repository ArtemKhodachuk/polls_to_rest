from rest_framework import serializers
from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    # question = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    choice_set=ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date', 'choice_set']
