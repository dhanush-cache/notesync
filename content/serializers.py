from rest_framework import serializers

from content import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ["id", "name", "slug", "code", "description"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ["id", "name", "slug", "code", "description", "course"]


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ["id", "chapter_no", "name", "summary", "subject"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ["id", "first_name", "last_name", "email", "university", "courses"]

    courses = serializers.PrimaryKeyRelatedField(
        queryset=models.Course.objects.all(), many=True
    )


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ["id", "title", "file", "upload_date", "uploader", "chapter", "rating"]

    rating = serializers.FloatField(source="average_rating", read_only=True)

    # def get_rating(self, content):
    #     rating = serializers.FloatField(source='average_rating', read_only=True)
    #     # models.Rating.objects.filter(rated_for=content)

    #     if ratings:
    #         # average_rating = ratings.aggregate(Avg("score"))["score__avg"]
    #         # return round(average_rating, 2)
    #         return sum(ratings) / len(ratings)
    #     return None
