from django.urls import path 
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import *


router = routers.DefaultRouter()
router.register('category', CategoryAPI)
router.register('course', CourseAPI)
router.register('enrollment', EnrollmentAPI)
router.register('assignment', AssignmentAPI)
router.register('submission', SubmissionAPI)
router.register('sponsorship', SponsorshipAPI)
router.register('payment', PaymentAPI)
router.register('notification', NotificationAPI)
router.register('manage-user', UserAPI)


urlpatterns = [
    
] + router.urls + debug_toolbar_urls()


