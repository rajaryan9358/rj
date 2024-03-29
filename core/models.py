from django.db import models
from django.utils import timezone

# Create your models here.
class RegisteredUsers(models.Model):
    Phone_No = models.IntegerField(primary_key=True)
    Device_ID = models.CharField(max_length=500)
    Account_Type = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Notification(models.Model):
    User_ID = models.ForeignKey('RegisteredUsers', on_delete=models.CASCADE)
    Notification_ID = models.AutoField(primary_key=True)
    Notification_Text = models.TextField()
    Notification_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User_ID
class Employee(models.Model):
    Active = models.BooleanField(default=False)
    Approved = models.BooleanField(default=False)
    Profile_Completed = models.BooleanField(default=False)
    User_ID = models.ForeignKey('RegisteredUsers', on_delete=models.CASCADE)
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Contact_No = models.CharField(max_length=20)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    State_Ut = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Referred_By = models.CharField(max_length=100, default='-')
    Qualification = models.CharField(max_length=50)
    Expected_Salary = models.IntegerField()
    Salary_Frequency = models.CharField(max_length=50)
    Preferred_Shift = models.CharField(max_length=50)
    Preferred_State_Ut = models.CharField(max_length=100)
    Preferred_City = models.CharField(max_length=100)
    Email_ID = models.CharField(max_length=100, default='-')
    Experience = models.TextField(default='-')
    Job_Preference = models.CharField(max_length=100)
    Profile_Picture = models.ImageField(upload_to='media/profile', default='abc.png')
    Aadhar_Number = models.CharField(max_length=20)
    Aadhar_Front = models.ImageField(upload_to='media/aadharfront', default='')
    Aadhar_Back = models.ImageField(upload_to='media/aadharback', default='')
    Contact_Credits = models.IntegerField(default=0)
    Interest_Credits = models.IntegerField(default=0)
    Total_Contact_Credits = models.IntegerField(default=0)
    Total_Interest_Credits = models.IntegerField(default=0)
    Validity = models.DateTimeField()
    Active_Pack = models.ForeignKey('EmployeeSubscription', on_delete=models.SET_NULL, null=True)
    Profile_OTP = models.IntegerField()
    Device_ID = models.CharField(max_length=500,default='-')

    def __str__(self):
        return self.Name

class Employer(models.Model):
    User_ID = models.ForeignKey('RegisteredUsers', on_delete=models.CASCADE)
    Active = models.BooleanField(default=False)
    Approved = models.BooleanField(default=False)
    Profile_Completed = models.BooleanField(default=False)
    Name = models.CharField(max_length=200)
    Organization = models.CharField(max_length=200)
    EmployerID = models.AutoField(primary_key=True)
    City = models.CharField(max_length=100)
    State_Ut = models.CharField(max_length=100)
    Email_ID = models.CharField(max_length=100, default='-')
    Organization_Type = models.CharField(max_length=100)
    Address = models.TextField()
    Active_Pack = models.ForeignKey('EmployerSubscription', on_delete=models.SET_NULL, null=True)
    Total_Job_Post_Credits = models.IntegerField(default=0)
    Total_Contact_Credits = models.IntegerField(default=0)
    Total_Interest_Credits = models.IntegerField(default=0)
    Job_Post_Credits = models.IntegerField(default=0)
    Contact_Credits = models.IntegerField(default=0)
    Interest_Credits = models.IntegerField(default=0)
    Validity = models.DateTimeField()
    Device_ID = models.CharField(max_length=500, default='-')
    Referred_By = models.CharField(max_length=100, default='-')

    def __str__(self):
        return self.Name

