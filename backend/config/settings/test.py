from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"