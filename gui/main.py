import cProfile

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithTabbedPanel


class MenuScreen(Screen):
    pass


class PlayerVsPlayerScreen(Screen):
    pass


class PlayerVsComputerScreen(Screen):
    pass


class ComputerVsComputerScreen(Screen):
    pass


class ChessApp(App):
    def on_start(self):
        self.profile = cProfile.Profile()
        self.profile.enable()

    def on_stop(self):
        self.profile.disable()
        self.profile.dump_stats("chess_app.profile")

    def build(self):
        self.settings_cls = SettingsWithTabbedPanel
        self.icon = "assets/W_King.png"

        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name="menu"))
        self.sm.add_widget(PlayerVsPlayerScreen(name="player_vs_player"))
        self.sm.add_widget(PlayerVsComputerScreen(name="player_vs_ai"))
        self.sm.add_widget(ComputerVsComputerScreen(name="ai_vs_ai"))

        return self.sm

    def build_config(self, config):
        config.read("config.ini")

    def display_settings(self, settings):
        if not self.sm.has_screen("settings"):
            s = Screen(name="settings")
            s.add_widget(settings)
            self.sm.add_widget(s)
        self.sm.transition.direction = "left"
        self.sm.current = "settings"

    def build_settings(self, settings):
        settings.add_json_panel("Chess", self.config, "settings.json")

    def close_settings(self, *largs):
        if self.sm.current == "settings":
            self.sm.transition.direction = "right"
            self.sm.current = "menu"


if __name__ == "__main__":
    ChessApp().run()
