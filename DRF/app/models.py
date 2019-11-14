from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    author_name = models.CharField(max_length=100, help_text='Enter author name')
    
    def __str__(self):
        return self.author_name
class BookCategory(models.Model):
    category_name = models.CharField(max_length=100, help_text='Enter book category')

    def __str__(self):
        return self.category_name

class Book(models.Model):
    book_name = models.CharField(max_length=200, help_text='Enter book name')
    isbn = models.CharField(max_length=200)
    book_price = models.IntegerField()
    availability = models.BooleanField()
    author_name = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    category_name = models.ForeignKey(BookCategory, null=True, on_delete=models.CASCADE)
    number_of_copies = models.IntegerField(default=1, help_text='number of available copies')
    books_in_stock = models.IntegerField(help_text='number of books in stock')
    book_description = models.TextField(help_text='overview of book')

    def __str__(self):
        return self.book_name

class Staff(models.Model):
    staff_id = models.CharField(max_length=100, help_text='Enter staff id')
    staff_name = models.CharField(max_length=200, help_text='Enter staff name')
    staff_mobile_number = models.IntegerField(help_text='Enter staff mobile number')
    staff_email = models.CharField(max_length=100, help_text='Enter staff email')
    staff_address = models.CharField(max_length=200, help_text='Enter staff address')

    def __str__(self):
        return self.staff_name
    
class Member(models.Model):
    member_id = models.CharField(unique=True, max_length=5, help_text='Enter member member id', validators=[MinLengthValidator(5)])
    member_name = models.CharField(max_length=200, help_text='Enter staff member name')
    member_mobile_number = models.IntegerField(help_text='Enter member mobile number')
    member_email = models.CharField(max_length=100, help_text='Enter member email')
    member_address = models.CharField(max_length=200, help_text='Enter member address')

    def __str__(self):
        return self.member_name

class Record(models.Model):
    borrowed_member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    return_date = models.DateField()
    issued_staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
