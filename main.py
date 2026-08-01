import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class MyApp (App):
   
    def build (self):
        btn = Button(text='Dad')
        btn2 = Button(text='Mom')
        btn.bind(on_press = self.On)
        btn2.bind(on_press = self.On)
        self.l = Label(text="Calculate your parents' genders",size_hint=(1,4))
        layout_btn = BoxLayout(orientation='horizontal')
        layout_all = BoxLayout(orientation='vertical')
        layout_btn.add_widget(btn)
        layout_btn.add_widget(btn2)
        layout_all.add_widget(self.l)
        layout_all.add_widget(layout_btn)
        return layout_all
    def On (self,instance):
        sen = ['girl','boy','man','woman','people','shit','...ahhhh~','cup','your father','your mathor','cat','tigger','Time', 'Knowledge', 'Power', 'Love', 'Light', 'Sound', 'Color', 'Space', 'Energy', 'Motion', 'Memory', 'Dream', 'Shadow', 'Stone', 'Water', 'Fire', 'Wind', 'Heart', 'Mind', 'Soul','Strength', 'Wisdom', 'Freedom', 'Justice', 'Peace', 'War', 'Storm', 'Thunder', 'Ice', 'Flame', 'Mist', 'Rainbow', 'Star', 'Moon', 'Sun', 'Galaxy', 'Nebula', 'Comet', 'Echo', 'Whisper', 'Riddle', 'Mystery', 'Miracle', 'Destiny', 'Glory', 'Honor', 'Grace', 'Mercy', 'Rage', 'Fury', 'a lion', 'a wolf', 'a hawk', 'a snake', 'a whale', 'a dolphin', 'an eagle', 'a raven', 'a spider', 'a scorpion', 'a pumpkin', 'a cactus', 'a lotus', 'a diamond', 'a pearl', 'a ruby', 'an emerald', 'a sapphire', 'an amethyst', 'a crystal']
        Gender = random.choice(sen)
        self.l.text = "Calculate your parents' genders\nyour "+instance.text+" is "+Gender
if __name__ == '__main__':
    MyApp().run()