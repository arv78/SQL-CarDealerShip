from tkinter import *
import tkinter.messagebox
import random
import pyodbc
import time
import datetime
conn = pyodbc.connect('Driver={SQL Server};'
                                          'Server=ARYA\ARYA;'
                                          'Database=Car_Dealership;'
                                          'Trusted_Connection=yes;')

cursor = conn.cursor()

                
class application:
    def __init__(self):
        self.window = Tk()
        # for putting window in middle of the screen
        window_height = 300
        window_width = 435
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.title("Car dealership")
        frame1 = Frame(self.window)
        frame2 = Frame(self.window)
        frame1.pack(fill=BOTH)
        frame2.pack(fill=BOTH)

        label1 = Label(frame1,text = "Car Dealership",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        msg_init = Message(frame2,text = "Welcome, to our car dealership application,"+\
                           " if you have an account you can Sign in or if you don't, just"+\
                           " Sign up!",fg = "red",font = "Helvetica 12 italic ").pack(fill = BOTH)
        bt_signup = Button(self.window,text = "Sign up",command = self.signup,fg = "blue"\
                           ,font = "Times 12 bold").place(x=183,y=180)
        bt_signin = Button(self.window,text = "Sign in",command = self.signin,fg = "blue"\
                           ,font = "Times 12 bold").place(x=185,y=230)
        
    def signup_insert(self,v1,v2,v3,v4): #inserting new customer to table
        cursor.execute("insert into customer(Ssn,fname,lname,phone) values (?,?,?,?);",v1,v2,v3,v4)
        cursor.commit()
    def check_signin(self,ssn): #checking customer_id is in table
        cursor.execute("select distinct hasAttachments = CASE WHEN EXISTS(select * from customer where Ssn = (?) ) then 1 else 0 end from customer C",ssn)
        for row in cursor:
            tmp=row
        tmp=str(tmp)
        result=int(tmp[1])
        return result

    def select_new(self,model,company,year,color,Ssn):
        cursor.execute("select vehicle_id from new_cars where model=(?) and company=(?) and year=(?) and color=(?)",model,company,year,color)
        for row in cursor:
           v_id=str(row)
        v_id = v_id.replace("(", "")
        v_id = v_id.replace(",", "")
        v_id = v_id.replace(")", "")
        v_id=int(v_id)
        cursor.execute("select price from new_cars where model=(?) and company=(?) and year=(?) and color=(?)",model,company,year,color) 
        for row in cursor:
           price=str(row)
        price = price.replace("(", "")
        price = price.replace(",", "")
        price = price.replace(")", "")
        price=(int(price)*110)//100
        cursor.execute("select fname from salesperson where Ssn=(?)",Ssn) 
        for row in cursor:
           fname=str(row)
        fname = fname.replace("(", "")
        fname = fname.replace(",", "")
        fname = fname.replace(")", "")
        fname= fname
        cursor.execute("select lname from salesperson where Ssn=(?)",Ssn) 
        for row in cursor:
           lname=str(row)
        lname = lname.replace("(", "")
        lname = lname.replace(",", "")
        lname = lname.replace(")", "")
        lname = lname
        cursor.execute("select guarantee_duration from guarantee where model=(?) and company=(?) and year=(?)",model,company,year) 
        for row in cursor:
           guarantee_duration=str(row)
        guarantee_duration = guarantee_duration.replace("(", "")
        guarantee_duration = guarantee_duration.replace(",", "")
        guarantee_duration = guarantee_duration.replace(")", "")
        guarantee_duration = int(guarantee_duration)
        return v_id,price,fname,lname,guarantee_duration
        
        
    def insert_new(self,v_ID,c_ID,s_ID,saleprice,saledate): 
       cursor.execute("insert into new_cars_deals(vehicle_id,customer_id,salesperson_id,sale_price,deal_date) values(?,?,?,?,?);",v_ID,c_ID,s_ID,saleprice,saledate)
       cursor.commit()

    
    def select_rent(self,model,company,year):
        cursor.execute("select vehicle_id from rental_cars where model=(?) and company=(?) and year=(?)",model,company,year)
        for row in cursor:
           v_id=str(row)
        v_id = v_id.replace("(", "")
        v_id = v_id.replace(",", "")
        v_id = v_id.replace(")", "")
        v_id=int(v_id)
        cursor.execute("select daily_rate from rental_cars where model=(?) and company=(?) and year=(?)",model,company,year)
        for row in cursor:
           d_rate=str(row)
        d_rate = d_rate.replace("(", "")
        d_rate = d_rate.replace(",", "")
        d_rate =  d_rate.replace(")", "")
        d_rate = int(d_rate)
        return v_id,d_rate

    def insert_rent(self,v_ID_2,c_ID_2,s_date,e_date):
        cursor.execute("insert into rents(vehicle_id,customer_id,start_date,end_date) values(?,?,?,?);",v_ID_2,c_ID_2,s_date,e_date)
        cursor.commit()
        

    def select_used(self,model,company,year,color,Ssn):
        cursor.execute("select vehicle_id from used_cars where model=(?) and company=(?) and year=(?) and color=(?)",model,company,year,color)
        for row in cursor:
           v_id = str(row)
        v_id = v_id.replace("(", "")
        v_id = v_id.replace(",", "")
        v_id = v_id.replace(")", "")
        v_id_2=int(v_id)
        cursor.execute("select seller_id from used_cars where model=(?) and company=(?) and year=(?) and color=(?)",model,company,year,color)
        for row in cursor:
            o_id=str(row)
        o_id = o_id.replace("(", "")
        o_id = o_id.replace(",", "")
        o_id = o_id.replace(")", "")
        o_id=int(o_id)
        cursor.execute("select fname from customer where Ssn=(?)",o_id)
        for row in cursor:
            fname=str(row)
        fname = fname.replace("(", "")
        fname = fname.replace(",", "")
        fname = fname.replace(")", "")
        fname= fname
        cursor.execute("select lname from customer where Ssn=(?)",o_id)
        for row in cursor:
            lname=str(row)
        lname = lname.replace("(", "")
        lname = lname.replace(",", "")
        lname = lname.replace(")", "")
        lname= lname
        cursor.execute("select price from used_cars where model=(?) and company=(?) and year=(?) and color=(?)",model,company,year,color) 
        for row in cursor:
            price=str(row)
        price = price.replace("(", "")
        price = price.replace(",", "")
        price = price.replace(")", "")
        price=(int(price)*110)//100
        cursor.execute("select fname from salesperson where Ssn=(?)",Ssn) 
        for row in cursor:
           fname_sp=str(row)
        fname_sp = fname_sp.replace("(", "")
        fname_sp = fname_sp.replace(",", "")
        fname_sp = fname_sp.replace(")", "")
        fname_sp= fname_sp
        cursor.execute("select lname from salesperson where Ssn=(?)",Ssn) 
        for row in cursor:
           lname_sp=str(row)
        lname_sp = lname_sp.replace("(", "")
        lname_sp = lname_sp.replace(",", "")
        lname_sp = lname_sp.replace(")", "")
        lname_sp = lname_sp
        
        return v_id_2,o_id,fname,lname,price,fname_sp,lname_sp
    
    def insert_used(self,v_ID,o_ID,c_ID,s_ID,saleprice,saledate):
        cursor.execute("insert into used_cars_deals(vehicle_id,owner_id,customer_id,salesperson_id,sale_price,deal_date) values(?,?,?,?,?,?);",v_ID,o_ID,c_ID,s_ID,saleprice,saledate)
        cursor.commit()


        
    def signup(self):
        self.flag=1
        self.window.destroy()
        self.window_signup = Tk()
        
        window_signup_height = 330
        window_signup_width = 435
        screen_width = self.window_signup.winfo_screenwidth()
        screen_height = self.window_signup.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_signup_width/2))
        y_cordinate = int((screen_height/2) - (window_signup_height/2))
        self.window_signup.geometry("{}x{}+{}+{}".format(window_signup_width, window_signup_height, x_cordinate, y_cordinate))

        self.window_signup.title("Sign up")
        frame1 = Frame(self.window_signup)
        frame1.pack(fill=BOTH)
        #variables
        self.var_Ssn = IntVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_phone = IntVar()
        
        label1 = Label(frame1,text = "Sign up form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        lb_Ssn = Label(self.window_signup,text = "Ssn",fg = "blue",font = "Times 13 bold").place(x=140,y=70)
        ent_Ssn = Entry(self.window_signup,textvariable = self.var_Ssn).place(x=205,y=70)
        lb_fname = Label(self.window_signup,text = "Fname",fg = "blue",font = "Times 13 bold").place(x=140,y=110)
        ent_fname = Entry(self.window_signup,textvariable = self.var_fname).place(x=205,y=110)
        lb_lname = Label(self.window_signup,text = "Lname",fg = "blue",font = "Times 13 bold").place(x=140,y=150)
        ent_lname = Entry(self.window_signup,textvariable = self.var_lname).place(x=205,y=150)
        lb_phone = Label(self.window_signup,text = "Phone",fg = "blue",font = "Times 13 bold").place(x=140,y=190)
        ent_phone = Entry(self.window_signup,textvariable = self.var_phone).place(x=205,y=190)

        bt_confirm = Button(self.window_signup,text = "Confirm",command = self.second_page,bg = "light blue",font = "Times 12 bold").place(x=190,y=240)
                
    def signin(self):
        self.flag = 0
        self.window.destroy()
        self.window_signin = Tk()
        
        window_signin_height = 200
        window_signin_width = 435
        screen_width = self.window_signin.winfo_screenwidth()
        screen_height = self.window_signin.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_signin_width/2))
        y_cordinate = int((screen_height/2) - (window_signin_height/2))
        self.window_signin.geometry("{}x{}+{}+{}".format(window_signin_width, window_signin_height, x_cordinate, y_cordinate))

        self.window_signin.title("Sign in")
        frame1 = Frame(self.window_signin)
        frame1.pack(fill=BOTH)
        #variables
        self.var_Ssn = IntVar()

        label1 = Label(frame1,text = "Sign in form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        lb_Ssn = Label(self.window_signin,text = "Ssn",fg = "blue",font = "Times 13 bold").place(x=140,y=70)
        ent_Ssn = Entry(self.window_signin,textvariable = self.var_Ssn).place(x=205,y=70)
   
        bt_login = Button(self.window_signin,text = "Log in",command = self.check_login,bg = "light blue",font = "Times 12 bold").place(x=190,y=110)
    
    def check_login(self):
        res=self.check_signin(self.var_Ssn.get()) 
        if res==1 :
            self.second_page()
        else:
            tkinter.messagebox.showinfo("unseccessfull","Not found!")
        # if self.var_get_Ssnexist in customer.dbo = sign in -> self.second_page()
        # else -> tkinter.messagebox -> sorry you don't have an account -> self.window_signin.destroy() -> self.signup()
        
    def second_page(self):
        if self.flag ==1:
             self.signup_insert(self.var_Ssn.get(),self.var_fname.get(),self.var_lname.get(),self.var_phone.get())
             self.window_signup.destroy()
        elif self.flag ==0:
             self.window_signin.destroy()
        self.window_sp = Tk()
        
        window_sp_height = 285
        window_sp_width = 435
        screen_width = self.window_sp.winfo_screenwidth()
        screen_height = self.window_sp.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_sp_width/2))
        y_cordinate = int((screen_height/2) - (window_sp_height/2))
        self.window_sp.geometry("{}x{}+{}+{}".format(window_sp_width, window_sp_height, x_cordinate, y_cordinate))

        self.window_sp.title("second page")
        frame1 = Frame(self.window_sp)
        frame1.pack(fill=BOTH)
        #variables
        self.var_get_Ssn = IntVar()

        label1 = Label(frame1,text = "Car Dealsership",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        bt_reg = Button(self.window_sp,text = "Register a car",command = self.reg,fg = "Blue",font = "Times 12 bold").place(x=160,y=60)
        bt_rent = Button(self.window_sp,text = "Rent a car",command = self.rent,fg = "Blue",font = "Times 12 bold").place(x=160,y=110)
        bt_used = Button(self.window_sp,text = "buy a used car",command = self.used,fg = "Blue",font = "Times 12 bold").place(x=160,y=160)
        bt_comp = Button(self.window_sp,text = "Work with us",command = self.comp,bg = "light blue",font = "Helvetica 12").place(x=330,y=250)

    def reg(self):
        self.window_sp.destroy()
        self.window_reg = Tk()
        
        window_reg_height = 350
        window_reg_width = 435
        screen_width = self.window_reg.winfo_screenwidth()
        screen_height = self.window_reg.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_reg_width/2))
        y_cordinate = int((screen_height/2) - (window_reg_height/2))
        self.window_reg.geometry("{}x{}+{}+{}".format(window_reg_width, window_reg_height, x_cordinate, y_cordinate))

        self.window_reg.title("register")
        frame1 = Frame(self.window_reg)
        frame1.pack(fill=BOTH)
        #variables
        self.var_model = StringVar()
        self.var_company = StringVar()
        self.var_year = IntVar()
        self.var_color = StringVar()
        # these three combine together to form the date at the 'confirm def'
        self.var_year_1 = IntVar()
        self.var_month_1 = IntVar()
        self.var_day_1 = IntVar()

        label1 = Label(frame1,text = "Regestring form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        
        lb_model = Label(self.window_reg,text = "Model",fg = "blue",font = "Times 13 bold").place(x=140,y=70)
        ent_model = Entry(self.window_reg,textvariable = self.var_model).place(x=205,y=70)
        lb_company = Label(self.window_reg,text = "Company",fg = "blue",font = "Times 13 bold").place(x=120,y=110)
        ent_company = Entry(self.window_reg,textvariable = self.var_company).place(x=205,y=110)
        lb_year = Label(self.window_reg,text = "model_year",fg = "blue",font = "Times 13 bold").place(x=105,y=150)
        ent_year = Entry(self.window_reg,textvariable = self.var_year).place(x=205,y=150)
        lb_color = Label(self.window_reg,text = "color",fg = "blue",font = "Times 13 bold").place(x=150,y=190)
        ent_color = Entry(self.window_reg,textvariable = self.var_color).place(x=205,y=190)
        
        lb_year_1 = Label(self.window_reg,text = "year",fg = "blue",font = "Times 11 bold").place(x=80,y=230)
        ent_year_1 = Entry(self.window_reg,textvariable = self.var_year_1,width = 8).place(x=120,y=230)
        lb_month_1 = Label(self.window_reg,text = "month",fg = "blue",font = "Times 11 bold").place(x=180,y=230)
        ent_month_1 = Entry(self.window_reg,textvariable = self.var_month_1,width = 8).place(x=230,y=230)
        lb_day_1 = Label(self.window_reg,text = "day",fg = "blue",font = "Times 11 bold").place(x=300,y=230)
        ent_day_1 = Entry(self.window_reg,textvariable = self.var_day_1,width = 8).place(x=330,y=230)
        
        #choosing from our salesperson people
        self.salesperson_p = [7007,7712,7726,7807,7808,7810,7813,7820,7822,7823]
        self.random_sp = random.randint(0,9)
        # salesperson_p[random_sp]
        bt_conf = Button(self.window_reg,text= "Confirm",command=self.confirm,bg = "light blue",font = "Times 12 bold").place(x=190,y=280)
        #self.reg_insert(self.var_model.get(),self.var_company.get(),self.var_year.get(),self.var_color.get(),self.var_Ssn,salesperson_p[random_sp],self.Date.get())
        

    def confirm(self):
        d = datetime.datetime(self.var_year_1.get(), self.var_month_1.get(), self.var_day_1.get()) #formatting saledate 
        saledate= d.date().isoformat()
        self.vehicle_id, self.saleprice, self.sp_fname, self.sp_lname, self.guarantee_duration_sale=  self.select_new (self.var_model.get() , self.var_company.get() , self.var_year.get() ,  self.var_color.get() , self.salesperson_p[self.random_sp]) #getting vehicleId and Saleprice from sql
        msg_box = tkinter.messagebox.askyesno("Validate","Price: "+str(self.saleprice)+"\nVehicle_id: "+str(self.vehicle_id)+"\nSalesperson: "+self.sp_fname+" "+self.sp_lname+"\nGuarantee: "+str(self.guarantee_duration_sale)) #informing user
        if msg_box == True : #validation
            self.insert_new(self.vehicle_id,self.var_Ssn.get() ,self.salesperson_p[self.random_sp] ,self.saleprice ,saledate) #inserting to new_cars_deal
            self.window_reg.destroy()
            msg_box_2 = tkinter.messagebox.showinfo("Successful","Your registraition has completed!")
                
    def rent(self):
        self.window_sp.destroy()
        self.window_rent = Tk()
        
        window_rent_height = 450
        window_rent_width = 435
        screen_width = self.window_rent.winfo_screenwidth()
        screen_height = self.window_rent.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_rent_width/2))
        y_cordinate = int((screen_height/2) - (window_rent_height/2))
        self.window_rent.geometry("{}x{}+{}+{}".format(window_rent_width, window_rent_height, x_cordinate, y_cordinate))

        self.window_rent.title("renting")
        frame1 = Frame(self.window_rent)
        frame1.pack(fill=BOTH)
        #variables
        self.var_model_rent = StringVar()
        self.var_company_rent = StringVar()
        self.var_year_rent = IntVar()
        self.var_color_rent = StringVar()
        self.var_year_s = IntVar()
        self.var_month_s = IntVar()
        self.var_day_s = IntVar()
        self.var_year_e = IntVar()
        self.var_month_e = IntVar()
        self.var_day_e = IntVar()
        
        label1 = Label(frame1,text = "Rental form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        
        lb_model = Label(self.window_rent,text = "Model",fg = "blue",font = "Times 13 bold").place(x=140,y=70)
        ent_model = Entry(self.window_rent,textvariable = self.var_model_rent).place(x=205,y=70)
        lb_company = Label(self.window_rent,text = "Company",fg = "blue",font = "Times 13 bold").place(x=120,y=110)
        ent_company = Entry(self.window_rent,textvariable = self.var_company_rent).place(x=205,y=110)
        lb_year = Label(self.window_rent,text = "model_year",fg = "blue",font = "Times 13 bold").place(x=105,y=150)
        ent_year = Entry(self.window_rent,textvariable = self.var_year_rent).place(x=205,y=150)
        lb_color = Label(self.window_rent,text = "color",fg = "blue",font = "Times 13 bold").place(x=150,y=190)
        ent_color = Entry(self.window_rent,textvariable = self.var_color_rent).place(x=205,y=190)
        # start_date
        lb_start = Label(self.window_rent,text = "Start Date: ",font = "Times 13 bold").place(x=40,y=220)
        lb_year_s = Label(self.window_rent,text = "year",fg = "blue",font = "Times 11 bold").place(x=90,y=260)
        ent_year_s = Entry(self.window_rent,textvariable = self.var_year_s,width = 8).place(x=130,y=260)
        lb_month_s = Label(self.window_rent,text = "month",fg = "blue",font = "Times 11 bold").place(x=190,y=260)
        ent_month_s = Entry(self.window_rent,textvariable = self.var_month_s,width = 8).place(x=240,y=260)
        lb_day_s = Label(self.window_rent,text = "day",fg = "blue",font = "Times 11 bold").place(x=310,y=260)
        ent_day_s = Entry(self.window_rent,textvariable = self.var_day_s,width = 8).place(x=340,y=260)
        #end_date
        lb_start = Label(self.window_rent,text = "End Date: ",font = "Times 13 bold").place(x=40,y=300)
        lb_year_e = Label(self.window_rent,text = "year",fg = "blue",font = "Times 11 bold").place(x=90,y=340)
        ent_year_e = Entry(self.window_rent,textvariable = self.var_year_e,width = 8).place(x=130,y=340)
        lb_month_e = Label(self.window_rent,text = "month",fg = "blue",font = "Times 11 bold").place(x=190,y=340)
        ent_month_e = Entry(self.window_rent,textvariable = self.var_month_e,width = 8).place(x=240,y=340)
        lb_day_e = Label(self.window_rent,text = "day",fg = "blue",font = "Times 11 bold").place(x=310,y=340)
        ent_day_e = Entry(self.window_rent,textvariable = self.var_day_e,width = 8).place(x=340,y=340)

        bt_conf = Button(self.window_rent,text= "Confirm",command=self.confirm_rent,bg = "light blue",font = "Times 12 bold").place(x=190,y=390)

    def confirm_rent(self):
        
        #combination_start_end
        
        d1= datetime.datetime(self.var_year_s.get(), self.var_month_s.get(), self.var_day_s.get())
        start_date= d1.date().isoformat()

        d2= datetime.datetime(self.var_year_e.get(), self.var_month_e.get(), self.var_day_e.get())
        end_date= d2.date().isoformat()

        self.vehicle_id_2,self.d_rate = self.select_rent(self.var_model_rent.get(),self.var_company_rent.get(),self.var_year_rent.get())
        
        msg_box = tkinter.messagebox.askyesno("Validate","Daily_rate: "+str(self.d_rate)+"\nVehicle_id: "+str(self.vehicle_id_2))
        if msg_box == True:
            self.insert_rent(self.vehicle_id_2,self.var_Ssn.get(),start_date,end_date)
            self.window_rent.destroy()
            msg_box_2 = tkinter.messagebox.showinfo("Successful","Your rental process has completed!")
            
    def used(self):
        self.window_sp.destroy()
        self.window_used = Tk()
        
        window_used_height = 400
        window_used_width = 435
        screen_width = self.window_used.winfo_screenwidth()
        screen_height = self.window_used.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_used_width/2))
        y_cordinate = int((screen_height/2) - (window_used_height/2))
        self.window_used.geometry("{}x{}+{}+{}".format(window_used_width, window_used_height, x_cordinate, y_cordinate))

        self.window_used.title("used cars")
        frame1 = Frame(self.window_used)
        frame1.pack(fill=BOTH)
        #variables
        self.var_model_used = StringVar()
        self.var_company_used = StringVar()
        self.var_year_real_used = IntVar()
        self.var_color_used = StringVar()
        self.var_kilometer_used = IntVar()
        self.var_year_used = IntVar()
        self.var_month_used = IntVar()
        self.var_day_used = IntVar()
        
        label1 = Label(frame1,text = "Used cars' form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)

        lb_model = Label(self.window_used,text = "Model",fg = "blue",font = "Times 13 bold").place(x=140,y=70)
        ent_model = Entry(self.window_used,textvariable = self.var_model_used).place(x=205,y=70)
        lb_company = Label(self.window_used,text = "Company",fg = "blue",font = "Times 13 bold").place(x=120,y=110)
        ent_company = Entry(self.window_used,textvariable = self.var_company_used).place(x=205,y=110)
        lb_year = Label(self.window_used,text = "model_year",fg = "blue",font = "Times 13 bold").place(x=105,y=150)
        ent_year = Entry(self.window_used,textvariable = self.var_year_real_used).place(x=205,y=150)
        lb_color = Label(self.window_used,text = "color",fg = "blue",font = "Times 13 bold").place(x=150,y=190)
        ent_color = Entry(self.window_used,textvariable = self.var_color_used).place(x=205,y=190)
        lb_kilometer = Label(self.window_used,text = "Kilometer",fg = "blue",font = "Times 13 bold").place(x=110,y=230)
        ent_kilometer = Entry(self.window_used,textvariable = self.var_kilometer_used).place(x=205,y=230)
        # deal_date
        lb_year_used = Label(self.window_used,text = "year",fg = "blue",font = "Times 11 bold").place(x=80,y=280)
        ent_year_used = Entry(self.window_used,textvariable = self.var_year_used,width = 8).place(x=120,y=280)
        lb_month_used = Label(self.window_used,text = "month",fg = "blue",font = "Times 11 bold").place(x=180,y=280)
        ent_month_used = Entry(self.window_used,textvariable = self.var_month_used,width = 8).place(x=230,y=280)
        lb_day_used = Label(self.window_used,text = "day",fg = "blue",font = "Times 11 bold").place(x=300,y=280)
        ent_day_used = Entry(self.window_used,textvariable = self.var_day_used,width = 8).place(x=330,y=280)

        bt_conf_used = Button(self.window_used,text = "Confirm",command=self.confirm_used,bg="light blue",font="Times 12 bold").place(x=190,y=330)
        #choosing from our salesperson people
        self.salesperson_p = [7007,7712,7726,7807,7808,7810,7813,7820,7822,7823]
        self.random_sp = random.randint(0,9)
              #salesperson_p[random_sp]
    def confirm_used(self):
        #combination
        d = datetime.datetime(self.var_year_used.get(), self.var_month_used.get(), self.var_day_used.get())
        saledate= d.date().isoformat()
        
        self.vehicle_id,self.owner_id,self.owner_fname,self.owner_lname,self.saleprice,self.sp_fname_2,self.sp_lname_2 = self.select_used(self.var_model_used.get(),self.var_company_used.get(),self.var_year_real_used.get(),self.var_color_used.get(),self.salesperson_p[self.random_sp])
                                                                        
        msg_box = tkinter.messagebox.askyesno("Validate","Price: "+str(self.saleprice)+"\nVehicle_id: "+str(self.vehicle_id)+"\nSalesperson: "+self.sp_fname_2+" "+self.sp_lname_2+"\nOwner: "+self.owner_fname+" "+self.owner_lname)
        if msg_box == True:
            self.insert_used(self.vehicle_id,self.owner_id,self.var_Ssn.get(),self.salesperson_p[self.random_sp],self.saleprice,saledate)
            self.window_used.destroy()
            msg_box_2 = tkinter.messagebox.showinfo("Successful","Your application form has completed!")
            
    def comp(self):
        self.window_sp.destroy()
        self.window_comp = Tk()
        
        window_comp_height = 370
        window_comp_width = 435
        screen_width = self.window_comp.winfo_screenwidth()
        screen_height = self.window_comp.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_comp_width/2))
        y_cordinate = int((screen_height/2) - (window_comp_height/2))
        self.window_comp.geometry("{}x{}+{}+{}".format(window_comp_width, window_comp_height, x_cordinate, y_cordinate))

        self.window_comp.title("companies")
        frame1 = Frame(self.window_comp)
        frame1.pack(fill=BOTH)
        #variables
        self.var_company_name = StringVar()
        self.var_year_s_comp = IntVar()
        self.var_month_s_comp = IntVar()
        self.var_day_s_comp = IntVar()
        self.var_year_e_comp = IntVar()
        self.var_month_e_comp = IntVar()
        self.var_day_e_comp = IntVar()
        
        label1 = Label(frame1,text = "companies' form",bg = "light green",fg = "blue"\
                       ,font = "Times 15 bold").pack(fill=BOTH)
        lb_company_name = Label(self.window_comp,text = "Company name",fg = "blue",font = "Times 13 bold").place(x=75,y=70)
        ent_company_name = Entry(self.window_comp,textvariable = self.var_company_name).place(x=205,y=70)
        # start_date
        lb_start = Label(self.window_comp,text = "Start Date: ",font = "Times 13 bold").place(x=40,y=120)
        lb_year_s = Label(self.window_comp,text = "year",fg = "blue",font = "Times 11 bold").place(x=90,y=160)
        ent_year_s = Entry(self.window_comp,textvariable = self.var_year_s_comp,width = 8).place(x=130,y=160)
        lb_month_s = Label(self.window_comp,text = "month",fg = "blue",font = "Times 11 bold").place(x=190,y=160)
        ent_month_s = Entry(self.window_comp,textvariable = self.var_month_s_comp,width = 8).place(x=240,y=160)
        lb_day_s = Label(self.window_comp,text = "day",fg = "blue",font = "Times 11 bold").place(x=310,y=160)
        ent_day_s = Entry(self.window_comp,textvariable = self.var_day_s_comp,width = 8).place(x=340,y=160)
        #end_date
        lb_start = Label(self.window_comp,text = "End Date: ",font = "Times 13 bold").place(x=40,y=200)
        lb_year_e = Label(self.window_comp,text = "year",fg = "blue",font = "Times 11 bold").place(x=90,y=240)
        ent_year_e = Entry(self.window_comp,textvariable = self.var_year_e_comp,width = 8).place(x=130,y=240)
        lb_month_e = Label(self.window_comp,text = "month",fg = "blue",font = "Times 11 bold").place(x=190,y=240)
        ent_month_e = Entry(self.window_comp,textvariable = self.var_month_e_comp,width = 8).place(x=240,y=240)
        lb_day_e = Label(self.window_comp,text = "day",fg = "blue",font = "Times 11 bold").place(x=310,y=240)
        ent_day_e = Entry(self.window_comp,textvariable = self.var_day_e_comp,width = 8).place(x=340,y=240)

        bt_conf_comp = Button(self.window_comp,text = "Confirm",command=self.confirm_comp,bg = "light blue",font = "Times 12 bold").place(x=190,y=290)
    def confirm_comp(self):
        #combination_start
        var_year_s_comp_2 = str(self.var_year_s_comp.get())
        var_month_s_comp_2 = str(self.var_month_s_comp.get())
        var_day_s_comp_2 = str(self.var_day_s_comp.get())
        self.Start_Date = var_year_s_comp_2+"-"+var_month_s_comp_2+"-"+var_day_s_comp_2
        #combination_emd
        var_year_e_comp_2 = str(self.var_year_e_comp.get())
        var_month_e_comp_2 = str(self.var_month_e_comp.get())
        var_day_e_comp_2 = str(self.var_day_e_comp.get())
        self.End_Date = var_year_e_comp_2+"-"+var_month_e_comp_2+"-"+var_day_e_comp_2

        self.window_comp.destroy()
        msg_box_2 = tkinter.messagebox.showinfo("Successful","Your company has registred!")
        
def main():
    A1 = application()
main()
        
