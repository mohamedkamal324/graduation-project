from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class MyPasswordResetTokenGen(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return six.text_type(user.pk) +six.text_type(timestamp)

password_reset_token = MyPasswordResetTokenGen()