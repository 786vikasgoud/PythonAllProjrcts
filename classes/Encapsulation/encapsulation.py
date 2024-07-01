class Bank:
    def __init__(self, acc_no=None, password=None):
        self._acc_no = acc_no
        self._password = password

    def setter(self, acc_no):
        self._acc_no = acc_no

    def set_password(self, password):
        self._password = password

    def get_acc_no(self):
        return self._acc_no

    def get_password(self):
        return self._password


sbi = Bank()
sbi.set_password("Vikas")
print(sbi.get_password())