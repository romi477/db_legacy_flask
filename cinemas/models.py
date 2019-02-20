from app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iso = db.Column(db.String(2))
    name = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Customer {self.id} - {self.name} [{self.iso}]>'


