from django.shortcuts import render,redirect
from .models import *
import pyttsx3
from datetime import date

def index(request):
    return render(request,"index.html")

def reg(request):
    msg=''
    fmsg=''
    if request.method=="POST":
        name=request.POST.get('name')
        fathername=request.POST.get('father_name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        dob=request.POST.get('birth_date')
        pincode=request.POST.get('pincode')
        Class=request.POST.get('Class')
        Password=request.POST.get('password')
        Email=request.POST.get('email')
        if name.isnumeric():
            msg=' incorrect name'
        if fathername.isnumeric():
            fmsg=' incorrect fathername'

        else:
            reg=Registrations(name=name,father_name=fathername,address=address,gender=gender,birth_date=dob,pincode=pincode,Class=Class,password=Password,email=Email)
            reg.save()
    return render(request,"reg.html",{'msg':msg,'msg':msg,'fmsg':fmsg})

def login(request):
    if request.method=="POST":
        name=request.POST.get("username")
        password=request.POST.get("password")
        rights=''
        cls=''
        email=''
        login=Registrations.objects.filter(name=name,password=password)
        teach=teacherreg.objects.filter(name=name,password=password)
        for j in teach:
            rights=j.rights
            cls=j.Class
            email=j.email
        for i in login:
            rights=i.rights
            ids=i.id
            email=i.email
        if rights=="user":
            request.session['id']=ids
            request.session['email']=email
            return redirect("/user/")
        elif rights=="teacher":
            request.session['email']=email
            request.session['Class']=cls
            return redirect("/teacher/")
        elif rights=="admin":
            return redirect("/principal/")

        else:
            engine=pyttsx3.init()
            msg="Invalid email or password"
            engine.say(msg)
            engine.runAndWait()

    return render(request,"login.html")

def user(request):
    return render(request,"user.html")


def teacher(request):
    return render(request,"teacher.html")

def admin(request):
    return render(request,"admin.html")


def teach(request):
    msg=''
    phmsg=''
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        dob=request.POST.get('birth_date')
        pincode=request.POST.get('pincode')
        Class=request.POST.get('Class')
        subject=request.POST.get('subject')
        phoneno=request.POST.get('phoneno')
        Password=request.POST.get('password')
        Email=request.POST.get('email')
        if name.isnumeric():
            msg='incorrect name'
        if not phoneno.isnumeric():
            phmsg='incorrect phoneno'
        else:
             teach=teacherreg(name=name,address=address,gender=gender,birth_date=dob,pincode=pincode,Class=Class,subject=subject,phoneno=phoneno,password=Password,email=Email)
             teach.save()
    return render(request,"teacherreg.html",{'msg':msg,'phmsg':phmsg})


def students(request):
    std=Registrations.objects.filter(rights='user')
    return render(request,"students.html",{'std':std})


def teachers(request):
    tchr=teacherreg.objects.filter(rights='teacher')
    return render(request,"teachers.html",{'tchr':tchr})


def mystudents(request):
    cls=request.session['Class']
    std=Registrations.objects.filter(Class=cls)
    return render(request,"mystudents.html",{'std':std})


def add_marks(request):
    cls=request.session['Class']
    std=Registrations.objects.filter(Class=cls)
    return render(request,"mark.html",{'std':std})


def mark_attendence(request):
    cls=request.session['Class']
    today = date.today()
    stds=[]


    att = Attendence.objects.filter(date=today)
    for i in att:
        student=i.student
        reg = Registrations.objects.filter(id=student)
        for j in reg:
            pass
            stds.append({'att':i,'std':j})
    std = Registrations.objects.filter(Class=cls)
    return render(request,"attendence.html",{'std':std,'att':att,'stds':stds})

def mark_present(request,id):
    att=Attendence(student=id,status='Present')
    att.save()
    return redirect('/mark_attendence/')

def mark_absent(request,id):
    att = Attendence(student=id, status='Absent')
    att.save()
    return redirect('/mark_attendence/')

def cancel_att(request,id):
    Attendence.objects.filter(id=id).delete()
    return redirect('/mark_attendence/')

def stdform(request,id):
    teacher = request.session['email']
    std=Registrations.objects.filter(id=id)
    for i in std:
        name=i.name
    if request.method == "POST":
        subject = request.POST.get('subject')
        mk = request.POST.get('mark')
        grade = request.POST.get('grade')
        ma = mark(teacher=teacher, student=id, subject=subject, mark=mk, grade=grade)
        ma.save()
    return render(request,"stdform.html",{'name':name})


def studentsmark(request):
    teacher = request.session['email']
    ma=mark.objects.filter(teacher=teacher)
    return render(request,"studentsmark.html",{'ma':ma})


def mymarks(request):
    student = request.session['id']
    ma=mark.objects.filter(student=student)
    marks=[]
    for  i in ma:
        std=i.student
        st=Registrations.objects.filter(id=std)
        for j in st:
            print(j)
            marks.append({'ma':i,'st':j})
    return render(request,"mymarks.html",{'marks':marks})

def stdattendance(request):
    student = request.session['id']
    ma=Attendence.objects.filter(student=student)
    return render(request,"stdattendance.html",{'ma':ma})


def form(request):
    email=request.session['email']
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        form=leave(teacher=email,name=name,email=email,phoneno=phoneno,date=date,reason=reason)
        form.save()

    return render(request,"form.html")



def studentleave(request):
    email=request.session['email']
    if request.method == "POST":

        name = request.POST.get('name')
        em = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        st=stdleave(user=email,name=name,email=em,phoneno=phoneno,date=date,reason=reason)
        st.save()

    return render(request,"studentleave.html")


def timetable1(request):
    tt=timetable.objects.filter()
    return render(request,"timetable.html",{'tt':tt})


def viewstdleave(request):
    stleave=stdleave.objects.filter()
    return render(request,"viewstudentleave.html",{'stleave':stleave})



def teacherleave(request):
    tchrleave=leave.objects.filter()
    return render(request,"viewteacherleave.html",{'tchrleave':tchrleave})

def app_tchr(request,id):
    leave.objects.filter(id=id).update(status='approved')
    return redirect('/teacherleave/')

def rej_tchr(request,id):
    leave.objects.filter(id=id).update(status='rejected')
    return redirect('/teacherleave/')

def app_std(request,id):
    stdleave.objects.filter(id=id).update(status='approved')
    return redirect('/viewstdleave/')

def rej_std(request,id):
    stdleave.objects.filter(id=id).update(status='rejected')
    return redirect('/viewstdleave/')



def timetab(request):
    if request.method == "POST":
        date = request.POST.get('date')
        trname = request.POST.get('teachername')
        subject = request.POST.get('subject')
        time = request.POST.get('time')
        tt = timetable(date=date, teachername=trname, subject=subject, time=time)
        tt.save()
    return render(request,"timetab.html")


def profile(request):
    email=request.session['email']
    prf=Registrations.objects.filter(email=email)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        Password = request.POST.get('password')
        Registrations.objects.filter(email=email).update(name=name,address=address,password=Password)
    return render(request,"profile.html",{'prf':prf})


def profile1(request):
    email=request.session['email']
    prf1=teacherreg.objects.filter(email=email)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        Password = request.POST.get('password')
        teacherreg.objects.filter(email=email).update(name=name,address=address,password=Password)
    return render(request,"profile1.html",{'prf1':prf1})


