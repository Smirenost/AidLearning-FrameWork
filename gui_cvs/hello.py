from cvs import *
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        # return of the root widget
        return gui.Label("Hello world!", width=100, height=30)

initcv(cvs.openwin)
startcv(MyApp)