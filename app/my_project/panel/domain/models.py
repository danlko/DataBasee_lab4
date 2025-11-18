from app.my_project import db

video_panel = db.Table('video_panel',
                       db.Column('panel_id', db.BigInteger, db.ForeignKey('panel.id'), primary_key=True),
                       db.Column('video_id', db.BigInteger, db.ForeignKey('video.id'), primary_key=True)
                       )


class PanelManufacturer(db.Model):
    __tablename__ = 'panel_manufacturer'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    panels = db.relationship('Panel', back_populates='manufacturer')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'country': self.country}


class PanelSpec(db.Model):
    __tablename__ = 'panel_spec'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    diagonal = db.Column(db.SmallInteger, nullable=False)
    resolution = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)

    panels = db.relationship('Panel', back_populates='spec')

    def to_dict(self):
        return {
            'id': self.id,
            'diagonal': self.diagonal,
            'resolution': self.resolution,
            'weight': self.weight,
            'power': self.power
        }


class Panel(db.Model):
    __tablename__ = 'panel'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    serial_number = db.Column(db.String(50), nullable=False, unique=True)
    model = db.Column(db.String(50), nullable=False)

    department_id = db.Column(db.BigInteger, db.ForeignKey('department.id'), nullable=False)
    manufacturer_id = db.Column(db.BigInteger, db.ForeignKey('panel_manufacturer.id'), nullable=False)
    spec_id = db.Column(db.BigInteger, db.ForeignKey('panel_spec.id'), nullable=False)

    department = db.relationship('Department', back_populates='panels')
    manufacturer = db.relationship('PanelManufacturer', back_populates='panels')
    spec = db.relationship('PanelSpec', back_populates='panels')

    videos = db.relationship('Video', secondary=video_panel, back_populates='panels')

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model,
            'department_id': self.department_id,
            'manufacturer_id': self.manufacturer_id,
            'spec_id': self.spec_id,
            'department_name': self.department.name if self.department else None,
            'manufacturer_name': self.manufacturer.name if self.manufacturer else None
        }