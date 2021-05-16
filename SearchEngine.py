from fetch import hdi
import asyncio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Frame(BoxLayout):
    searchbox = ObjectProperty(None)
    body = ObjectProperty(None)
    pass

    def capture(self):
        result = asyncio.run(hdi(self.searchbox.text))
        self.body.text = result
        print(result)

class Search(App):
    def build(self):
        self.title = "Search Engine"

        return Frame()


if __name__ == "__main__":
    print(asyncio.run(hdi("Comment in C")))
    Search().run()
    #print(asyncio.run(hdi("exit c program")))

# TODO: Add progress bar and toggle button
# TODO: Toggle button for howdoi, wiki and web

