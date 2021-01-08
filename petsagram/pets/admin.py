from django.contrib import admin

from pets.models import Pet, Like, Comment


class LikeInLine(admin.TabularInline):
    model = Like


class AdminPet(admin.ModelAdmin):
    list_display = ('id', 'type', 'name')
    list_filter = ('type', 'age',)
    inlines = (
        LikeInLine,
    )


admin.site.register(Pet, AdminPet)
admin.site.register(Comment)
# admin.site.register(Like,)
