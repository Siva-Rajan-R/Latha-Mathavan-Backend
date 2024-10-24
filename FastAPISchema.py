from pydantic import BaseModel

class StudentDetails(BaseModel):
    student_register_number:str
    student_name:str|None=None
    student_attedence:str|None=None
    student_fee:str|None=None