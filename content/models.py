from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    code = models.CharField(max_length=50, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    code = models.CharField(max_length=50, null=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}"


class Chapter(models.Model):
    chapter_no = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255)
    summary = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.chapter_no}- {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, through="Enrollment")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        unique_together = [
            ["student", "course"],
        ]


class Content(models.Model):
    title = models.CharField(max_length=255)
    file = models.URLField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(Student, on_delete=models.PROTECT)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    message = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)


class Rating(models.Model):
    RATING_LIFE_SAVER = 5
    RATING_COMPREHENSIVE = 4
    RATING_ADEQUATE = 3
    RATING_INSUFFICIENT = 2
    RATING_MISLEADING = 1

    RATINGS = [
        (RATING_LIFE_SAVER, "Life-Saver"),
        (RATING_COMPREHENSIVE, "Comprehensive"),
        (RATING_ADEQUATE, "Adequate"),
        (RATING_INSUFFICIENT, "Insufficient"),
        (RATING_MISLEADING, "Misleading"),
    ]

    score = models.IntegerField(choices=RATINGS, default=1)
    created_at = models.DateTimeField(auto_now=True)
    rated_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    rated_for = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{dict(self.RATINGS)[self.score]}"

    class Meta:
        unique_together = [
            ["rated_by", "rated_for"],
        ]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tagged_on = models.ForeignKey(Content, on_delete=models.CASCADE)
