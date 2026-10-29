from django.contrib import admin

from apps.users.models import ProfileModel, UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('-id',)


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'user', 'created_at')
    search_fields = ('name', 'surname', 'user__email')