from db import db


class RoomModel(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(40))
    location = db.Column(db.String(80))
    name = db.Column(db.String(40))
    description = db.Column(db.String(200))
    rateofescape = db.Column(db.String(20))
    image = db.Column(db.String(80))
    duration = db.Column(db.String(30))
    playedon = db.Column(db.String(80))

    def __init__(self, _id, company, location, name, description, rateofescape, image, duration, playedon):
        self.id = _id
        self.company = company
        self.location = location
        self.name = name
        self.description = description
        self.rateofescape = rateofescape
        self.image = image
        self.duration = duration
        self.playedon = playedon

    def json(self):
        return {
            'id': self.id,
            'Company': self.company,
            'Location': self.location,
            'Name': self.name,
            'Description': self.description,
            'Rate of Escape': self.rateofescape,
            'Image': self.image,
            'Duration': self.duration,
            'Played On': self.playedon
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name_company(cls, name, company):
        return cls.query.filter_by(name=name, company=company).first()

    @classmethod
    def get_all_rooms(cls):
        return {'rooms': [room.json() for room in cls.query.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
