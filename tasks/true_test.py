import requests


class TestCompanyRegistrationRestaurant:
    company_register_url = "http://localhost/addressbook/edit.php"
    valid_registration_data = {
        'firstname': 'My new company',
        'middlename': 'Isaac',
        'lastname': 'Newton',
        'nickname': '+447911123456',
        'title': 'secret_pass',
        'company': 'secret_pass',
        'address': 'Woolsthorpe Manor, Woolsthorpe-by-Colsterworth, Linconshire',
        'home': '3172418374',
        'mobile': "airGrill",
        'work': 10,
        'photo': "C:\\Users\\Nata\\PycharmProjects\\test_image.png",
        'fax': 2,
        'email': "user@example.com",
        'email2': "user2@example.com",
        'email3': "user3@example.com",
        'homepage': "https://google.com",
        'bday': "1",
        'bmonth': "10",
        'byear': "2021",
        'aday': "1",
        'amonth': "10",
        'ayear': "2021",
        'new_group': "9",
        "address2": "123",
        "phone2": "567",
        "notes": "512"
    }

    def test_worker_registration(self):
        r = requests.Session()
        message = "Information entered into address book."
        response = r.post(self.company_register_url, {'user': 'admin', 'pass': 'secret'})

        if response.status_code == 200:
            response = r.post(self.company_register_url, self.valid_registration_data, files=dict(photo="C:\\Users\\Nata\\PycharmProjects\\test_image.png"))

        assert message in response.text
