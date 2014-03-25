from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import \
    ObjectProperty
import time


class Object(Widget):
    """Class to manage drag and drop
   
    """   
    def on_touch_move(self, touch):
        """Function called when the object is moved
        
        :param touch: finger on the screen     
        
        """       
        #If the current object is the one grab
        if touch.grab_current is self:
            #Update of position
            self.parent.touched_object = self
            self.center_x = touch.x
            self.center_y = touch.y          
    
    def on_touch_down(self, touch):
        """Function called when the object is double clicked
        
        :param touch: finger on the screen     
        
        """
        #Get the object touched by the user    
        if self.collide_point(*touch.pos): 
            if touch.is_double_tap:    
                #Play a sound if the user do a double tap           
                sound = SoundLoader.load(self.text)
                sound.play()
                return;
            #Set opacity to display the current selected object
            self.opacity = 0.2
            #The object is grabbed
            touch.grab(self)
            return True

    def on_touch_up(self, touch):
        """Function called when the object is dropped after a move
        
        :param touch: finger on the screen     
        
        """
        #If this is the correct object
        if touch.grab_current is self:    
            #The Object is ungrabbed
            touch.ungrab(self)  
            #The initial opacity is set                
            self.opacity = 1
            #Check if the object has been dropped on the category House
            if (self.collide_widget(self.parent.category_house)):
                print("House touched")
                #Check if the object has been dropped on the good category
                if (self.category=="house"):
                    print("Congratulations !")
                    #Object is removed
                    self.parent.remove_widget(self)
                    return True
                else:
                    print("This is the wrong category")
                    #The object is moved back to the initial position
                    self.pos = self.pos_base

            #Check if the object has been dropped on the category Vehicle
            elif(self.collide_widget(self.parent.category_vehicle)):
                print("Vehicle touched")
                #Check if the object has been dropped on the good category
                if (self.category=="vehicle"):
                    print("Congratulations !")
                    #Object is removed
                    self.parent.remove_widget(self)
                    return True
                else:
                    print("This is the wrong category")
                    #The object is moved back to the initial position
                    self.pos = self.pos_base

            #Check if the object has been dropped on the category Character
            elif(self.collide_widget(self.parent.category_character)):
                print("Character touched")
                #Check if the object has been dropped on the good category
                if (self.category=="character"):
                    print("Congratulations !")
                    #Object is removed
                    self.parent.remove_widget(self)
                    return True
                else:
                    print("This is the wrong category")
                    #The object is moved back to the initial position
                    self.pos = self.pos_base   
            
            #The object is moved back to the initial position
            self.pos = self.pos_base

                    
class CategoryHouse(Widget):
    '''       
    This is the category which regroup all house objects
'''
    
class CategoryVehicle(Widget):
    '''       
    This is the category which regroup all vehicle objects
'''

class CategoryCharacter(Widget):
    '''       
    This is the category which regroup all character objects
'''
class Game2(Widget):
    
    #Define the three categories
    category_house = ObjectProperty(None)
    category_vehicle = ObjectProperty(None)
    category_character = ObjectProperty(None)
    
    
    def update(self, dt):
        pass
    
    def on_winning(self, touch):
        pass
    def get_Widget(self):
        return self.Widget

class Game2App(App):
    def build(self):
        game = Game2()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    Game2App().run()