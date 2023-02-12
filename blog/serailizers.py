from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "thumbnail",
        )


class BlogDetailSerializer(BlogSerializer):
    class Meta:
        model = BlogSerializer.Meta.model
        fields = BlogSerializer.Meta.fields + ("description", "estimate_reading_time")
