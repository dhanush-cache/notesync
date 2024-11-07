from rest_framework.routers import DefaultRouter

from content import views

router = DefaultRouter()
router.register("courses", views.CourseViewSet)
router.register("subjects", views.SubjectViewSet)
router.register("chapters", views.ChapterViewSet)
router.register("students", views.StudentViewSet)
router.register("contents", views.ContentViewSet, basename="hello")

urlpatterns = router.urls
