#import tkinter as Tk
from tkinter import*
#root=Tk()


from telco_ml_2 import*
def Exploratory_Data_Analysis(*args):
    window2=Tk()
    window2.geometry('1500x1000')
    window2.minsize(500,400)
    window2.maxsize(1250,800)



    b1 = Button(window2, text='Relation_of_all_column_with_churn',height=2,width=30,command=lambda :relation_of_all_column_with_churn_column(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b1.grid(row=1,column=0,padx=100,pady=20,sticky='w')


    b11 = Button(window2, text='Relation_of_all_column_with_churn',height=2,width=30,command=lambda :relation_of_all_column_with_churn_column(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b11.grid(row=1,column=0,padx=700,pady=20,sticky='w')




    b2 = Button(window2, text='Gender_Distribution',height=2,width=30,command=lambda :Gender_Distribution(), bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b2.grid(row=2,column=0,padx=100,pady=20,sticky='w')


    b3 = Button(window2, text='Senior_Citizens',height=2,width=30,command=lambda :Senior_Citizens(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b3.grid(row=2,column=0,padx=700,pady=20,sticky='w')



    b4 = Button(window2, text='Partner_and_dependent_status',height=2,width=30,command=lambda :Partner_and_dependent_status(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b4.grid(row=4,column=0,padx=100,pady=20,sticky='w')


    b5 = Button(window2, text='Customer_Account_Information_Tenure',height=2,width=30,command=lambda :Customer_Account_Information_Tenure(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b5.grid(row=4,column=0,padx=700,pady=20,sticky='w')


    b6 = Button(window2, text='Customer_Account_Information_Cotracts',height=2,width=30,command=lambda :Customer_Account_Information_Cotracts(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b6.grid(row=6,column=0,padx=100,pady=20,sticky='w')




    b7 = Button(window2, text='Customer_VS_Services',height=2,width=30,command=lambda :Customer_VS_Services(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b7.grid(row=6,column=0,padx=700,pady=20,sticky='w')


    b8 = Button(window2, text='MonthlyCharges_VS_TotalCharges',height=2,width=30,command=lambda :MonthlyCharges_VS_TotalCharges(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b8.grid(row=7,column=0,padx=100,pady=20,sticky='w')


    b9 = Button(window2, text='Exit',height=2,width=30,command=window2.quit,bg='coral',font="comicsansms 20 bold",activebackground='red') 
    b9.grid(row=7,column=0,padx=700,pady=20,sticky='w')




def Churn_Rate_Relations(*args):
    window2=Tk()
    window2.geometry('1500x1000')
    window2.minsize(500,400)
    window2.maxsize(1250,800)



    b1 = Button(window2, text='Churn_Rate_in_dataset',height=2,width=30,command=lambda :Churn_Rate_in_dataset(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b1.grid(row=1,column=0,padx=100,pady=20,sticky='w')

    b2 = Button(window2, text='Churn_by_Tenure',height=2,width=30,command=lambda :Churn_by_Tenure(), bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b2.grid(row=1,column=0,padx=700,pady=20,sticky='w')


    b3 = Button(window2, text='Churn_by_Contract_Type',height=2,width=30,command=lambda :Churn_by_Contract_Type(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b3.grid(row=2,column=0,padx=100,pady=20,sticky='w')

    '''

    b4 = Button(window2, text='Churn_by_Seniority',height=2,width=30,command=lambda :Churn_by_Seniority(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b4.grid(row=2,column=0,padx=700,pady=20,sticky='w')


    b5 = Button(window2, text='Churn_by_Monthly_Charges',height=2,width=30,command=lambda :Churn_by_Monthly_Charges(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b5.grid(row=3,column=0,padx=100,pady=20,sticky='w')


    b6 = Button(window2, text='Churn_by_Total_Charges',height=2,width=30,command=lambda :Churn_by_Total_Charges(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b6.grid(row=3,column=0,padx=700,pady=20,sticky='w')

    

    b7 = Button(window2, text='Exit',height=2,width=20,command=window2.quit,bg='coral',font="comicsansms 20 bold",activebackground='red') 
    b7.grid(row=8,column=0,padx=550,pady=20,sticky='w')

    '''




    b4 = Button(window2, text='Churn_by_Seniority',height=2,width=30,command=lambda :Churn_by_Contract_Type(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b4.grid(row=2,column=0,padx=700,pady=20,sticky='w')


    b5 = Button(window2, text='Churn_by_Monthly_Charges',height=2,width=30,command=lambda :Churn_by_Contract_Type(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b5.grid(row=3,column=0,padx=100,pady=20,sticky='w')


    b6 = Button(window2, text='Churn_by_Total_Charges',height=2,width=30,command=lambda :Churn_by_Contract_Type(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b6.grid(row=3,column=0,padx=700,pady=20,sticky='w')

    

    b7 = Button(window2, text='Exit',height=2,width=20,command=window2.quit,bg='coral',font="comicsansms 20 bold",activebackground='red') 
    b7.grid(row=8,column=0,padx=550,pady=20,sticky='w')
def ML_Based_Prediction(*args):
    

    window2=Tk()
    window2.geometry('1500x1000')
    window2.minsize(500,400)
    window2.maxsize(1250,800)



    b1 = Button(window2, text='Logistic Regression',height=2,width=30,command=lambda :Logistic_Regression(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b1.grid(row=1,column=0,padx=350,pady=20,sticky='w')

    b2 = Button(window2, text='Random Forest Classifier',height=2,width=30,command=lambda :RandomForestClassifier(), bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b2.grid(row=4,column=0,padx=350,pady=20,sticky='w')


    b3 = Button(window2, text='Support Vecor Machine SVM',height=2,width=30,command=lambda :Support_Vecor_Machine_SVM(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b3.grid(row=5,column=0,padx=350,pady=20,sticky='w')

    b4 = Button(window2, text='ADA Boost',height=2,width=30,command=lambda :ADA_Boost(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b4.grid(row=6,column=0,padx=350,pady=20,sticky='w')


    b5 = Button(window2, text='XG Boost',height=2,width=30,command=lambda :XG_Boost(),bg='deep sky blue',font="comicsansms 20 bold",activebackground='green2') 
    b5.grid(row=7,column=0,padx=350,pady=20,sticky='w')

    
    b6 = Button(window2, text='Exit',height=2,width=30,command=window2.quit,font="comicsansms 20 bold",activebackground='red') 
    b6.grid(row=8,column=0)
def homepage():
    

    window=Tk()
    window.geometry('1400x1500')
    window.minsize(500,400)
    window.maxsize(1250,800)

    l1=Label(window,text='Let\'s Play with Telco Data :TechTrioZ',bg='cyan',font="comicsansms 30 bold",borderwidth=3, relief="solid")
    l1.grid(row=0,column=0,columnspan=15,padx=100,pady=50)




    b1 = Button(window, text='Churn Rate Relations',height=1,width=30,bg='Royalblue1',command =lambda :Churn_Rate_Relations(window),font="comicsansms 20 bold",activebackground='green2') 
    b1.grid(row=2,column=2,padx=350,pady=15)
    b1.bind('<Button-1>,<Return>')
    #b1.bind('<Return>')


    b2 = Button(window, text='ML based predictive models ',height=1,width=30,bg='Royalblue1',command=lambda :ML_Based_Prediction(window),font="comicsansms 20 bold",activebackground='green2') 
    b2.grid(row=3,column=2,pady=15)

    b0 = Button(window, text='Exploratory Data Analysis',height=1,width=30,bg='Royalblue1',command=lambda :Exploratory_Data_Analysis(window),font="comicsansms 20 bold",activebackground='green2') 
    b0.grid(row=1,column=2,pady=15)


    b3 = Button(window, text='Exit',height=1,width=10,bg='coral',command=window.quit,font="comicsansms 20 bold",activebackground='red') 
    b3.grid(row=4,column=2,padx=400,pady=15)


    window.mainloop()




def main():
    homepage()


if __name__ == "__main__":
    main()    