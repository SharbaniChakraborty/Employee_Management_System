import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title("Employee Management System")
choice = st.sidebar.selectbox("My Menu",("Home","Employee Login","Administration","Read about company"))
st.header(choice)
if(choice =="Home"):
    st.image("https://img.freepik.com/premium-vector/business-people-standing-together-as-team_3482-8672.jpg")
    st.header("WELCOME!")
    st.write("This is an application developed by Sharbani Chakraborty")
elif(choice == "Employee Login"):
    if 'login' not in st.session_state:
        st.session_state['login'] = False
    id = st.text_input("Enter Employee ID")
    dob = st.text_input("Enter Date Of Birth")
    btn = st.button("Login")
    if btn:
        mydb = mysql.connector.connect(host="localhost",user="root",password="*******",database="employee_management_sys")
        c = mydb.cursor()
        c.execute("select * from employee_detail")
        for r in c:
            if(r[0] == id and r[2] == dob):
                 st.session_state['login'] = True
                 break
        if(st.session_state['login'] == False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['login'] == True):
        st.subheader("Login Successful")
        choice2 = st.selectbox("Features",("None","View All Lessons","View All Leave Applications"))
        if(choice2 == "View All Lessons"):
            mydb = mysql.connector.connect(host="localhost",user="root",password="********",database="employee_management_sys")
            c = mydb.cursor()
            c.execute("select * from department")
            l=[]
            for r in c:
                l.append(r)
            df = pd.DataFrame(data=l,columns=['department_name','department_id'])
            st.dataframe(df)
        elif(choice2 =="View All Leave Applications"):
            employee_name = st.text_input("Enter the employee name")
            employee_dob = st.text_input("Enter the employee date of birth")
            btn2 = st.button("Apply!")
            if(btn2):
                doi = str(datetime.datetime.now())
                mydb = mysql.connector.connect(host="localhost",user="root",password="**********",database="employee_management_sys")
                c = mydb.cursor()
                c.execute("insert into apply_for_leave values(%s,%s,%s)",(doi, employee_name,employee_dob))
                mydb.commit()
                st.header("Successful Leave Application!!")
                
            
            
                
elif(choice == "Administration"):
    st.video("https://www.youtube.com/watch?v=o_XVt5rdpFY")
    if 'alogin' not in st.session_state:
        st.session_state['alogin'] = False
    id = st.text_input("Enter Administrator ID")
    dob = st.text_input("Enter Date Of Birth")
    btn = st.button("Login")
    if btn:
        mydb = mysql.connector.connect(host="localhost",user="root",password="*******",database="employee_management_sys")
        c = mydb.cursor()
        c.execute("select * from employee_detail")
        for r in c:
            if(r[0] == id and r[2] == dob):
                 st.session_state['alogin'] = True
                 break
        if(st.session_state['alogin'] == False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['alogin'] == True):
        st.subheader("Login Successful")
        choice2 = st.selectbox("Features",("None","View All Lessons","View All Leave Applications"))
        if(choice2 == "View All Lessons"):
            mydb = mysql.connector.connect(host="localhost",user="root",password="******",database="employee_management_sys")
            c = mydb.cursor()
            c.execute("select * from department")
            l=[]
            for r in c:
                l.append(r)
            df = pd.DataFrame(data=l,columns=['department_name','department_id'])
            st.dataframe(df)
        elif(choice2 =="View All Leave Applications"):
            employee_name = st.text_input("Enter the employee name")
            employee_dob = st.text_input("Enter the employee date of birth")
            btn2 = st.button("Apply!")
            if(btn2):
                doi = str(datetime.datetime.now())
                mydb = mysql.connector.connect(host="localhost",user="root",password="********",database="employee_management_sys")
                c = mydb.cursor()
                c.execute("insert into apply_for_leave values(%s,%s,%s)",(doi, employee_name,employee_dob))
                mydb.commit()
                st.header("Successful Leave Application!!")

elif(choice == "Read about company"):
    st.title("Python")
    st.markdown('<iframe src="https://static.realpython.com/python-basics-sample-chapters.pdf" width = "100%" height = "400px"></iframe',unsafe_allow_html = True)
    st.title("WordPress")
    st.markdown('<iframe src="https://greenteapress.com/thinkpython2/thinkpython2.pdf" width = "100%" height = "400px"></iframe',unsafe_allow_html = True)