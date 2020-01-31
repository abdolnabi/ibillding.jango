from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name='', last_name='', password=None, is_active=False,
                    financial_credit=0.0):
        """
        Create and save user
        """
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            financial_credit=financial_credit,
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, email, password, first_name, last_name):
        user = self.create_user(username, email, first_name, last_name, password)

        user.is_admin = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self.db)

        return user
