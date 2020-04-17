# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser, PermissionsMixin
# )

# class UserManager(BaseUserManager):
#     def create_user(self, email,  name, password=None):

#         if not email:
#             raise ValueError(_('Users must have an email address'))

#         user = self.model(
#             email=self.normalize_email(email),
#             name = name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password):

#         user = self.create_user(
#             email=email,
#             name = name,
#         )
#         user.is_superuser = True
#         user.is_active = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
    
#     name = models.CharField(
#         verbose_name = '이름',
#         max_length=15,
#         null=True
#     )

#     email = models.EmailField(
#         verbose_name = '이메일',
#         max_length=255,
#         unique=True,
#         null=True
#     )

   
#     is_active = models.BooleanField(default=False)
    
#     objects = UserManager()

#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS = [
#         'name', 
#         'email',
#     ]

#     def __str__(self):
#         return self.name

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_superuser