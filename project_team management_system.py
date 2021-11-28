import mysql.connector
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.properties import BooleanProperty 

from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.behaviors import DragBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.uix.recycleboxlayout import RecycleBoxLayout

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.dropdown import DropDown

import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
Config.set('graphics', 'resizable', True)
from kivy.core.window import Window
#Window.clearcolor = (1, 1, 1, 1)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SQL108SQL",
  database="pro_db"
)


class plta():
    def __init__(self):
        pass
    
    def shw(self,a,title,y,x,select):
        data = dict(a)
        
        courses = list(data.keys())
        if select==2:
            courses=data_b().get_task_by_l(courses)
        if select==3:
            courses=data_b().get_pro_l(courses)
        values = list(data.values())
        fig = plt.figure()

        # creating the bar plot
        plt.bar(courses, values, color ='maroon',
                width = 0.4)
         
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)
        return plt.gcf()
        
        
        
        
class data_b():
    def __init__(self):
        self.my_cur=mydb.cursor()
        #self.my_cur.execute("select name from people")

    def add_p_in_db(self,a,b):
        stri="INSERT INTO PEOPLE(name,EmailId) VALUES('{aa}','{bb}');"

        if  a and  b:
            self.my_cur.execute(stri.format(aa=a,bb=b))
            mydb.commit()
            


    

    def add_t_in_db(self,a,b,c):
        stri='INSERT INTO task(Name,Descr,type) VALUES("{aa}","{bb}","{cc}");'
        if  a and  b:
            self.my_cur.execute(stri.format(aa=a,bb=b,cc=c))
            mydb.commit()
    
    def add_pro_in_db(self,a,b,c):
        stri='INSERT INTO project(Name,Descr,Status) VALUES("{aa}","{bb}","{cc}");'
        if  a and  b:
            self.my_cur.execute(stri.format(aa=a,bb=b,cc=c))
            mydb.commit()
    
    
    def get_project(self):
        self.my_cur.execute("select * from project;")
        my_r=self.my_cur.fetchall()
        l=[]
        for i in my_r:
            l.append(i[1])
        return(l)
    
    def get_name(self):
        self.my_cur.execute("select * from people;")
        my_r=self.my_cur.fetchall()
        l=[]
        m=[]
        for i in my_r:
            l.append(i[0])
            m.append(i[1])
        return(l,m)
    
        
    def get_all_task(self,selecta):
        star="select * from task where task_id={a};"
        self.my_cur.execute(star.format(a=selecta))
        my_r=self.my_cur.fetchall()
        l,m,n,aaa,ooo=[],[],[],[],[]
        for i in my_r:
            l.append(i[0])
            m.append(i[1])
            n.append(i[2])
           
        i=selecta    
        stra="select name from people where id in (select people_id from peot where task_id={a});"
        istra="select name from project where project_id in (select project_id from prot where task_id={a});"
        self.my_cur.execute(stra.format(a=i))
        aaa=self.my_cur.fetchall()
        self.my_cur.execute(istra.format(a=i))
        ooo=self.my_cur.fetchall()
            
        return(l,m,n,aaa,ooo)
    
    
    def get_all_pro(self,selecta):
        stra="select * from project where name='{a}';".format(a=selecta)
        self.my_cur.execute(stra)
        my_r=self.my_cur.fetchall()
        l,m,n,o=[],[],[],[]
        for i in my_r:
            l.append(i[0])
            m.append(i[1])
            n.append(i[2])
            o.append(i[4])
            
        stra="select name from people where id in (select people_id from pp where project_id={a});"
        istra="select name from task where task_id in(select task_id from prot where project_id={a});"
        self.my_cur.execute(stra.format(a=i[0]))
        aaa=self.my_cur.fetchall()
        self.my_cur.execute(istra.format(a=i[0]))
        ooo=self.my_cur.fetchall()

            
        return(l,m,n,o,aaa,ooo)
    
    def get_all_peop(self,selecta):
        stra="select * from people where id={a};".format(a=selecta)
        self.my_cur.execute(stra)
        my_r=self.my_cur.fetchall()
        l,m,n=[],[],[]
        for i in my_r:
            l.append(i[0])
            m.append(i[1])
            n.append(i[2])
                
        stra="select name from project where project_id in (select project_id from pp where people_id={a});"
        istra="select name from task where task_id in (select task_id from peot where people_id={a});"
        self.my_cur.execute(stra.format(a=selecta))
        aaa=self.my_cur.fetchall()
        
        my_r=self.my_cur.execute(istra.format(a=selecta))
        ooo=self.my_cur.fetchall()
            
        return(l,m,n,aaa,ooo)
    
    def get_o_name(self):
            self.my_cur.execute("select * from people")
            my_r=self.my_cur.fetchall()
            l=[]
            m=[]
            for i in my_r:
                l.append(i[0])
                m.append(i[1])
                
            return(l,m)
    
    def get_o_task(self):
            self.my_cur.execute("select * from task")
            my_r=self.my_cur.fetchall()
            l=[]
            m=[]
            for i in my_r:
                l.append(i[0])
                m.append(i[1])
          
            return(l,m)
    
    def get_o_project(self):
            self.my_cur.execute("select * from project")
            my_r=self.my_cur.fetchall()
            l=[]
            m=[]
            for i in my_r:
                l.append(i[0])
                m.append(i[1])
                
            return(l,m)
    
    def get_task(self):
         self.my_cur.execute("select * from task")
         my_r=self.my_cur.fetchall()
         l=[]
         m=[]
         for i in my_r:
            l.append(i[0])
            m.append(i[1])
            
         return(l,m)

    def as_t_to_pe(self,a,b):
        checker='SELECT IF(EXISTS(select * from peot where people_id ={aa} and task_id={bb}), 1, 0)';
        stri='INSERT INTO peot(people_id,task_id )VALUES({aa},{bb});'
        for i in a:
            for j in b:
                self.my_cur.execute(checker.format(aa=i,bb=j))
                ss=self.my_cur.fetchall()
                if ss[0][0]:
                    return
                else:
                    self.my_cur.execute(stri.format(aa=i,bb=j))
                    mydb.commit()
    
    
    def as_pe_to_pro(self,a,b):
        checker='SELECT IF(EXISTS(select * from pp where people_id ={aa} and project_id={bb}), 1, 0)';
        stri='INSERT INTO pp(people_id,project_id )VALUES({aa},{bb});'
        #
        for i in a:
            for j in b:
                self.my_cur.execute(checker.format(aa=i,bb=j))
                ss=self.my_cur.fetchall()
                if ss[0][0]:
                    return
                else:
                    self.my_cur.execute(stri.format(aa=i,bb=j))
                    mydb.commit()
        
    def as_pro_to_t(self,a,b):
        checker='SELECT IF(EXISTS(select * from prot where project_id ={aa} and task_id={bb}), 1, 0)';
        stri='INSERT INTO prot(project_id,task_id )VALUES({aa},{bb});'
        #self.my_cur.execute(stri.format(aa=a,bb=b))
        for i in a:
            for j in b:
                    self.my_cur.execute(checker.format(aa=i,bb=j))
                    ss=self.my_cur.fetchall()

                    if ss[0][0]:
                        return
                    else:
                        self.my_cur.execute(stri.format(aa=i,bb=j))
                        mydb.commit()

    def get_grap_t(self,data):
        stri='select project_id,count(project_id) from pp where project_id in(select project_id from prot where task_id={a}) and people_id in(select people_id from peot where task_id={a}) group by project_id;'
        self.my_cur.execute(stri.format(a=data))
        aaa=self.my_cur.fetchall()

        return aaa
    
    def get_grap_pro(self,data):
        stri='select task_id,count(task_id) from peot where task_id in(select task_id from prot where project_id={a}) and people_id in(select people_id from pp where project_id={a}) group by task_id;'
        self.my_cur.execute(stri.format(a=data))
        aaa=self.my_cur.fetchall()

        return aaa
    
    def get_grap_peop(self,data):
      stri='select task_id,count(task_id) from prot where project_id in(select project_id from pp where people_id={a}) and task_id in(select task_id from peot where people_id={a}) group by task_id;'
      self.my_cur.execute(stri.format(a=data))
      aaa=self.my_cur.fetchall()

      return aaa     

    
    def get_task_by_l(self,data):
        stri="select name from project where project_id={a};"
        l=[]
        for i in data:
            self.my_cur.execute(stri.format(a=i))
            aaa=self.my_cur.fetchall()
            l.append(aaa[0][0])
        return l
            

    def get_pro_l(self,data):
        stri="select name from task where task_id={a};"
        l=[]
        for i in data:
            self.my_cur.execute(stri.format(a=i))
            aaa=self.my_cur.fetchall()
            l.append(aaa[0][0])
        return l
    
    


    def del_t(self,i):

        stri="delete from peot where task_id={a}"
        stri1="delete from prot where task_id={a}"
        stri2="delete from task where task_id={a}"
        self.my_cur.execute(stri.format(a=i))
        self.my_cur.execute(stri1.format(a=i))
        self.my_cur.execute(stri2.format(a=i))
        self.my_cur.fetchall()

