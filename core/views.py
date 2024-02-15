from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class RegisteredUsersAPIView(APIView):
    serializer_class = RegisteredUsersSerializer

    def get_object(self, Phone_No):
        try:
            return RegisteredUsers.objects.get(Phone_No=Phone_No)
        except RegisteredUsers.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, Phone_No, format=None):
        instance = self.get_object(Phone_No)
        serializer = self.serializer_class(
            instance, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeAPIView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = self.serializer_class(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailAPIView(APIView):
    serializer_class = EmployeeSerializer

    def get_object_by_user_id(self, user_id):
        try:
            employee = Employee.objects.get(User_ID=user_id)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get_object_by_employee_id(self, employee_id):
        try:
            employee = Employee.objects.get(EmployeeID=employee_id)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, employee_id, format=None):
        employee = self.get_object_by_employee_id(employee_id)
        serializer = self.serializer_class(employee)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        employee = self.get_object_by_user_id(user_id)
        serializer = self.serializer_class(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerAPIView(APIView):
    serializer_class = EmployerSerializer

    def get(self, request, format=None):
        employers = Employer.objects.all()
        serializer = self.serializer_class(employers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerDetailAPIView(APIView):
    serializer_class = EmployerSerializer

    def get_object(self, employer_id):
        try:
            employer = Employer.objects.get(id=employer_id)
            return employer
        except Employer.DoesNotExist:
            raise Http404

    def get(self, request, employer_id, format=None):
        employer = self.get_object(employer_id)
        serializer = self.serializer_class(employer)
        return Response(serializer.data)

    def put(self, request, employer_id, format=None):
        employer = self.get_object(employer_id)
        serializer = self.serializer_class(employer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentEmployeeAPIView(APIView):
    def post(self, request, format=None):
        serializer = PaymentEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, employee_id):
        try:
            payment_employee = Payment_Employee.objects.get(Employee_ID=employee_id)
            return payment_employee
        except Payment_Employee.DoesNotExist:
            raise Http404

    def get(self, request, employee_id, format=None):
        payment_employee = self.get_object(employee_id)
        serializer = PaymentEmployeeSerializer(payment_employee)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

class PaymentEmployerAPIView(APIView):
    def post(self, request, format=None):
        serializer = PaymentEmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, employer_id):
        try:
            payment_employer = Payment_Employer.objects.get(Employer_ID=employer_id)
            return payment_employer
        except Payment_Employer.DoesNotExist:
            raise Http404

    def get(self, request, employer_id, format=None):
        payment_employer = self.get_object(employer_id)
        serializer = PaymentEmployerSerializer(payment_employer)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

class EmployeeToEmployerJobAPIView(APIView):
    serializer_class = EmployeeToEmployerJobSerializer

    def get_object_by_job_id(self, Job_ID):
        try:
            return Employee_To_Employer_Job.objects.filter(Job_ID=Job_ID)
        except Employee_To_Employer_Job.DoesNotExist:
            raise Http404

    def get_object_by_employee_id(self, Employee_ID):
        try:
            return Employee_To_Employer_Job.objects.filter(Employee_ID=Employee_ID)
        except Employee_To_Employer_Job.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Job_ID = request.query_params.get('job_id')
        Employee_ID = request.query_params.get('employee_id')

        if Job_ID:
            employee_to_employer_jobs = self.get_object_by_job_id(Job_ID)
        elif Employee_ID:
            employee_to_employer_jobs = self.get_object_by_employee_id(Employee_ID)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(employee_to_employer_jobs, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerToEmployeeJobAPIView(APIView):
    serializer_class = EmployerToEmployeeJobSerializer

    def get_object_by_job_id(self, Job_ID):
        try:
            return Employer_To_Employee_Job.objects.filter(Job_ID=Job_ID)
        except Employer_To_Employee_Job.DoesNotExist:
            raise Http404

    def get_object_by_employee_id(self, Employee_ID):
        try:
            return Employer_To_Employee_Job.objects.filter(Employee_ID=Employee_ID)
        except Employer_To_Employee_Job.DoesNotExist:
            raise Http404

    def get_object_by_employer_id(self, Employer_ID):
        try:
            return Employer_To_Employee_Job.objects.filter(Employer_ID=Employer_ID)
        except Employer_To_Employee_Job.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        job_id = request.query_params.get('job_id')
        employee_id = request.query_params.get('employee_id')
        employer_id = request.query_params.get('employer_id')

        if job_id:
            employer_to_employee_jobs = self.get_object_by_job_id(job_id)
        elif employee_id:
            employer_to_employee_jobs = self.get_object_by_employee_id(employee_id)
        elif employer_id:
            employer_to_employee_jobs = self.get_object_by_employer_id(employer_id)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(employer_to_employee_jobs, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobAPIView(APIView):
    serializer_class = JobSerializer

    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = self.serializer_class(jobs, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobExtendedAPIView(APIView):
    serializer_class = JobSerializer

    def get_job_by_employer_id(self, Employer_ID):
        jobs = Job.objects.filter(Employer_ID=Employer_ID)
        return jobs

    def get(self, request, Employer_ID=None, format=None):
        if Employer_ID:
            jobs = self.get_job_by_employer_id(Employer_ID)
            serializer = self.serializer_class(jobs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, job_id=None, format=None):
        try:
            job = Job.objects.get(pk=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeSubscriptionAPIView(APIView):
    serializer_class = EmployeeSubscriptionSerializer

    def get(self, request, format=None):
        subscriptions = EmployeeSubscription.objects.all()
        serializer = self.serializer_class(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmployerSubscriptionAPIView(APIView):
    serializer_class = EmployerSubscriptionSerializer

    def get(self, request, format=None):
        subscriptions = EmployerSubscription.objects.all()
        serializer = self.serializer_class(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RequestACallAPIView(APIView):
    serializer_class = RequestACallSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferredByAPIView(APIView):
    serializer_class = ReferredBySerializer

    def get(self, request, format=None):
        referrals = ReferredBy.objects.all()
        serializer = self.serializer_class(referrals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class JobCategoryAPIView(APIView):
    serializer_class = JobCategorySerializer

    def get(self, request, format=None):
        categories = JobCategory.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HiringTableAPIView(APIView):
    serializer_class = HiringTableSerializer

    def get_object(self, employer_id):
        try:
            return HiringTable.objects.filter(Employer_ID=employer_id)
        except HiringTable.DoesNotExist:
            raise Http404

    def get(self, request, employer_id, format=None):
        hiring_entries = self.get_object(employer_id)
        serializer = self.serializer_class(hiring_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactPhoneList(APIView):
    serializer_class = ContactPhoneSerializer

    def get(self, request, format=None):
        contact_phones = Contact_phone.objects.all()
        serializer = self.serializer_class(contact_phones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationAPIView(APIView):
    serializer_class = NotificationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_by_user_id(self, user_id):
        # Retrieve notifications for a specific user by User_ID
        notifications = Notification.objects.filter(User_ID=user_id).order_by('-Notification_Date')
        serializer = self.serializer_class(notifications, many=True)
        return Response(serializer.data)

    def get(self, request, user_id, format=None):
        return self.get_by_user_id(user_id)
