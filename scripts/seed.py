import itertools
import random

from django.core.management import call_command

from content import models
from scripts import fake


def populate_courses(n):
    for _ in range(n):
        course = models.Course()
        course.name = fake.name()
        course.slug = fake.to_slug(course.name)
        course.code = fake.code()
        course.description = fake.sentence()
        course.save()
        print("Course:", course.pk)


def populate_subjects(n):
    query_set = models.Course.objects.only("pk")

    for _ in range(n):
        subject = models.Subject()
        subject.name = fake.name()
        subject.slug = fake.to_slug(subject.name)
        subject.code = fake.code()
        subject.description = fake.sentence()
        subject.course = random.choice(query_set)
        subject.save()
        print("Subject:", subject.pk)


def populate_chapters(n):
    query_set = models.Subject.objects.only("pk")
    for _ in range(n):
        chapter = models.Chapter()
        chapter.chapter_no = random.randint(1, 10)
        chapter.name = fake.name()
        chapter.summary = fake.sentence()
        chapter.subject = random.choice(query_set)
        chapter.save()
        print("Chapter:", chapter.pk)


def populate_students(n):
    for _ in range(n):
        student = models.Student()
        student.first_name = fake.first_name()
        student.last_name = fake.last_name()
        student.email = fake.email(student.first_name, student.last_name)
        student.university = fake.name()
        student.save()
        print("Student:", student.pk)


def populate_enrollments(n):
    initial_records = {
        (enrollment.course, enrollment.student)
        for enrollment in models.Enrollment.objects.only("course", "student")
    }
    course_query_set = models.Course.objects.only("pk")
    student_query_set = models.Student.objects.only("pk")
    composite_primary_keys = list(
        set(itertools.product(course_query_set, student_query_set)) - initial_records
    )
    random.shuffle(composite_primary_keys)

    slots_available = len(composite_primary_keys)
    for _ in range(min(n, slots_available)):
        enrollment = models.Enrollment()
        enrollment.course, enrollment.student = composite_primary_keys.pop()
        enrollment.save()
        print(f"Enrollment: {enrollment.student.pk}, {enrollment.course.pk}")


def populate_contents(n):
    student_query_set = models.Student.objects.only("pk")
    chapter_query_set = models.Chapter.objects.only("pk")
    for _ in range(n):
        content = models.Content()
        content.title = fake.name()
        content.file = fake.url()
        content.upload_date = fake.date()
        content.uploader = random.choice(student_query_set)
        content.chapter = random.choice(chapter_query_set)
        content.save()
        print("Content:", content.pk)


def populate_comments(n):
    student_query_set = models.Student.objects.only("pk")
    content_query_set = models.Content.objects.only("pk")
    for _ in range(n):
        comment = models.Comment()
        comment.message = fake.sentence()
        comment.student = random.choice(student_query_set)
        comment.created_at = fake.date()
        comment.content = random.choice(content_query_set)
        comment.save()
        print("Comment:", comment.pk)


def populate_ratings(n):
    initial_records = {
        (enrollment.rated_by, enrollment.rated_for)
        for enrollment in models.Rating.objects.only("rated_by", "rated_for")
    }
    student_query_set = models.Student.objects.only("pk")
    content_query_set = models.Content.objects.only("pk")
    composite_primary_keys = list(
        set(itertools.product(student_query_set, content_query_set)) - initial_records
    )
    random.shuffle(composite_primary_keys)

    slots_available = len(composite_primary_keys)
    for _ in range(min(n, slots_available)):
        rating = models.Rating()
        rating.score = fake.score()
        rating.created_at = fake.date()
        rating.rated_by, rating.rated_for = composite_primary_keys.pop()
        rating.save()
        print(f"Rating: {rating.rated_by.pk}, {rating.rated_for.pk}")


def populate_tags(n):
    for _ in range(n):
        tag = models.Tag()
        tag.name = fake.name()
        tag.save()
        print("Tag:", tag.pk)


def populate_taggeditems(n):
    tag_query_set = models.Tag.objects.only("pk")
    content_query_set = models.Content.objects.only("pk")
    for _ in range(n):
        item = models.TaggedItem()
        item.tag = random.choice(tag_query_set)
        item.tagged_on = random.choice(content_query_set)
        item.save()
        print("TaggedItem:", item.pk)


def main():
    populate_courses(5)
    populate_subjects(30)
    populate_chapters(120)
    populate_students(500)
    populate_enrollments(500)
    populate_contents(1000)
    populate_comments(1200)
    populate_ratings(800)
    populate_tags(60)
    populate_taggeditems(240)


if __name__ == "__main__":
    call_command("migrate", "content", "zero")
    call_command("migrate", "content", "0001")
    main()
