from datetime import date
from SessionType import SessionType

class IRFile:
    sub_sessionID: int
    session_name: str
    import_date: date
    session_date: date
    track_name: str
    car_model: str
    session_type: SessionType
    # hz
    refresh_rate: int
    # in gb
    file_size: float
    file_path: str

    def __init__(self, 
                 sub_sessionID, session_name, 
                 import_date, session_date, 
                 track_name, car_model, 
                 session_type, refresh_rate, 
                 file_size, file_path):
        self.sub_sessionID = sub_sessionID
        self.session_name = session_name
        self.import_date = import_date
        self.session_date = session_date
        self.track_name = track_name
        self.car_model = car_model
        self.session_type = session_type
        self.refresh_rate = refresh_rate
        self.file_size = file_size
        self.file_path = file_path