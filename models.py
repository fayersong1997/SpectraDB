from exts import db
# from datetime import datetime
from sqlalchemy.schema import PrimaryKeyConstraint

class User(db.Model):
    __table_name__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # 自动无符号
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    # # 此处datetime.now相当于传过去一个函数，而不是datetime.now()调用这个函数的值
    # join_time = db.Column(db.DateTime, default=datetime.now)

class Sample(db.Model):
    sample_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sample_name = db.Column(db.String(50), nullable=False)
    sample_formula = db.Column(db.String(20))
    sample_preparation = db.Column(db.String(50))
    sample_notes = db.Column(db.String(100))

class Facility(db.Model):
    facility_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facility_fullname = db.Column(db.String(20), unique=True)
    facility_abbreviation = db.Column(db.String(10), nullable=False, unique=True)
    facility_laboratory = db.Column(db.String(50))
    facility_country = db.Column(db.String(20))
    facility_city = db.Column(db.String(20))

class Beamline(db.Model):
    beamline_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beamline_name = db.Column(db.String(50), nullable=False)

    facility_id = db.Column(db.Integer, db.ForeignKey('facility.facility_id'))
    facility = db.relationship('Facility', backref='beamlines')

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(50), nullable=False, unique=True)
    group_description = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship('User', backref='groups')

class DivideGroup(db.Model):
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)
    spectra_id = db.Column(db.Integer, db.ForeignKey('spectra.spectra_id'), primary_key=True)

    # 使用两个外键作为主键
    __table_args__ = (PrimaryKeyConstraint('group_id', 'spectra_id'),)

    # 此处不知是否恰当
    group = db.relationship('Group', backref='dividegroups')
    spectra = db.relationship('Spectra', backref='dividegroups')

class Spectra(db.Model):
    spectra_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    element = db.Column(db.String(10), nullable=False)
    edge = db.Column(db.String(10), nullable=False)
    measurement_mode = db.Column(db.String(30))
    rating = db.Column(db.String(20))
    file_path = db.Column(db.String(50), nullable=False, unique=True)

    sample_id = db.Column(db.Integer, db.ForeignKey('sample.sample_id'))
    sample = db.relationship('Sample', backref='spectras')
    beamline_id = db.Column(db.Integer, db.ForeignKey('beamline.beamline_id'))
    beamline = db.relationship('Beamline', backref='spectras')