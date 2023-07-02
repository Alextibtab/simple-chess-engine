from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass


class PlayerVsPlayerScreen(Screen):
    pass


class PlayerVsComputerScreen(Screen):
    pass


class ComputerVsComputerScreen(Screen):
    pass


class ChessApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(PlayerVsPlayerScreen(name="player_vs_player"))
        sm.add_widget(PlayerVsComputerScreen(name="player_vs_ai"))
        sm.add_widget(ComputerVsComputerScreen(name="ai_vs_ai"))

        return sm


if __name__ == "__main__":
    ChessApp().run()
