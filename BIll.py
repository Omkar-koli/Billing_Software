from tkinter import*
import math,random,os
from tkinter import messagebox
from ctypes.wintypes import MSG
import smtplib
from email.message import EmailMessage

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#8FC0A9"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="black",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        #===========variables===========#
        #==========grocery===========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.flour=IntVar()

        #======Cosmetic======
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.shampoo=IntVar()
        self.gell=IntVar()
        self.conditoner=IntVar()
        #========Stationary========
        self.book=IntVar()
        self.scissors=IntVar()
        self.glue=IntVar()
        self.sketch_pen=IntVar()
        self.sticky_notes=IntVar()
        self.pen=IntVar()
        
        #======Total Product Price & Tax variable====
        self.grocery_price=StringVar()
        self.cosmetic_price=StringVar()
        self.stationary_price=StringVar()

        self.grocery_tax=StringVar()
        self.cosmetic_tax=StringVar()
        self.stationary_tax=StringVar()

        #=======Customer=====
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.email_id=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        # ==========Customer Details Frame
        F1 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="#FAF3DD", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="black", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15,textvariable=self.c_name ,font="arial 15", relief=SUNKEN, bd=7, ).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="black", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phon ,font="arial 15", relief=SUNKEN, bd=7, ).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Email-ID", bg=bg_color, fg="black", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.email_id ,font="arial 15", relief=SUNKEN, bd=7, ).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Mail",command=self.mail_app, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10,
                                                                                        pady=10)

        # ==========Cosmetics Frame

        F2 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="#FAF3DD", bg=bg_color)
        F2.place(x=348, y=180, width=325, height=380)
        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10,textvariable=self.soap ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        hair_s_lbl = Label(F2, text="Shampoo", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10,textvariable=self.shampoo ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        Conditioner_lbl = Label(F2, text="Conditioner", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Conditioner_txt = Entry(F2, width=10,textvariable=self.conditoner, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=10)

        hair_g_lbl = Label(F2, text="Hair gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)
        #===========Grocery
        F3 = LabelFrame(self.root, bd=10,relief=SUNKEN, text="Grocery", font=("times new roman", 15, "bold"),fg="#FAF3DD", bg=bg_color)
        F3.place(x=5, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        g2_lbl = Label(F3, text="Flour", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.flour ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)
        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                     padx=10, pady=10)

        g4_lbl = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                     padx=10, pady=10)

        g5_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                     padx=10, pady=10)

        g6_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)

        # ==========Stationary

        F4 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Stationary", font=("times new roman", 15, "bold"),
                        fg="#FAF3DD", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Book", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.book, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)
        c2_lbl = Label(F4, text="Scissors", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.scissors, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                     column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)

        c3_lbl = Label(F4, text="Glue", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.glue, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                     padx=10, pady=10)

        c4_lbl = Label(F4, text="Sketch Pen", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.sketch_pen, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                     padx=10, pady=10)

        c5_lbl = Label(F4, text="Sticky notes", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.sticky_notes, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                     padx=10, pady=10)

        c6_lbl = Label(F4, text="Pen", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=10,
                                                                                                           sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.pen, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)
        # ==========Billing Area

        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=380, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        # ========Button Frame
        F6 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="#FAF3DD", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cosmetic_price, bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_price, bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Stationary Price", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.stationary_price, bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_tax, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Stationary Tax", bg=bg_color, fg="black",
                       font=("times now roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.stationary_tax, bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)
        total_btn = Button(btn_F,command=self.total, text="Total", bg="cadetblue", fg="black", pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill",command=self.bill_area, bg="cadetblue", fg="black", pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="cadetblue", fg="black", pady=15, width=10, bd=2,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="cadetblue", fg="black", pady=15, width=10, bd=2,
                          font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):

        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.flour.get()*120
        self.g_d_p=self.daal.get()*60
        self.g_fd_p=self.food_oil.get()*180
        self.g_w_p=self.wheat.get()*150
        self.g_s_p=self.sugar.get()*35

        self.total_grocery_price=float(
                                   self.g_r_p+
                                   self.g_f_p+
                                   self.g_d_p+
                                   self.g_fd_p+
                                   self.g_w_p+
                                   self.g_s_p
                                   )
        self.grocery_price.set("Rs.  "+str(self.total_grocery_price))  
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs.   "+str(self.g_tax))

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*130
        self.c_fw_p=self.face_wash.get()*70
        self.c_sh_p=self.shampoo.get()*140
        self.c_cd_p=self.conditoner.get()*120
        self.c_g_p=self.gell.get()*95
        self.total_cosmetic_price=float(
                                   self.c_s_p+
                                   self.c_fc_p+
                                   self.c_fw_p+
                                   self.c_sh_p+
                                   self.c_cd_p+
                                   self.c_g_p
                                   )
        self.cosmetic_price.set("Rs.  "+str(self.total_cosmetic_price)) 
        self.c_tax=round((self.total_cosmetic_price*0.1),2)
        self.cosmetic_tax.set("Rs.   "+str(self.c_tax))
        
        self.s_b_p=self.book.get()*25
        self.s_s_p=self.scissors.get()*60
        self.s_g_p=self.glue.get()*40
        self.s_sp_p=self.sketch_pen.get()*35
        self.s_sn_p=self.sticky_notes.get()*60
        self.s_p_p=self.pen.get()*40
        
        self.total_stationary_price=float(
                                   self.s_b_p+
                                   self.s_s_p+
                                   self.s_g_p+
                                   self.s_sp_p+
                                   self.s_sn_p+
                                   self.s_p_p
                                   )
        self.stationary_price.set("Rs.  "+str(self.total_stationary_price))                           
        self.sn_tax=round((self.total_stationary_price*0.2),2)
                        
        self.stationary_tax.set("Rs.   "+str(self.sn_tax)) 

        self.total_bill=float( self.total_grocery_price+
                               self.total_cosmetic_price+
                               self.total_stationary_price+
                               self.g_tax+
                               self.c_tax+
                               self.sn_tax
                            )



    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tWelcome\n") 
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n Email_ID : {self.email_id.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\n Products\t\tQuantity\t\tPrice")
        self.txtarea.insert(END,f"\n========================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details invalid")
        
        else:  
            self.welcome_bill()
            #=======Grocery=============
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.flour.get()!=0:
                self.txtarea.insert(END,f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
                
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fd_p}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}") 

            #=======Cosmetics=======
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
                
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.shampoo.get()}\t\t{self.c_sh_p}")

            if self.conditoner.get()!=0:
                self.txtarea.insert(END,f"\n Conditoner\t\t{self.conditoner.get()}\t\t{self.c_cd_p}")

            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gell.get()}\t\t{self.c_g_p}")


            #=========Stationary========

            if self.book.get()!=0:
                self.txtarea.insert(END,f"\n BooKs\t\t{self.book.get()}\t\t{self.s_b_p}")

            if self.scissors.get()!=0:
                self.txtarea.insert(END,f"\n Scissors\t\t{self.scissors.get()}\t\t{self.s_s_p}")
                
            if self.glue.get()!=0:
                self.txtarea.insert(END,f"\n Glue\t\t{self.glue.get()}\t\t{self.s_g_p}")

            if self.sketch_pen.get()!=0:
                self.txtarea.insert(END,f"\n Sketch Pen\t\t{self.sketch_pen.get()}\t\t{self.s_sp_p}")

            if self.sticky_notes.get()!=0:
                self.txtarea.insert(END,f"\n Sticky Notes\t\t{self.sticky_notes.get()}\t\t{self.s_sn_p}")

            if self.pen.get()!=0:
                self.txtarea.insert(END,f"\n Pen\t\t{self.pen.get()}\t\t{self.s_p_p}")                          
            
            self.txtarea.insert(END,f"\n----------------------------------------")
            if self.grocery_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            
            if self.cosmetic_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            
            if self.stationary_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\n Stationary Tax\t\t\t{self.stationary_tax.get()}")
            
            self.txtarea.insert(END,f"\n----------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill\t\t\t Rs. {self.total_bill}")

            
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)     
            f1=open("Customer Bill/"+str(self.c_name.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Your Bill no: {self.bill_no.get()} has been saved successfully")
        else:
            return

    def clear_data(self):
            op=messagebox.askyesno("Clear","Clear everything?")
            if op>0:
                
            #==========grocery===========
             self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.flour.set(0)

            #======Cosmetic======
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.shampoo.set(0)
            self.gell.set(0) 
            self.conditoner.set(0)
            #========Stationary========
            self.book.set(0)
            self.scissors.set(0)
            self.glue.set(0)
            self.sketch_pen.set(0)
            self.sticky_notes.set(0)
            self.pen.set(0)
            
            #======Total Product Price & Tax variable====
            self.grocery_price.set("")
            self.cosmetic_price.set("")
            self.stationary_price.set("")

            self.grocery_tax.set("")
            self.cosmetic_tax.set("")
            self.stationary_tax.set("")

            #=======Customer=====
            self.c_name.set("")
            self.c_phon.set("")
            self.email_id.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
        
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Plan on leaving so soon?")
        if op>0:
            self.root.destroy()

    def mail_app(self):
        op=messagebox.askyesno("Email","DO you want to mail?")
        EMAIL_ADDRESS = 'inft.20101b0069@gmail.com'
        EMAIL_PASSWORD = 'nqyxxnuoddqyutew'
        Email_FROM = self.email_id.get()

        msg = EmailMessage()
        msg['Subject'] = 'Here is your bill thank you for shopping with us'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = Email_FROM
        msg.set_content('Here is your bill')

        msg.add_alternative(self.bill_data)

        with smtplib.SMTP('smtp.gmail.com', 25) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
            smtp.send_message(msg)

root=Tk()
obj=Bill_App(root)
root.mainloop()
