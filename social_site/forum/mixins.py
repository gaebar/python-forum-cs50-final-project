from django.contrib.auth.mixins import UserPassesTestMixin

# Mixins Documentation:
# https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/
# https://docs.djangoproject.com/en/dev/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin


class StaffMixing(UserPassesTestMixin):
    """
    The purpose of this mixin is to make sure that only the staff can create new sections.
    The test can be considered passed if the test_func() function returns a Boolean value of True
    """

    def test_func(self):
        return self.request.user.is_staff
