from rest_framework.routers import SimpleRouter
from .views import StudentViewSet, FacultyViewSet, CourseViewSet, ClassroomViewSet, TimeslotViewSet, ScheduleViewSet


router = SimpleRouter()

router.register("Student", StudentViewSet)
router.register("Faculty", FacultyViewSet)
router.register("Classroom", ClassroomViewSet)
router.register("Course", CourseViewSet)
router.register("Timeslot", TimeslotViewSet)
router.register("Schedule", ScheduleViewSet)

urlpatterns = router.urls
