from django.contrib import admin
from .models import Book, Author, BookCategory, Staff, Member, Record

# admin.site.register()
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'category_name', 'book_price', 'number_of_copies', 'books_in_stock', 'availability',)
    list_filter = ('availability', 'category_name')
    search_fields = ('book_name',)
    ordering = ('book_name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'staff_email', 'staff_mobile_number',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_mobile_number', 'member_email',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('borrowed_member', 'borrowed_book', 'borrowed_date', 'return_date','issued_staff','is_returned',)


admin.site.register(Book, BookAdmin,)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookCategory,BookCategoryAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Record,RecordAdmin)