class Payment_Employee(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    inv_date = models.DateTimeField(default=timezone.localtime, editable=False)
    inv_number = models.CharField(max_length=100,default='-')
    user_name = models.CharField(max_length=100,default='-')
    name = models.CharField(max_length=100,default='-')
    address = models.TextField(default='-')
    subscription_name = models.CharField(max_length=500,default='-')
    subscription_start = models.DateTimeField(default=timezone.localtime)
    subscription_end = models.DateTimeField(default=timezone.localtime)
    list_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order ID: {self.Order_ID}, Employee: {self.Employee_ID}"

class Payment_Employer(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    inv_date = models.DateTimeField(default=timezone.localtime, editable=False,)
    inv_number = models.CharField(max_length=100,default='-')
    user_name = models.CharField(max_length=100,default='-')
    name = models.CharField(max_length=100,default='-')
    address = models.TextField(default='-')
    subscription_name = models.CharField(max_length=500,default='-')
    subscription_start = models.DateTimeField(default=timezone.localtime)
    subscription_end = models.DateTimeField(default=timezone.localtime)
    list_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order ID: {self.Order_ID}, Employer: {self.Employer_ID}"

class Job(models.Model):
    Job_ID = models.AutoField(primary_key=True)
    Job_Profile = models.CharField(max_length=200)
    Vacancy = models.IntegerField()
    Employer_ID = models.ForeignKey(RegisteredUsers, on_delete=models.CASCADE)
    Contact_No = models.CharField(max_length=100)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Salary_Offered = models.IntegerField()
    Frequency = models.CharField(max_length=100)
    Sent_Interests = models.IntegerField()
    Received_Interests = models.IntegerField()
    Job_Image = models.CharField(max_length=100)

    def __str__(self):
        return f"Job ID: {self.Job_ID}, Job Profile: {self.Job_Profile}"

class Employee_To_Employer_Job(models.Model):
    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Organization_Name = models.CharField(max_length=300)
    Organization_Category = models.CharField(max_length=200)
    Photo_Url = models.CharField(max_length=300)
    City = models.CharField(max_length=200)
    State_Ut = models.CharField(max_length=200)
    Salary = models.IntegerField()
    Salary_Frequency = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    First_Pref = models.CharField(max_length=200)

    def __str__(self):
        return f"Job ID: {self.Job_ID}, Employee: {self.Employee_ID}, Employer: {self.Employer_ID}"

class Employer_To_Employee_Job(models.Model):
    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Photo_Url = models.CharField(max_length=300)
    City = models.CharField(max_length=200)
    State_Ut = models.CharField(max_length=200)
    Salary = models.IntegerField()
    Salary_Frequency = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    First_Pref = models.CharField(max_length=200)

    def __str__(self):
        return f"Job ID: {self.Job_ID}, Employee: {self.Employee_ID}, Employer: {self.Employer_ID}"

class Employee_To_Employer_Call(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Organization_Name = models.CharField(max_length=300)
    Organization_Category = models.CharField(max_length=200)
    Photo_Url = models.CharField(max_length=300)
    City = models.CharField(max_length=200)
    State_Ut = models.CharField(max_length=200)
    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Contact_No = models.CharField(max_length=20)

    def __str__(self):
        return f"Date: {self.Date}, Employee: {self.Employee_ID}, Employer: {self.Employer_ID}"

class Employer_To_Employee_Call(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Photo_Url = models.CharField(max_length=300)
    City = models.CharField(max_length=200)
    State_Ut = models.CharField(max_length=200)
    Salary = models.IntegerField()
    Salary_Frequency = models.CharField(max_length=100)
    Name = models.CharField(max_length=200)
    First_Pref = models.CharField(max_length=200)
    Contact_No = models.CharField(max_length=20)

    def __str__(self):
        return f"Date: {self.Date}, Employee: {self.Employee_ID}, Employer: {self.Employer_ID}"



class EmployeeSubscription(models.Model):
    Plan_Name = models.CharField(max_length=200, primary_key=True)
    Text = models.TextField()
    Visible = models.BooleanField(default=True)
    Validity_In_Days = models.IntegerField()
    Price = models.IntegerField()
    Discounted_Price = models.IntegerField()

    def __str__(self):
        return self.Plan_Name

class EmployerSubscription(models.Model):
    Plan_Name = models.CharField(max_length=200, primary_key=True)
    Text = models.TextField()
    Visible = models.BooleanField(default=True)
    Validity_in_days = models.IntegerField()
    Price = models.IntegerField()
    Discounted_Price = models.IntegerField()

    def __str__(self):
        return self.Plan_Name

class RequestACall(models.Model):
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class ReferredBy(models.Model):
    Referral_ID = models.AutoField(primary_key=True)
    Referrer_Name = models.CharField(max_length=200, default="-")

    def __str__(self):
        return self.Referrer_Name


class JobCategory(models.Model):
    Category = models.CharField(max_length=200, primary_key=True)
    Photo = models.CharField(max_length=100, default='others.png')

    def __str__(self):
        return self.Category

class HiringTable(models.Model):
    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Employer_ID = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Candidate_Name = models.CharField(max_length=200)
    Job_Profile = models.CharField(max_length=200)
    Salary = models.IntegerField()
    Salary_Frequency = models.CharField(max_length=200)
    Aadhar_No = models.CharField(max_length=20)
    Contact_No = models.CharField(max_length=20)

    def __str__(self):
        return f"Job: {self.Job_ID}, Employee: {self.Employee_ID}, Employer: {self.Employer_ID}"

class Contact_phone(models.Model):
    Phone = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.Phone
