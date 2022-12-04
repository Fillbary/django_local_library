from django.contrib import admin
from catalog.models import Book, Author, Genre, BookInstance, Language


class BooksInLine(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInLine]


class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInLine]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Genre)
admin.site.register(Language)



