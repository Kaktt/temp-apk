from kivy.app import App
from kivy.uix.label import Label

class TempApp(App):
    def build(self):
        return Label(text="សួស្តីពី temp.apk!")

if __name__ == "__main__":
    TempApp().run()
