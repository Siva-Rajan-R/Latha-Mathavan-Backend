from fastapi import FastAPI
from FastAPISchema import StudentDetails
from fastapi.responses import FileResponse
import pandas as pd
import pyrebase
app=FastAPI()
config={
    'apiKey': "AIzaSyCHSvIznxadoPnKL9OybZNbem3b5SZHRD4",
    'authDomain': "latha-mathavan.firebaseapp.com",
    'databaseURL': "https://latha-mathavan-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "latha-mathavan",
    'storageBucket': "latha-mathavan.appspot.com",
    'messagingSenderId': "104476232130",
    'appId': "1:104476232130:web:1a0d65ccfad0c9533a2e5b",
    'measurementId': "G-2FNTBB38MQ"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()

@app.post('/Add-Student')
def AddUser(student_details:StudentDetails):
    if db.child('latha_mathavan_student_details').child(student_details.student_register_number).get().val()==None:
        db.child('latha_mathavan_student_details').child(student_details.student_register_number).set({'register_number':student_details.student_register_number,'student_name':student_details.student_name,'student_attedence':student_details.student_attedence,'student_fee':student_details.student_fee})
        return {'detail':'Successfully Added','bool':1}
    return {'detail':'Student Already Exists','bool':0}
    
    

@app.put('/Update-Student')
def UpdateStudent(student_details:StudentDetails):
    if db.child('latha_mathavan_student_details').child(student_details.student_register_number).get().val()!=None:
        db.child('latha_mathavan_student_details').child(student_details.student_register_number).update({'student_attedence':student_details.student_attedence,'student_fee':student_details.student_fee})
        return {'detail':'Successfully Updated','bool':1}
    return {'detail':'Student Not Found','bool':0}

@app.delete('/Delete-Student')
def DeleteStudent(student_details:StudentDetails):
    if db.child('latha_mathavan_student_details').child(student_details.student_register_number).get().val()!=None:
        db.child('latha_mathavan_student_details').child(student_details.student_register_number).remove()
        return {'detail':'Successfully Deleted','bool':1}
    return {'detail':'Student Not Found','bool':0}

@app.get('/Get-Student')
def GetStudent():
    return {'detail':list(db.child('latha_mathavan_student_details').get().val().values())}

@app.get('/Get-Single-Student')
def GetSingleStudent(student_details:StudentDetails):
    detail=db.child('latha_mathavan_student_details').child(student_details.student_register_number).get().val()
    if detail!=None:
        return {'detail':{'student_name':detail['student_name'],'student_attedence':detail['student_attedence'],'student_fee':detail['student_fee']}}
    return {'detail':'No Student Found'}

@app.get('/Download-Student')
def DownloadStudent():
    data = {
        "Register Number": [],
        "Student Name": [],
        "Student Attedence": [],
        'Student Fee':[]
    }
    for i in list(db.child('latha_mathavan_student_details').get().val().values()):
        temp=['Register Number','Student Attedence','Student Fee','Student Name']
        for j in i:
            data[temp[0]].append(i[j])
            temp.pop(0)
    df = pd.DataFrame(data)
    df.to_excel('student.xlsx',index=False)
    return FileResponse('student.xlsx', media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="student.xlsx")