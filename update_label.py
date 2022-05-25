from kivy.app import App
from kivy.lang import Builder
import os
from kivy.properties import ObjectProperty
from os.path import dirname, join
from kivy.uix.widget import Widget
from kivy.utils import platform


class MyLayout(Widget):
    def press(self):
        name = self.ids.name_input.text
        self.ids.name_input.text = ''
        self.ids.name_label.text = name if name != '' else "What's your name?"

        self.worker()

    def worker(self):
        if platform == "android":
            try:
                from android.permissions import request_permissions, Permission
                request_permissions(
                    [
                        Permission.READ_EXTERNAL_STORAGE,
                        Permission.WRITE_EXTERNAL_STORAGE
                    ]
                )
                app_folder = os.path.dirname(os.path.abspath(__file__))
                path = "/storage/emulated/0/Download/0111down.txt"
            except:
                self.ids.name_label.text += '\nCould not get permission!'

        else:
            path = '0111down.txt'

        try:
            f = open(path, 'w')
            f.write(f'new file\n{self.ids.name_label.text}')
            f.close()
            self.ids.name_label.text += '\nWrote successfully!'
        except Exception as e:
            self.ids.name_label.text += f'\nCould not write!\n{e}'


kv = Builder.load_file('update_label.kv')


class AwesomeApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    AwesomeApp().run()
