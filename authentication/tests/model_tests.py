from django.test import TestCase
import authentication.models as auth_models
import uuid
# Create your tests here.


class TestUserModal(TestCase):
    def setUp(self):
        user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

    def test_existence_of_user_created(self):

        check_existence = auth_models.User.objects.filter(
            first_name='timo').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_user_record(self):

        user_store = auth_models.User.objects.get(first_name='timo')
        user_store.first_name = 'masiko'
        user_store.save()
        check_existence = auth_models.User.objects.filter(
            first_name='masiko').exists()
        self.assertTrue(check_existence)

    def test_delete_of_user_record(self):

        user_store = auth_models.User.objects.get(first_name='timo')
        user_store.delete()
        check_existence = auth_models.User.objects.filter(
            first_name='timo').exists()
        self.assertFalse(check_existence)


# guidance with the crud operation