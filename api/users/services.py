import csv
import os

from users.models import User
class UserService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_user(self, user):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames = User.schema())
            writer.writerow(user.to_dict())


    def list_user(self):
        with open(self.table_name, mode = 'r') as f:
            reader = csv.DictReader(f, fieldnames= User.schema())

            return list(reader) 

    
    def update_user(self, updated_user):
        """Clients that are registered before."""
        users = self.list_user()

        """New client list with user updated."""
        updated_users = []
        for user in users:
            if updated_user.uid == user['uid']:
                updated_users.append(updated_user.to_dict)
            else:
                updated_users.append(user)

        self._save_to_disk(updated_users)


    def delete_user(self, user_ident):
        users = self.list_user()

        """New client list with user updated."""
        updated_users = []
        for user in users:
            if user_ident != user['identification']:
                updated_users.append(user)

        self._save_to_disk(updated_users)
    
    def _save_to_disk(self, users):
        tmp_tabla_name = self.table_name + '.tmp'
        with open(tmp_tabla_name , mode = 'w') as f:
            writer = csv.DictWriter(f, fieldnames= User.schema())
            writer.writerows(users)

        os.remove(self.table_name)
        os.rename(tmp_tabla_name, self.table_name)