class Tv(ScrollView):
    def __init__(self,**kwargs):
            super().__init__(**kwargs)
            pass



class Cust_screen_label(Label):
    def __init__(self,**kwargs):
            super().__init__(**kwargs)

            
            
    def up(self,te):
        final=te
        final = final.replace("[", "")
        final = final.replace("]", "")
        final = final.replace("[", "")
        final = final.replace("(", "")
        final = final.replace(")", "")
        final = final.replace("'", "")
        final = final.replace(",", " ")
        self.text=final
        

class GraphScreen(ScrollView):
    def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
    def replace(self,a,t,y,x,select):
        self.clear_widgets()
        p=plta()
        
        pltaaa =p.shw(a,t,y,x,select)
        self.add_widget(FigureCanvasKivyAgg(pltaaa))
        
        
class New_people(FloatLayout):
    pass


class Add_bu_peop(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Add_people_popup().open()




class Add_people_popup(Popup,DragBehavior):
     def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title="add people"
        self.size_hint=[0.4,0.4]
        self.drag_rectangle=self.x, self.y, self.width, self.height
        self.drag_timeout=100000
        self.drag_distance=0
        self.auto_dismiss=True
        self.add_widget(Poup_inside())
        
        
        
     def remov_self(self):
        self.dismiss()
        
class c_close(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            self.parent.clos()
            

class c_pop(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            self.parent.popo()            
            
            

class Poup_inside(BoxLayout):
    def __init__(self,**kwargs):
        super(Poup_inside,self,**kwargs).__init__(**kwargs)
        self.orientation='vertical'
        self.add_widget(Label(text="name"))
        self.txt1=User_name(font_size=15,text='')
        self.add_widget(self.txt1)
        self.add_widget(Label(text="Email"))
        self.txt2=User_mail(font_size=15,text='')
        self.add_widget(self.txt2)
        self.add_widget(c_pop(text="add"))
        self.add_widget(c_close(text="close"))
        
        
        
    def popo(self):
        data_b().add_p_in_db(self.txt1.text,self.txt2.text)
        self.txt1.text=""
        self.txt2.text=""

    def clos(self):
        self.parent.parent.parent.dismiss()
                        
class User_name(TextInput):
    pass
class User_mail(TextInput):
    pass




        
        
class Add_task(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Add_Task_popup().open()    




class Add_Task_popup(Popup,DragBehavior):
     def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title="add Task"
        self.size_hint=[0.4,0.5]
        self.drag_rectangle=self.x, self.y, self.width, self.height
        self.drag_timeout=100000
        self.drag_distance=0
        self.auto_dismiss=True
        self.add_widget(Task_Poup_inside())




class Task_add(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            self.parent.popo()
            
            
            
            

class Task_Poup_inside(BoxLayout):
    def __init__(self,**kwargs):
        super(Task_Poup_inside,self,**kwargs).__init__(**kwargs)
        self.orientation='vertical'
        self.add_widget(Label(text="name"))
        self.txt1=TextInput(font_size=15,text='')
        self.add_widget(self.txt1)
        self.add_widget(Label(text="Description"))
        self.txt2=TextInput(font_size=15,text='',multiline=True)
        self.add_widget(self.txt2)
        self.add_widget(Label(text="type"))
        
        self.txt3=TextInput(font_size=15,text='')
        self.add_widget(self.txt3)
        self.add_widget(Task_add(text="add"))
        self.add_widget(c_close(text="close"))
        
        


    def popo(self):
        data_b().add_t_in_db(self.txt1.text,self.txt2.text,self.txt3.text)
        self.txt1.text=""
        self.txt2.text=""
        self.txt3.text=""

    def clos(self):
        self.parent.parent.parent.dismiss()
        data_b().get_task()




class Add_project(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Add_Pro_popup().open()




class Add_Pro_popup(Popup,DragBehavior):
     def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title="add Project"
        self.size_hint=[0.4,0.5]
        self.drag_rectangle=self.x, self.y, self.width, self.height
        self.drag_timeout=100000
        self.drag_distance=0
        self.auto_dismiss=True
        self.add_widget(Pro_Poup_inside())




class Pro_add(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            self.parent.popo()
            
            
            
            

class Pro_Poup_inside(BoxLayout):
    def __init__(self,**kwargs):
        super(Pro_Poup_inside,self,**kwargs).__init__(**kwargs)
        self.orientation='vertical'
        self.add_widget(Label(text="name"))
        self.txt1=TextInput(font_size=15,text='')
        self.add_widget(self.txt1)
        self.add_widget(Label(text="Description"))
        self.txt2=TextInput(font_size=15,text='',multiline=True)
        self.add_widget(self.txt2)
        self.add_widget(Label(text="status"))
        
        self.txt3=TextInput(font_size=15,text='')
        self.add_widget(self.txt3)

        self.add_widget(Pro_add(text="add"))
        self.add_widget(c_close(text="close"))
        
        
    def popo(self):
        data_b().add_pro_in_db(self.txt1.text,self.txt2.text,self.txt3.text)
        self.txt1.text=""
        self.txt2.text=""
        self.txt3.text=""

    def clos(self):
        self.parent.parent.parent.dismiss()





class  Assign_task(Button):
    pass


class La(Label):
    pass
class La2(Label):
    pass
class La3(Label):
    pass
class Scrol(RecycleView):
     def __init__(self,**kwargs):
        super(Scrol,self,**kwargs).__init__(**kwargs)
        ll=data_b().get_project()
        self.data = [{'text': str(x)} for x in ll]
        
        
class Scrol_b(Button):
    def __init__(self,**kwargs):
        super(Scrol_b,self,**kwargs).__init__(**kwargs)
    def on_press(self):
        pro_tv(self.text,self.parent.parent.parent.children[0].ids.tv_label)

class MainFloat(FloatLayout): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(New_people())
        self.add_widget(La())
        self.add_widget(La2())
        self.add_widget(La3())
        self.add_widget(Scrol())
        
        self.add_widget(Tv())
        
    def _update(self):
        self.clear_widgets()
        self.__init__()
        
       
        
              
        
    def on_kv_post(self, *largs):
        self.add_widget(Recyc2())
        self.add_widget(Recyc1())
        self.add_widget(GraphScreen())

class Re_button(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        pass


class Del_Button(Button):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.is_t=False
        self.image_path="delete.png"
        self.pos=(self.pos[0]+self.size[0]/2.0) - 40/2.0, (self.pos[1]+self.size[1]/2.0) -40/2.0
        self.background_color= 0, 0, 0, 0
    def on_press(self):
        data_b().del_t(self.parent.get_id())
        self.parent.parent.remove_widget(self.parent)
        
        
def peop_tv(a,pp):
    
    l,m,n,aaa,ooo=data_b().get_all_peop(a)
    t1=""
    t2=""
    t3=""
    t4=""
    
    final='ID:  '+t1.join(str(l[0]))+"\n \n NAME:  "+t2.join(str(m[0]))+"\n \n Email:  "+ t3.join(str(n[0])) +"\n \n Involved in projects:  " +t3.join(   str(aaa)    )+" \n \n Tasks assigned:  "+t4.join(str(ooo))
    graph_data=data_b().get_grap_peop(l[0])
    pp.parent.parent.children[6].replace(graph_data,str(m[0]),"project","tasks",select=3)
    pp.up(final)
    
def task_tv(a,pp):
    l,m,n,aaa,ooo=data_b().get_all_task(a)
    t1=""
    t2=""
    t3=""
    t4=""
    t5=""
    final='ID:  '+t1.join(str(l[0]))+"\n \n NAME:  "+t2.join(str(m[0]))+"\n \n Description:  "+ t3.join(str(n[0])) +"\n \n Assigned to:  " +t4.join(str(aaa))+" \n \n Sub_tasked_in:  "+t5.join(str(ooo))
    
    a=data_b().get_grap_t(l[0])
    pp.parent.parent.children[6].replace(a,str(m[0]),"no. of people","projects",select=2)
    pp.up(final)

def pro_tv(a,pp):
    
    l,m,n,o,aaa,ooo=data_b().get_all_pro(a)
    t1=""
    t2=""
    t3=""
    t4=""
    t5=""
    t6=""
    final='ID:  '+t1.join(str(l[0]))+"\n \n NAME:  "+t2.join(str(m[0]))+"\n \n Description:  "+ t3.join(str(n[0])) +"\n \n Status:  " +t4.join(str(o[0]))+" \n \n Assigned to:  "+t5.join(str(aaa))+"\n \n subtasks:   "+t6.join(str(ooo))
    graph_data=data_b().get_grap_pro(l[0])
    pp.parent.parent.children[6].replace(graph_data,str(m[0]),"people","tasks",select=3)
    pp.up(final)
    
class User_Label(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 2
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    
        
    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        self.label1_text = data['label1']['text']
        self.label2_text = data['label2']['text']
        return super(User_Label, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(User_Label, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            peop_tv(self.label1_text,self.parent.parent.parent.children[0].ids.tv_label)
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))



    
class Recyc1(RecycleView):
     def __init__(self, **kwargs):
        super(Recyc1, self).__init__(**kwargs)
        l,m=data_b().get_name()
        self.data = [{'label1': {'text': str(i1)}, 'label2': {'text': str(i2)}} for i1, i2 in zip(l, m)]










class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class Task_Label(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 3

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        self.label1_text = data['label1']['text']
        self.label2_text = data['label2']['text']
        #self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        return super(Task_Label, self).refresh_view_attrs(
            rv, index, data)
    
    
    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(Task_Label, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        
    
        if is_selected :
            task_tv(self.label1_text,self.parent.parent.parent.children[0].ids.tv_label)
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))

    def get_id(self):
        return self.label1_text


class Recyc2(RecycleView):
    def __init__(self, **kwargs):
        super(Recyc2, self).__init__(**kwargs)
        l,m=data_b().get_task()
        self.data = [{'label1': {'text': str(i1)}, 'label2': {'text': i2}} for i1, i2 in zip(l, m)]
        
        
        
class Task_view(BoxLayout):
    def __init__(self,text="ddd",**kwargs):
        super(Task_view,self).__init__(**kwargs)
        self.orientation="horizontal"
        l=Label(text=text)
        x=Re_button(text="jkjk")
        self.add_widget(x)
        self.add_widget(l)
        
        
        
        
        
class Asssign_task(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Assign_Task_popup(tad=0).open()         
        
        
        
class Assign_Task_add(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            data_b().as_t_to_pe(self.parent.tas, self.parent.pep)
            
            
            
            
            
            
            

class Asssign_peop(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Assign_Task_popup(tad=1).open() 

class Assign_peop_add(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            data_b().as_pe_to_pro(self.parent.tas, self.parent.pep)
            
            
            
class Refresh(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        self.parent.parent._update()        
            


            
class Asssign_pro(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    
    def on_press(self):
        Assign_Task_popup(tad=2).open() 

class Assign_pro_add(Button):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            
        def on_press(self):
            data_b().as_pro_to_t(self.parent.tas, self.parent.pep)
            
        
class Assign_Task_popup(Popup,DragBehavior):
     def __init__(self,tad,**kwargs):
        super().__init__(**kwargs)
        self.title="add Task"
        self.size_hint=[0.4,0.5]
        self.drag_rectangle=self.x, self.y, self.width, self.height
        self.drag_timeout=100000
        self.drag_distance=0
        self.auto_dismiss=True
        if tad==0:
            self.add_widget(Assign_Task_Poup_inside(tad=tad)) 
        if tad==1:
            self.add_widget(Assign_peop_Poup_inside(tad=tad))
        if tad==2:
            self.add_widget(Assign_pro_Poup_inside(tad=tad))
               
        
        
class Assign_Task_Poup_inside(BoxLayout):
    def __init__(self,tad,**kwargs):
        super(Assign_Task_Poup_inside,self,**kwargs).__init__(**kwargs)
        self.tas=[]
        self.pep=[]
        self.orientation='vertical'
        if tad==0:
            self.add_widget(Assign_Task_add(text="add"))

        self.add_widget(c_close(text="close"))   
        
        
    def clos(self):
        self.parent.parent.parent.dismiss()        
        
class Assign_peop_Poup_inside(BoxLayout):
    def __init__(self,tad,**kwargs):
        super(Assign_peop_Poup_inside,self,**kwargs).__init__(**kwargs)
        self.tas=[]
        self.pep=[]
        self.orientation='vertical'
        if tad==1:
            self.add_widget(Assign_peop_add(text="add"))
        self.add_widget(c_close(text="close"))        
    

    def clos(self):
        self.parent.parent.parent.dismiss()







class Assign_pro_Poup_inside(BoxLayout):
    def __init__(self,tad,**kwargs):
        super(Assign_pro_Poup_inside,self,**kwargs).__init__(**kwargs)
        self.tas=[]
        self.pep=[]
        self.orientation='vertical'
        if tad==2:
            self.add_widget(Assign_pro_add(text="add"))
        self.add_widget(c_close(text="close"))

    def clos(self):
        self.parent.parent.parent.dismiss()



        
class MultiSelectSpinner(Button):
    """Widget allowing to select multiple text options."""

    dropdown = ObjectProperty(None)
    """(internal) DropDown used with MultiSelectSpinner."""

    values = ListProperty([])
    """Values to choose from."""

    selected_values = ListProperty([])
    """List of values selected by the user."""

    def __init__(self, topa=True,**kwargs):
        self.topa=topa
        self.bind(dropdown=self.update_dropdown)
        self.bind(values=self.update_dropdown)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.bind(on_release=self.toggle_dropdown)
        self.l=[]
        self.m=[]
        
    def uu(self):
        self.text='people'
        l,m=data_b().get_o_name()
        self.l=l
        self.m=m
        return m
    
    def vv(self):
        self.text='task'
        l,m=data_b().get_o_task()
        self.l=l
        self.m=m
        return m
    
    def ww(self):
        self.text="project"
        l,m=data_b().get_o_project()
        self.l=l
        self.m=m
        return m
        
    def toggle_dropdown(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    def update_dropdown(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown(effect_cls= "ScrollEffect",scroll_type= ['bars'])
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                self.dropdown.add_widget(b)

    def select_value(self, instance, value):
        if value == 'down':
            if instance.text not in self.selected_values:
                self.selected_values.append(instance.text)
                if self.topa:
                    qq=self.m.index(instance.text)
                    
                    self.parent.tas.append(self.l[qq])
                else:
                    qq=self.m.index(instance.text)
                    self.parent.pep.append(self.l[qq])
        else:
            if instance.text in self.selected_values:
                self.selected_values.remove(instance.text)
                if self.topa:
                    qq=self.m.index(instance.text)
                    self.parent.tas.remove(self.l[qq])
                else:
                    qq=self.m.index(instance.text)
                    self.parent.pep.remove(self.l[qq])
                

            
    def on_selected_values(self, instance, value):
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''        

        
        
class demoApp(App): 
    # defining build() 
    def build(self): 
        # returning the instance of root class 
        #self.load_kv('demo.kv')
        return MainFloat()
    

   
if __name__ == "__main__": 
    print("hello")
    demoApp().run() 
    
