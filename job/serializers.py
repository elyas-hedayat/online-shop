from rest_framework import serializers

from .models import Apply, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "thumbnail",
            "description",
        )


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "description",
            "resume",
            "job",
        )
