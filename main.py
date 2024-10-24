from fastapi import FastAPI
from FastAPISchema import StudentDetails
app=FastAPI()
lis=[]

@app.post('/Add-Student')
def AddUser(student_details:StudentDetails):
    flag=False
    for i in lis:
        print(i['register_number']==student_details.student_register_number)
        if i['register_number']==student_details.student_register_number:
            flag=True
    if flag==False:
        lis.append({'register_number':student_details.student_register_number,'student_name':student_details.student_name,'student_attedence':student_details.student_attedence,'student_fee':student_details.student_fee})
        return {'detail':'Successfully Added','bool':1}
    return {'detail':'Student Already Exists','bool':0}
    
    

@app.put('/Update-Student')
def UpdateStudent(student_details:StudentDetails):
    for i in lis:
        if i['register_number']==student_details.student_register_number:
            i['student_attedence']=student_details.student_attedence
            i['student_fee']=student_details.student_fee
            return {'detail':'Successfully Updated','bool':1}
    return {'detail':'Student Not Found','bool':0}

@app.delete('/Delete-Student')
def DeleteStudent(student_details:StudentDetails):
    for j,i in enumerate(lis):
        if i['register_number']==student_details.student_register_number:
            lis.pop(j)
            return {'detail':'Successfully Deleted','bool':1}
    return {'detail':'Student Not Found','bool':0}

@app.get('/Get-Student')
def GetStudent():
    return {'detail':lis}

@app.get('/Get-Single-Student')
def GetSingleStudent(student_details:StudentDetails):
    print(lis)
    for i in lis:
        if i['register_number']==student_details.student_register_number:
            return {'detail':i}
    return {'detail':'No Student Found'}