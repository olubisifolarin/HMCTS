from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value

    def validate_due_date(self, value):
        # ensure due date is in the future
        if value <= timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
