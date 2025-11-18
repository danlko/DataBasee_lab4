from app.my_project import db


class RetailNetwork(db.Model):
    __tablename__ = 'retail_network'  #

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    supermarkets = db.relationship('Supermarket', back_populates='retail_network', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Supermarket(db.Model):
    __tablename__ = 'supermarket'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    avg_visitors_per_day = db.Column(db.Integer, nullable=False)
    working_hours = db.Column(db.String(50), nullable=False)
    visiting_hours = db.Column(db.String(50), nullable=False)

    network_id = db.Column(db.BigInteger, db.ForeignKey('retail_network.id'), nullable=False)

    retail_network = db.relationship('RetailNetwork', back_populates='supermarkets')

    departments = db.relationship('Department', back_populates='supermarket', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'area': self.area,
            'description': self.description,
            'avg_visitors_per_day': self.avg_visitors_per_day,
            'working_hours': self.working_hours,
            'visiting_hours': self.visiting_hours,
            'network_id': self.network_id,
            # Ми можемо навіть додати дані з пов'язаної мережі
            'network_name': self.retail_network.name if self.retail_network else None
        }


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    supermarket_id = db.Column(db.BigInteger, db.ForeignKey('supermarket.id'), nullable=False)

    supermarket = db.relationship('Supermarket', back_populates='departments')

    panels = db.relationship('Panel', back_populates='department', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'supermarket_id': self.supermarket_id
        }