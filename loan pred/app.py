import streamlit as st 
import pandas as pd 
import pickle as pk 

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))
st.header('Loan APproval')

no_of_dep = st.text_input("Number of dependents in Family")
grad = st.selectbox("Choose Education",['Graduated','Not Graduated'])
self_emp = st.selectbox("Self Employed",['Yes','No'])
Annual_income =st.text_input("Enter annual Income")
Loan_amt =st.text_input("Enter Loan amount")
Loan_duration =st.selectbox("Enter Loan Duration" , ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
Assets =st.text_input("Enter your total asset value")
cibil = st.text_input("Enter Cibil Score")


#converting grad,self to numeric

if grad =="Not Graduated":
    grad_s=0
else:
    grad_s=1

if self_emp =="No":
    emp_s=0
else:
    emp_s=1

if  st.button("PRedict"):
    pred= pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_income,Loan_amt,Loan_duration,cibil,Assets]],
                   columns=['no_of_dependents', 'education', 'self_employed', 'income_annum',
       'loan_amount', 'loan_term', 'cibil_score', 'Assets'])
    pred=scaler.transform(pred)
    predict =model.predict(pred)
    if predict[0] ==1:
        st.markdown("Appproved")
    else:
        st.markdown("Rejected")
