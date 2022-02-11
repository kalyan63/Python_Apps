import kivy
  
from kivy.app import App
from kivy.uix.button import Label
  

class HelloKivy(App):
  
    # This returns the content we want in the window
    def build(self):
  
        # Return a label widget with Hello Kivy
        return Label(text ="Hello Geeks for new start")
  
helloKivy = HelloKivy()
helloKivy.run()