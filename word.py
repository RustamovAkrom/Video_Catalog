# # import os
# # from _config_ import settings

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_config_.settings")

# application = get_wsgi_application()


# # def mkdir_media_defaul_avatar():
# #     dir_name = "media/" + settings.DEFAULT_AUTH_USER_AVATAR_DIR

# #     if not os.path.exists(dir_name):
# #         os.makedirs(dir_name)

# #     if not os.path.exists(settings.READING_AVATAR_DIR):
# #         print("Default image reading not found on settings (READING_AVATAR_DIR = ?)")

# #     with open(settings.READING_AVATAR_DIR, "rb") as r:
# #         with open(dir_name + settings.DEFAULT_AUTH_USER_AVATAR_NAME, "wb") as w:
# #             w.write(r.read())

# # mkdir_media_defaul_avatar()
# from apps.videos.models import Categories



# CATEGORY_CHOICES()