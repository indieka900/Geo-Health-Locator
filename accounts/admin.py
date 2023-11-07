from django.contrib import admin

from django.contrib.auth.models import Group
from accounts.models import (User, Profile)

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["email", "username"]
    list_display = ("username", "first_name", "middle_name", 
                    "last_name", "identification", "email", "gender", "role",
                    "phone", "county", "sub_county", "ward", "location", 
                    "sub_location", "village", 
                    "is_active", "is_admin",
                    "is_staff", "timestamp")

# @admin.register(Profile)    
# class ProfileAdmin(admin.ModelAdmin):
#     search_fields = ["get_username",]
#     list_display = ("get_username", "user", "bio", "profile_picture")

#     def get_username(self, obj):
#         return obj.user.username
#     get_username.short_description = "Username"
#     get_username.admin_order_field = "user__username"
    
# @admin.register(Administrator)
# class AdministratorAdmin(admin.ModelAdmin):
#     search_fields = ["get_username",]
#     list_display = ("get_username", "first_name", "middle_name", 
#                     "last_name", "county", "sub_county")
    
#     def get_username(self, obj):
#         return obj.user.username
#     get_username.short_description = "Username"
#     get_username.admin_order_field = "user__username"

# @admin.register(CommunityMember)
# class CommunityMemberAdmin(admin.ModelAdmin):
#     search_fields = ["get_username",]
#     list_display = ("get_username", "county",
#                     "sub_county", "ward", "location",
#                     "sub_location", "village")
    
#     def get_username(self, obj):
#         return obj.user.username
#     get_username.short_description = "Username"
#     get_username.admin_order_field = "user__username"

# @admin.register(MedicalPersonel)
# class MedicalPersonelAdmin(admin.ModelAdmin):
#     search_fields = ["get_username",]
#     list_display = ("kmdb_number", "email")

#     def get_username(self, obj):
#         return obj.user.username
#     get_username.short_description = "Username"
#     get_username.admin_order_field = "user__username"
    