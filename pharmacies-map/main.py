from tkinter import *
from tkintermapview import TkinterMapView
#=====================================================
root = Tk()
root.geometry('880x450')
root.title('Pharmacies | 24h/7d')
root.iconbitmap('icon.ico')
root.configure(background='white')
#=== CODING BACK-END =================================
#=== country get =====================================
def Cunt():
    country = entry1.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}$y={y}&z={z}&s=Ga", max_zoom=22)
    map.set_address(country, marker=True)
#== pharmacy 1 =======================================
def farm1():
    pharmacy1 = button2.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&h1=en&x={x}$y={y}&z={z}&s=Ga", max_zoom=22)
    map.set_position(15.35889250192969, 44.18269569425643)
    map.set_zoom(15)
    marker = map.set_marker(15.35889250192969, 44.18269569425643)
    marker.set_text('[CENTRAL PHARMACY]')
#=====================================================
#=== title ===========================================
title1 = Label(root,
              text='Central and night shift pharmacies project',
              fg='white',
              bg='black',
              font=('Tajawal', 18),
              )
title1.pack(fill=X)
#=== logo ============================================ 
logo = PhotoImage(file='1.png')
lab_log = Label(root, image=logo, bd=0, bg='white')
lab_log.place(x=10,y=40)
#-----------------------------------------------------
#=== Left side | label1 + entry1 + button1 ===========
label1 = Label(root, text='Country:', font=('Tajawal 13'), fg='black', bg='white')
label1.place(x=10,y=260)
# fg= font color | bg= background-color | 
#---------------------------------------------------------------------------------
entry1 = Entry(root, font=('Tajawal 14'), width=10, bd=2, relief=GROOVE )
entry1.place(x=140,y=260)
#
#---------------------------------------------------------------------------------
button1 = Button(root,  
          text='Get Country',  
          bg='green', 
          fg='white', bd=1, relief=SOLID, cursor='hand2', command=Cunt,)
button1.place(x=260,y=260)
#
#-----------------------------------------------------------------------------------------------------
#=== pharmacies button ===============================
button2 = Button(root, 
                 text='pharmacy1', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', fg='black', bd=1, relief=SOLID, command=farm1)
button2.place(x=10,y=300)
#------------------------
button3 = Button(root, 
                 text='pharmacy2', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', fg='black', bd=1, relief=SOLID)
button3.place(x=130,y=300)
#-------------------------
button4 = Button(root, 
                 text='pharmacy3', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button4.place(x=250,y=300)
#--------------------------
button5 = Button(root, 
                 text='pharmacy4', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button5.place(x=10,y=340)
#--------------------------
button6 = Button(root, 
                 text='pharmacy5', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button6.place(x=130,y=340)
#--------------------------
button7 = Button(root, 
                 text='pharmacy6', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button7.place(x=250,y=340)
#--------------------------
button8 = Button(root, 
                 text='pharmacy7', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button8.place(x=10,y=380)
#--------------------------
button9 = Button(root, 
                 text='pharmacy8', 
                 font=('Tajawal 12'), 
                 width=12, 
                 cursor='hand2', 
                 bg='white', 
                 fg='black', 
                 bd=1, 
                 relief=SOLID)
button9.place(x=130,y=380)
#--------------------------
button10 = Button(root, 
                  text='pharmacy9', 
                  font=('Tajawal 12'), 
                  width=12, 
                  cursor='hand2', 
                  bg='white', 
                  fg='black', 
                  bd=1, 
                  relief=SOLID)
button10.place(x=250,y=380)
#=====================================================
#=== right side | MAP - 
map = TkinterMapView(root, width=500, height=400, corner_radius=2)
map.place(x=370,y=45)
#================================
#=====================================================
root.mainloop() #-------------------------------------
#=====================================================