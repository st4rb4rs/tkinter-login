from tkinter import *
import sys, os
import newlogins as logins
import pagetwo
#users and passes dictionary
lookup = dict(zip(logins.users, logins.passes))
#globals
bg_color = '#111'
fg_color = '#00ee00'
#commands
def errmsg(strg):
    err = Toplevel()
    err.config(bg=bg_color)
    err.title('Error')
    txt = Label(err,text=strg, font=('Terminal',12),bg=bg_color,fg=fg_color)
    ok = Button(err, text='Ok',font=('Terminal',12),bg=bg_color,fg=fg_color,command=err.destroy)
    txt.pack()
    ok.pack()
    err.after(5000, lambda: err.destroy())

def restart():
    os.startfile('main.py')
    sys.exit() 

def signup():
    new_user = sue1.get()
    new_pasw = sue2.get()
    conf_pasw = sue3.get()
    sue1.delete(0, END), sue2.delete(0, END), sue3.delete(0, END)
    #checks if proper criteria is met 
    if new_pasw != conf_pasw:
        errmsg('Passwords must Match')
    if new_user == '' or new_pasw == '':
        errmsg('please enter both fields')
        return
    if len(new_user) < 4 or len(new_pasw) < 4:
        errmsg('Username or password must be at least 4 chars long each.')
        return
    if new_user == new_pasw:
        errmsg('User and Password must be different')
        return
    for i in range(len(logins.users)):
        if new_user == logins.users[i]:
            errmsg('Username taken, try something different')
            return
    #uhhhhhh i mean it works?
    logins.users.append(new_user)
    logins.passes.append(new_pasw)
    f = open('newlogins.py','w')
    f.write('users = ' + str(logins.users) + '\n')
    f.write('passes = ' + str(logins.passes) + '\n')
    restart()

def login():
    global is_loggedin
    user = lge1.get()
    pasw = lge2.get()
    lge2.delete(0, END)
    #pre-login file searching checks
    if user == '' or pasw == '':
        errmsg('please enter both fields')
        return
    if len(user) < 4 or len(pasw) < 4:
        errmsg('Username or password must be at least 4 chars long each.')
        lge1.delete(0, END)
        return
    #main check
    if lookup.get(user, None) == pasw:
        mainpage()
    else:
        errmsg('Invalid user or password, try again.')
#pages
#when logged in
def mainpage():
    #clear login page
    clearstart()
    return
#start
def start_page():
    global lge1, lge2, sue1, sue2, sue3, frame1, frame2, spc1, spc2
    spc1 = Frame(root,width=30,bg=bg_color)
    spc2 = Frame(root,width=30,bg=bg_color)
    frame1 = Frame(root,width=250, bg=bg_color)#, relief=RAISED, bd = 3)
    frame2 = Frame(root,width=250, bg=bg_color)#, relief=RAISED, bd = 3)

    #login box
    lgspc1 = Frame(frame1,height=10,width=250,bg=bg_color)
    lgspc2 = Frame(frame1,height=10,width=250,bg=bg_color)
    lgspc3 = Frame(frame1,height=10,width=250,bg=bg_color)
    lgspc4 = Frame(frame1,height=10,width=250,bg=bg_color)
    lg1 = Label(frame1, text='L O G   I N',font=('Small Fonts', 12), fg=fg_color, bg=bg_color,relief=GROOVE,bd=2)
    lg2 = Label(frame1, text='USERNAME:',font=('Small Fonts', 12), fg=fg_color, bg=bg_color)
    lge1 = Entry(frame1, fg='black', bg='white', font=('Terminal', 12))
    lg3 = Label(frame1, text='PASSWORD:',font=('Small Fonts', 12), fg=fg_color, bg=bg_color)
    lge2 = Entry(frame1, fg='black', bg='white', font=('Terminal', 12),show='*')
    lgb1 = Button(frame1, text='ENTER',bg=bg_color,fg=fg_color,font=('Small Fonts', 12),command=login)

    #sign up box
    suspc1 = Frame(frame2,height=10,width=250,bg=bg_color)
    suspc2 = Frame(frame2,height=10,width=250,bg=bg_color)
    suspc3 = Frame(frame2,height=10,width=250,bg=bg_color)
    suspc4 = Frame(frame2,height=10,width=250,bg=bg_color)
    su1 = Label(frame2, text='S I G N   U P',font=('Small Fonts', 12), fg=fg_color, bg=bg_color,relief=GROOVE,bd=2)
    su2 = Label(frame2, text='USERNAME:',font=('Small Fonts', 12), fg=fg_color, bg=bg_color)
    sue1 = Entry(frame2, fg='black', bg='white', font=('Terminal', 12))
    su3 = Label(frame2, text='PASSWORD:',font=('Small Fonts', 12), fg=fg_color, bg=bg_color)
    sue2 = Entry(frame2, fg='black', bg='white', font=('Terminal', 12),show='*')
    su4 = Label(frame2, text='CONFIRM:',font=('Small Fonts', 12), fg=fg_color, bg=bg_color)
    sue3 = Entry(frame2, fg='black', bg='white', font=('Terminal', 12),show='*')
    sub1 = Button(frame2, text='ENTER',bg=bg_color,fg=fg_color,font=('Small Fonts', 12),command=signup)
    #login box pack
    lgspc1.pack()
    lg1.pack()
    lgspc2.pack()
    lg2.pack()
    lge1.pack()
    lgspc3.pack()
    lg3.pack()
    lge2.pack()
    lgspc4.pack()
    lgb1.pack()
    spc1.pack(side=LEFT)
    frame1.pack(side=LEFT)
    #sign up box pack
    suspc1.pack()
    su1.pack()
    suspc2.pack()
    su2.pack()
    sue1.pack()
    suspc3.pack()
    su3.pack()
    sue2.pack()
    su4.pack()
    sue3.pack()
    suspc4.pack()
    sub1.pack()
    spc2.pack(side=RIGHT)
    frame2.pack(side=RIGHT)

def clearstart():
    frame1.pack_forget()
    frame2.pack_forget()
    spc1.pack_forget()
    spc2.pack_forget()
    ssp.pack_forget()
    sp.pack_forget()
    title.pack_forget()
    b1.pack_forget()
    return
def credit():
    c = Toplevel()
    c.overrideredirect(True)
    c.geometry('1580x920')
    c.config(bg=bg_color)
    s = Frame(c,height=360,bg=bg_color)
    txt = Label(c,text='2021 Jack Adkins', font=('Terminal',14),bg=bg_color,fg=fg_color)
    s.pack()
    txt.pack()
    c.after(3000,lambda: c.withdraw())

def main():
    global root, ssp, title, sp, b1
    root = Tk()
    root.geometry('600x400')
    root.title('Login')
    root.config(bg=bg_color)
    root.minsize(height=375,width=590) #TODO once i get other stuff setup. Update:  DONE!
    #root.resizable(False, False)
    #title
    ssp = Frame(root,height=30,bg=bg_color)
    title = Label(root,text='LOGIN (WIP)',font=('Terminal',36),bg=bg_color,fg=fg_color)
    ssp.pack()
    title.pack()
    #start page
    start_page()
    #bottom
    sp = Frame(root,height=30,bg=bg_color)
    b1 = Button(root,text='[c]', font=('Small Fonts',10),bg=bg_color,fg=fg_color,relief=FLAT,command=credit)
    sp.pack(side=BOTTOM)
    b1.pack(side=BOTTOM)
    #mainloop
    root.mainloop()

while __name__ == '__main__':
    main()
    print('Goodbye!')
    sys.exit()