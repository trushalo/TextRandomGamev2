import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from random import randint
from functools import partial

#Global variables
#btn char limit 172
#text char limit 500


activeList = [
{
'node': 2,
'mainText': 'Looking around you spot a yacht with a drunk kid collapsed on the gangway and an open airlock. This looks like an invitation; what do you do?',
'btn1': {'textbtn1':'Walk inside like the ship is yours,  call station control for departure, leave before anyone gets wise.',
'Node2': 5, 'Node1': 6 , 'Node0': 7, 'heat': True},
'btn2': {'textbtn2':'Don\'t assume anything. Go through the ship records, grab the title,crew compliment, and bribe a janitor friend to know who got off.',
'nextNode': 8, 'wealth': randint(-3, -1)},
'btn3': {'textbtn3':'Stealing a ship was a bad idea. Just go buy a ship instead.',
'nextNode': 10},

},
{
'node': 3,
'mainText': 'Node1 neutral result.',
'btn1': {'textbtn1':'btn1 string node2',
'nextNode': 5},
'btn2': {'textbtn2':'btn2 string node2',
'nextNode': 6},
'btn3': {'textbtn3':'btn3 string node3',
'nextNode': 7},

},
{
'node': 4,
'mainText': 'Node0 negative result.',
'btn1': {'textbtn1':'btn1 string node2',
'nextNode': 5},
'btn2': {'textbtn2':'btn2 string node2',
'nextNode': 6},
'btn3': {'textbtn3':'btn3 string node3',
'nextNode': 7},

}
]

#Active Dict
activeDict = {
'node': 0,
'mainText': 'You want to acquire a ship. How do you do it?',
'btn1': {'textbtn1':'Steal an undefended ship', 'Node2': 2, 'Node1': 3, 'Node0': 4, 'wealth': randint(5,15)},
'btn2': {'textbtn2':'Save up every credit for decades.',
'nextNode': 10, 'wealth': randint(10,25)},
'btn3': {'textbtn3':'Fortune smiles on you. You drained a large credit stash from a major corporation. Buy a ship and run like your life depends on it.\n It does.',
'nextNode': 10, 'wealth': randint(20,50),'heat': True}
}

currentStats = {'Brains: ' : 0,
'Braun: ' : 1,
'Health: ' : 10,
'Wealth: ' : None,
'Heat: ' : False,
'Ship: ' : None
}

#Global functions

def nodeChoice():
    n = randint(0,2)
    if n == 0:
        return 'Node0'
    elif n == 1:
        return 'Node1'
    else:
        return 'Node2'

def find(list, key, value):
    for i, dic in enumerate(list):
        if dic[key] == value:
            return i
    return 0


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        size_hint_y = None
        height = self.minimum_height
#        width = Window.width

        self.inside = GridLayout(size_hint_y=0.2)
        self.inside.cols = 4

        self.brains = Label(text="Brains: "+str(currentStats['Brains: ']))
        self.inside.add_widget(self.brains)
        
        self.braun = Label(text = 'Braun: '+str(currentStats['Braun: ']))
        self.inside.add_widget(self.braun)

        self.health = Label(text="Health: "+ str(currentStats['Health: ']))
        self.inside.add_widget(self.health)

        self.wealth = Label(text="Wealth:" + str(currentStats['Wealth: ']))
        if currentStats["Wealth: "] != None:
            self.inside.add_widget(self.wealth)

        self.add_widget(self.inside)
        self.mainScroll = ScrollView(do_scroll_x = False, do_scroll_y = True)
        self.mainScroll.width = Window.width#, size_hint=(2, None))

        self.scrollGrid = GridLayout()
        self.scrollGrid.cols = 1
        self.scrollGrid.width = Window.width
        self.mainScroll.add_widget(self.scrollGrid)

        self.mainText = Label(text=activeDict['mainText'], text_size=(None, None), font_size = '12sp',pos_hint={'center_x': 0.5, 'center_y': .85}, halign='left', valign='middle',size_hint_y=1.5)
        self.mainText.bind(size = self.setting_function)

        self.scrollGrid.add_widget(self.mainText)

        self.btn1 = Button(text=activeDict['btn1']['textbtn1'], disabled=False, font_size = '12sp', pos_hint={'center_x': 0.5, 'center_y': .85}, halign='center', valign='middle',size_hint_y=None)
        self.btn1.bind(size = self.setting_function1)
        self.btn1.bind(on_press = self.pressed)#bind(on_press=partial(self.pressed, 'btn1'))
        self.scrollGrid.add_widget(self.btn1)
        
        self.btn2 = Button(text=activeDict['btn2']['textbtn2'], disabled = False, font_size ='12sp',pos_hint={'center_x': 0.5, 'center_y': .85}, halign='center', valign='middle',size_hint_y=None)
        self.btn2.text_size = (self.width, None)
        self.btn2.bind(on_press=self.pressed)
        self.btn2.bind(size = self.setting_function2)
        
        self.scrollGrid.add_widget(self.btn2)
        
        self.btn3 = Button(text=activeDict['btn3']['textbtn3'], disabled = False, font_size ='12sp',pos_hint={'center_x': 0.5, 'center_y': .85}, halign='center', valign='middle',size_hint_y=None)
        self.btn3.bind(size = self.setting_function3)
        self.btn3.bind(on_press=self.pressed)
        self.scrollGrid.add_widget(self.btn3)
        self.add_widget(self.mainScroll)
        
#Wrap text functions
    def setting_function(self, *args):
        self.mainText.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.mainText.text_size=self.size
        
    def setting_function1(self, *args):
        self.btn1.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.btn1.text_size=self.size
        
    def setting_function2(self, *args):
        self.btn2.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.btn2.text_size=self.size
        
    def setting_function3(self, *args):
        self.btn3.pos_hint = {'center_x': 0.5, 'center_y': .85}
        self.btn3.text_size=self.size
        
#Run the button click functions
    def pressed(self, instance):
#        pass
        global activeDict, activeList, currentStats
        try: 
            listIndex = int(find(activeList, 'node',activeDict['btn1']['nextNode']))
        except KeyError:
            listIndex = int(find(activeList, 'node',activeDict['btn1'][nodeChoice()]))
                     
#Wealth update            
        try: 
            wealthTemp = activeDict['btn1']['wealth']
            currentStats['Wealth: '] = currentStats['Wealth: '] + wealthTemp
            self.wealth.text = currentStats['Wealth: '] + str(wealthTemp)
            
        except KeyError:
            pass
        except TypeError:
            currentStats['Wealth: '] = activeDict['btn1']['wealth']
            self.wealth.text = 'Wealth: ' +str(currentStats['Wealth: '])
            self.inside.add_widget(self.wealth)

#Health update
        try:
            healthTemp  = activeDict['btn1']['Health: ']
            currentStats['Health: '] = currentStats['Health: '] + healthTemp
            self.health.text='Health: ' + str(currentStats['Health: '])
            if currentStats['Health: ']<1:
                self.mainText.text = 'You have died. What do you think of the afterlife?'
                
        except KeyError:
            pass
            
        try:
            currentStats['Heat: '] = activeDict['btn1']['heat']
        except KeyError:
            pass
        
#update display

        activeDict = activeList[listIndex]
        self.mainText.text = activeDict['mainText']
        self.btn1.text=activeDict['btn1']['textbtn1']
        self.btn2.text=activeDict['btn2']['textbtn2']
        self.btn3.text=activeDict['btn3']['textbtn3']
            
#quit method        
    def quit():
        App.get_running_app().stop()

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
