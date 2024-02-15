from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Registered Users
    path('api/registered-users/', RegisteredUsersAPIView.as_view(), name='registered-users'),

    # Employee
    path('api/employees/', EmployeeAPIView.as_view(), name='employee-list'),
    path('api/employees/<int:user_id>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),

    # Employer
    path('api/employers/', EmployerAPIView.as_view(), name='employer-list'),
    path('api/employers/<int:employer_id>/', EmployerDetailAPIView.as_view(), name='employer-detail'),

    # Payment
    path('api/payment-employee/', PaymentEmployeeAPIView.as_view(), name='payment-employee'),
    path('api/payment-employer/', PaymentEmployerAPIView.as_view(), name='payment-employer'),

    # Notification API
    path('api/notifications/', NotificationAPIView.as_view(), name='notification-list'),
    path('api/notifications/<int:user_id>/', NotificationAPIView.as_view(), name='notification-detail'),

    # EmployeeToEmployerJob
    path('api/employee-to-employer-job/', EmployeeToEmployerJobAPIView.as_view(), name='employee-to-employer-job'),

    # EmployerToEmployeeJob
    path('api/employer-to-employee-job/', EmployerToEmployeeJobAPIView.as_view(), name='employer-to-employee-job'),

    # Job
    path('api/jobs/', JobAPIView.as_view(), name='job-list'),
    path('api/jobs/<int:job_id>/', JobExtendedAPIView.as_view(), name='job-extended'),

    # Employee Subscription
    path('api/employee-subscriptions/', EmployeeSubscriptionAPIView.as_view(), name='employee-subscriptions'),

    # Employer Subscription
    path('api/employer-subscriptions/', EmployerSubscriptionAPIView.as_view(), name='employer-subscriptions'),

    # Request A Call
    path('api/request-a-call/', RequestACallAPIView.as_view(), name='request-a-call'),

    # Referred By
    path('api/referred-by/', ReferredByAPIView.as_view(), name='referred-by'),

    # Job Category
    path('api/job-categories/', JobCategoryAPIView.as_view(), name='job-categories'),

    # Hiring Table
    path('api/hiring-table/<int:employer_id>/', HiringTableAPIView.as_view(), name='hiring-table'),
    path('api/contact_phones/', ContactPhoneList.as_view(), name='contact-phone-list')


]
