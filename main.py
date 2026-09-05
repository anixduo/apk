"""
Frost Mart Trial Checker - Professional Discord Token Checker
Developer: Frosty (@seller.wave)
Discord: https://discord.gg/Tdkh9cTQmG
Theme: Purple ❄️ Red 🔴 Yellow 🌟
Icons: Material Design Icons
Sound: MP3 Format
"""

import os
import json
import threading
import time
import random
from datetime import datetime
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem, ThreeLineListItem, IconListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.image import MDImage
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.divider import MDDivider
import requests

# ============== SOUND PLAYER (MP3 SUPPORT) ==============
try:
    from kivy.core.audio import SoundLoader
    SOUND_ENABLED = True
except:
    SOUND_ENABLED = False

class SoundManager:
    """Handles MP3 sound effects for the app"""
    
    SOUNDS = {
        'success': 'assets/sounds/success.mp3',
        'nitro': 'assets/sounds/nitro.mp3',
        'error': 'assets/sounds/error.mp3',
        'click': 'assets/sounds/click.mp3',
        'start': 'assets/sounds/start.mp3',
        'trial': 'assets/sounds/trial.mp3',
    }
    
    @staticmethod
    def play(sound_name):
        """Play a sound by name"""
        if not SOUND_ENABLED:
            return
        
        try:
            sound_path = SoundManager.SOUNDS.get(sound_name)
            if sound_path and os.path.exists(sound_path):
                sound = SoundLoader.load(sound_path)
                if sound:
                    sound.volume = 0.8  # 80% volume
                    sound.play()
        except Exception as e:
            pass  # Silent fail if sound not found

# ============== THEME COLORS ==============
COLORS = {
    'primary': '#7B2FBE',
    'primary_dark': '#4A148C',
    'primary_light': '#B39DDB',
    'accent': '#FF1744',
    'secondary': '#FFD600',
    'bg_dark': '#121212',
    'bg_card': '#1E1E2E',
    'text_primary': '#FFFFFF',
    'text_secondary': '#9E9E9E',
    'success': '#00E676',
    'error': '#FF1744',
    'warning': '#FFD600',
    'surface': '#2A2A3A',
}

if platform == 'win' or platform == 'linux':
    Window.size = (360, 720)

# ============== KV LAYOUT ==============
KV = '''
<StatCard@MDCard>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(90)
    padding: dp(8)
    radius: [dp(12)]
    md_bg_color: app.theme_cls.bg_card
    elevation: 2

<LogItem@OneLineListItem>:
    theme_text_color: 'Custom'
    text_color: 1, 1, 1, 0.9
    bg_color: 0.1, 0.1, 0.1, 0.3
    ripple_behavior: False

MDScreen:
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: toolbar
            title: "Frost Mart"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            right_action_items: [["account-circle-outline", lambda x: root.show_profile()]]
            elevation: 4
            specific_text_color: 1, 1, 1, 1
            md_bg_color: app.theme_cls.primary_color
        
        MDBottomNavigation:
            id: bottom_nav
            panel_color: app.theme_cls.primary_color
            selected_color_background: app.theme_cls.secondary_color
            text_color_active: 1, 1, 1, 1
            
            MDBottomNavigationItem:
                name: 'home'
                text: 'Home'
                icon: 'home-outline'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(12)
                    spacing: dp(10)
                    
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(90)
                        spacing: dp(8)
                        
                        StatCard:
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(2)
                                MDIcon:
                                    icon: 'account-multiple-outline'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.secondary_color
                                    font_size: '24sp'
                                MDLabel:
                                    id: token_count
                                    text: '0'
                                    font_style: 'H5'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_primary
                                MDLabel:
                                    text: 'TOKENS'
                                    font_style: 'Caption'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_secondary
                        
                        StatCard:
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(2)
                                MDIcon:
                                    icon: 'diamond-stone'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.accent_color
                                    font_size: '24sp'
                                MDLabel:
                                    id: nitro_count
                                    text: '0'
                                    font_style: 'H5'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_primary
                                MDLabel:
                                    text: 'NITRO'
                                    font_style: 'Caption'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_secondary
                        
                        StatCard:
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(2)
                                MDIcon:
                                    icon: 'gift-outline'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.success_color
                                    font_size: '24sp'
                                MDLabel:
                                    id: trial_count
                                    text: '0'
                                    font_style: 'H5'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_primary
                                MDLabel:
                                    text: 'TRIALS'
                                    font_style: 'Caption'
                                    halign: 'center'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_secondary
                    
                    MDCard:
                        orientation: 'vertical'
                        padding: dp(15)
                        spacing: dp(8)
                        radius: [dp(12)]
                        md_bg_color: app.theme_cls.bg_card
                        size_hint_y: None
                        height: dp(100)
                        elevation: 2
                        
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(4)
                            MDLabel:
                                text: 'SYSTEM STATUS'
                                font_style: 'Caption'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_secondary
                            MDBoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(8)
                                MDIcon:
                                    id: status_icon
                                    icon: 'snowflake'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.primary_color
                                MDLabel:
                                    id: status_text
                                    text: 'Ready for Action'
                                    font_style: 'H6'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_primary
                    
                    MDProgressBar:
                        id: progress_bar
                        value: 0
                        size_hint_y: None
                        height: dp(6)
                        color: app.theme_cls.primary_color
                    
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(48)
                        spacing: dp(8)
                        
                        MDRaisedButton:
                            text: 'START'
                            icon: 'play'
                            md_bg_color: app.theme_cls.accent_color
                            on_release: root.start_checking()
                            font_style: 'Button'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.5
                        
                        MDRaisedButton:
                            text: 'STOP'
                            icon: 'stop'
                            md_bg_color: app.theme_cls.error_color
                            on_release: root.stop_checking()
                            font_style: 'Button'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.5
                    
                    MDCard:
                        orientation: 'vertical'
                        padding: dp(12)
                        spacing: dp(4)
                        radius: [dp(12)]
                        md_bg_color: app.theme_cls.bg_card
                        elevation: 1
                        
                        MDBoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(8)
                            MDIcon:
                                icon: 'discord'
                                theme_text_color: 'Custom'
                                text_color: '#5865F2'
                            MDLabel:
                                text: 'Join Community'
                                font_style: 'Subtitle2'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_primary
                            Widget:
                            MDIcon:
                                icon: 'chevron-right'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_secondary
                        on_release: root.open_discord()
            
            MDBottomNavigationItem:
                name: 'tokens'
                text: 'Tokens'
                icon: 'format-list-bulleted'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(12)
                    spacing: dp(10)
                    
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(44)
                        spacing: dp(8)
                        
                        MDRaisedButton:
                            text: 'IMPORT'
                            icon: 'file-import-outline'
                            on_release: root.import_tokens()
                            font_style: 'Button'
                            size_hint_x: 0.33
                        
                        MDRaisedButton:
                            text: 'PASTE'
                            icon: 'content-paste'
                            on_release: root.show_paste_dialog()
                            font_style: 'Button'
                            size_hint_x: 0.33
                        
                        MDRaisedButton:
                            text: 'CLEAR'
                            icon: 'delete-outline'
                            md_bg_color: app.theme_cls.error_color
                            on_release: root.clear_tokens()
                            font_style: 'Button'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.34
                    
                    MDDivider:
                    
                    MDScrollView:
                        MDList:
                            id: token_list
                            padding: dp(4)
            
            MDBottomNavigationItem:
                name: 'console'
                text: 'Console'
                icon: 'console'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(12)
                    spacing: dp(10)
                    
                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(44)
                        spacing: dp(8)
                        
                        MDRaisedButton:
                            text: 'CLEAR'
                            icon: 'delete-outline'
                            md_bg_color: app.theme_cls.error_color
                            on_release: root.clear_console()
                            font_style: 'Button'
                            theme_text_color: 'Custom'
                            text_color: 1, 1, 1, 1
                            size_hint_x: 0.5
                        
                        MDRaisedButton:
                            text: 'EXPORT'
                            icon: 'export-variant'
                            on_release: root.export_results()
                            font_style: 'Button'
                            size_hint_x: 0.5
                    
                    MDDivider:
                    
                    MDScrollView:
                        MDList:
                            id: console_log
                            padding: dp(4)
            
            MDBottomNavigationItem:
                name: 'stats'
                text: 'Stats'
                icon: 'chart-bar'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(12)
                    spacing: dp(10)
                    
                    MDCard:
                        orientation: 'vertical'
                        padding: dp(15)
                        spacing: dp(5)
                        radius: [dp(12)]
                        md_bg_color: app.theme_cls.bg_card
                        elevation: 2
                        
                        MDGridLayout:
                            cols: 2
                            spacing: dp(8)
                            size_hint_y: None
                            height: dp(280)
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(4)
                                MDLabel:
                                    text: 'STATISTICS'
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_secondary
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(2)
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'check-circle-outline'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.success_color
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_valid
                                            text: 'Valid: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.success_color
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'close-circle-outline'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.error_color
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_invalid
                                            text: 'Invalid: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.error_color
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'diamond-stone'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.accent_color
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_nitro
                                            text: 'Nitro: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.accent_color
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'gift-outline'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.success_color
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_trial
                                            text: 'Trials: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.success_color
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'lock-outline'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.warning_color
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_locked
                                            text: 'Locked: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: app.theme_cls.warning_color
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: dp(4)
                                MDLabel:
                                    text: 'HUMANIZED STAGES'
                                    font_style: 'Caption'
                                    theme_text_color: 'Custom'
                                    text_color: app.theme_cls.text_secondary
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    spacing: dp(2)
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'check-decagram'
                                            theme_text_color: 'Custom'
                                            text_color: '#00E676'
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_stage3
                                            text: 'Stage 3: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: '#00E676'
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'progress-wrench'
                                            theme_text_color: 'Custom'
                                            text_color: '#FFD600'
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_stage2
                                            text: 'Stage 2: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: '#FFD600'
                                    
                                    MDBoxLayout:
                                        orientation: 'horizontal'
                                        spacing: dp(4)
                                        MDIcon:
                                            icon: 'alert-circle-outline'
                                            theme_text_color: 'Custom'
                                            text_color: '#FF1744'
                                            font_size: '16sp'
                                        MDLabel:
                                            id: stat_stage1
                                            text: 'Stage 1: 0'
                                            font_style: 'Body2'
                                            theme_text_color: 'Custom'
                                            text_color: '#FF1744'
                    
                    MDDivider:
                    
                    MDLabel:
                        text: 'Developer: Frosty (@seller.wave)'
                        font_style: 'Caption'
                        halign: 'center'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.text_secondary
            
            MDBottomNavigationItem:
                name: 'profile'
                text: 'Profile'
                icon: 'account-circle-outline'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(20)
                    spacing: dp(15)
                    
                    MDCard:
                        orientation: 'vertical'
                        padding: dp(25)
                        spacing: dp(10)
                        radius: [dp(20)]
                        md_bg_color: app.theme_cls.bg_card
                        size_hint_y: None
                        height: dp(300)
                        elevation: 4
                        
                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(8)
                            MDIcon:
                                icon: 'snowflake'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.primary_color
                                font_size: '56sp'
                                halign: 'center'
                            MDLabel:
                                text: 'FROST MART'
                                font_style: 'H5'
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_primary
                                bold: True
                            MDLabel:
                                text: 'Trial Checker v1.0'
                                font_style: 'Caption'
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_secondary
                            MDDivider:
                            MDLabel:
                                text: 'Developer: Frosty'
                                font_style: 'Subtitle2'
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.secondary_color
                            MDLabel:
                                text: '@seller.wave'
                                font_style: 'Caption'
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.text_secondary
                            MDLabel:
                                text: 'discord.gg/Tdkh9cTQmG'
                                font_style: 'Caption'
                                halign: 'center'
                                theme_text_color: 'Custom'
                                text_color: app.theme_cls.primary_light
                    
                    MDRaisedButton:
                        text: 'JOIN DISCORD'
                        icon: 'discord'
                        md_bg_color: '#5865F2'
                        on_release: root.open_discord()
                        font_style: 'Button'
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                    
                    MDFlatButton:
                        text: 'Contact: seller.wave'
                        icon: 'email-outline'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.text_secondary
'''

# ============== MAIN APP CLASS ==============
class FrostMartApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tokens = []
        self.valid_tokens = []
        self.nitro_tokens = []
        self.trial_tokens = []
        self.stage1 = 0
        self.stage2 = 0
        self.stage3 = 0
        self.valid = 0
        self.invalid = 0
        self.locked = 0
        self.nitro = 0
        self.trial = 0
        self.is_checking = False
        self.current_token_index = 0
        self.results = []
        
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.theme_style = 'Dark'
        
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen
    
    def on_start(self):
        self.add_console_log('Frost Mart Started', 'info')
        self.add_console_log('Developer: Frosty (@seller.wave)', 'info')
        self.add_console_log('System Ready', 'success')
        self.update_stats()
        SoundManager.play('start')
    
    # ============== TOKEN MANAGEMENT ==============
    def import_tokens(self):
        from kivy.uix.filechooser import FileChooserListView
        from kivy.uix.popup import Popup
        
        content = FileChooserListView()
        popup = Popup(
            title='Select Tokens File',
            content=content,
            size_hint=(0.9, 0.9)
        )
        
        def on_selection(instance, selection):
            if selection:
                self.load_tokens_from_file(selection[0])
                popup.dismiss()
        
        content.bind(on_selection=on_selection)
        popup.open()
        SoundManager.play('click')
    
    def load_tokens_from_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            added = 0
            for line in lines:
                token = line.strip()
                if token and not token.startswith('#'):
                    self.tokens.append(token)
                    self.add_token_to_list(token)
                    added += 1
            self.update_token_count()
            self.add_console_log(f'Loaded {added} tokens from file', 'success')
            SoundManager.play('success')
        except Exception as e:
            self.add_console_log(f'Error loading tokens: {str(e)}', 'error')
            SoundManager.play('error')
    
    def show_paste_dialog(self):
        dialog = MDDialog(
            title='Paste Tokens',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='token_input',
                    hint_text='Paste tokens here (one per line)',
                    multiline=True,
                    size_hint_y=None,
                    height=200,
                    mode='rectangle'
                ),
                orientation='vertical',
                padding=20,
                spacing=10
            ),
            buttons=[
                MDFlatButton(text='CANCEL', on_release=lambda x: dialog.dismiss()),
                MDRaisedButton(
                    text='ADD',
                    on_release=lambda x: self.add_pasted_tokens(
                        dialog.content_cls.ids.token_input.text
                    )
                )
            ]
        )
        dialog.open()
        SoundManager.play('click')
    
    def add_pasted_tokens(self, text):
        lines = text.strip().split('\n')
        added = 0
        for line in lines:
            token = line.strip()
            if token:
                self.tokens.append(token)
                self.add_token_to_list(token)
                added += 1
        self.update_token_count()
        self.add_console_log(f'Added {added} tokens from clipboard', 'success')
        SoundManager.play('success')
    
    def add_token_to_list(self, token):
        masked = token[:15] + '...' + token[-5:] if len(token) > 20 else token
        item = OneLineListItem(text=masked)
        self.screen.ids.token_list.add_widget(item)
    
    def clear_tokens(self):
        self.tokens.clear()
        self.valid_tokens.clear()
        self.nitro_tokens.clear()
        self.trial_tokens.clear()
        self.screen.ids.token_list.clear_widgets()
        self.update_token_count()
        self.add_console_log('All tokens cleared', 'info')
        SoundManager.play('click')
    
    def update_token_count(self):
        self.screen.ids.token_count.text = str(len(self.tokens))
    
    # ============== CHECKER ENGINE ==============
    def start_checking(self):
        if not self.tokens:
            Snackbar(text='No tokens loaded!').open()
            SoundManager.play('error')
            return
        
        if self.is_checking:
            return
        
        self.is_checking = True
        self.current_token_index = 0
        self.results = []
        self.screen.ids.status_text.text = 'Checking tokens...'
        self.screen.ids.status_icon.icon = 'loading'
        self.screen.ids.status_icon.text_color = COLORS['warning']
        self.screen.ids.progress_bar.value = 0
        self.add_console_log('Starting trial check...', 'info')
        SoundManager.play('start')
        
        threading.Thread(target=self.check_tokens, daemon=True).start()
    
    def check_tokens(self):
        total = len(self.tokens)
        
        for idx, token in enumerate(self.tokens):
            if not self.is_checking:
                break
            
            self.current_token_index = idx + 1
            progress = ((idx + 1) / total) * 100
            
            Clock.schedule_once(lambda dt, p=progress: self.update_progress(p), 0)
            
            result = self.check_single_token(token)
            self.results.append(result)
            
            Clock.schedule_once(lambda dt, r=result: self.process_result(r), 0)
            
            if result['nitro']:
                SoundManager.play('nitro')
            elif result['trial']:
                SoundManager.play('trial')
            elif result['status'] == 'valid':
                SoundManager.play('success')
            elif result['status'] in ['invalid', 'locked']:
                SoundManager.play('error')
            
            time.sleep(0.5 + random.random() * 0.5)
        
        self.is_checking = False
        Clock.schedule_once(lambda dt: self.finish_checking(), 0)
    
    def check_single_token(self, token):
        result = {
            'token': token,
            'status': 'valid',
            'nitro': False,
            'trial': False,
            'stage': 1,
            'type': 'Unclaimed',
            'error': None
        }
        
        try:
            token_only = token.split(':')[-1]
            headers = {'authorization': token_only}
            
            r = requests.get(
                'https://discord.com/api/v9/users/@me/guilds',
                headers=headers,
                timeout=10
            )
            
            if r.status_code == 401:
                result['status'] = 'invalid'
                return result
            elif r.status_code == 403:
                result['status'] = 'locked'
                return result
            elif r.status_code == 429:
                time.sleep(r.json().get('retry_after', 5))
                return self.check_single_token(token)
            
            r = requests.get(
                'https://discord.com/api/v9/users/@me',
                headers=headers,
                timeout=10
            )
            
            if r.status_code != 200:
                result['status'] = 'error'
                result['error'] = f'Status {r.status_code}'
                return result
            
            user_data = r.json()
            
            if user_data.get('email') and user_data.get('verified'):
                result['type'] = 'Email verified'
            if user_data.get('phone'):
                result['type'] = 'Fully verified' if result['type'] == 'Email verified' else 'Phone verified'
            
            # Humanized Stage
            avatar = user_data.get('avatar') is not None
            bio = bool(str(user_data.get('bio') or '').strip())
            
            pronouns = False
            user_id = user_data.get('id')
            if user_id:
                try:
                    r_profile = requests.get(
                        f'https://discord.com/api/v9/users/{user_id}/profile',
                        headers=headers,
                        timeout=10
                    )
                    if r_profile.status_code == 200:
                        prof_data = r_profile.json()
                        user_profile = prof_data.get('user_profile') or {}
                        pronouns = bool(str(user_profile.get('pronouns') or '').strip())
                except:
                    pass
            
            flags = user_data.get('flags', 0) or user_data.get('public_flags', 0) or 0
            hypesquad = bool(flags & (4 | 64 | 128 | 256))
            has_any = avatar or bio or pronouns or hypesquad
            
            if avatar and bio and pronouns and hypesquad:
                result['stage'] = 3
            elif not has_any:
                result['stage'] = 1
            else:
                result['stage'] = 2
            
            # Nitro Check
            try:
                r2 = requests.get(
                    'https://discord.com/api/v9/users/@me/billing/subscriptions',
                    headers=headers,
                    timeout=10
                )
                if r2.status_code == 200:
                    data = r2.json()
                    if isinstance(data, list) and data:
                        result['nitro'] = True
            except:
                pass
            
            # Trial Check
            try:
                headers_trial = headers.copy()
                headers_trial['content-type'] = 'application/json'
                
                r_trial = requests.post(
                    'https://discord.com/api/v9/users/@me/billing/user-offer',
                    headers=headers_trial,
                    json={},
                    timeout=10
                )
                if r_trial.status_code == 200:
                    t_data = r_trial.json()
                    user_trial_offer = t_data.get('user_trial_offer')
                    if isinstance(user_trial_offer, dict) and user_trial_offer.get('trial_id'):
                        result['trial'] = True
            except:
                pass
            
            result['status'] = 'valid'
            return result
            
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)[:50]
            return result
    
    def process_result(self, result):
        token = result['token']
        masked = token[:15] + '...' + token[-5:] if len(token) > 20 else token
        
        if result['status'] == 'valid':
            self.valid += 1
            self.valid_tokens.append(token)
            
            if result['stage'] == 3:
                self.stage3 += 1
            elif result['stage'] == 2:
                self.stage2 += 1
            else:
                self.stage1 += 1
            
            if result['nitro']:
                self.nitro += 1
                self.nitro_tokens.append(token)
                self.add_console_log(f'NITRO | {masked} | {result["type"]}', 'nitro')
            elif result['trial']:
                self.trial += 1
                self.trial_tokens.append(token)
                self.add_console_log(f'TRIAL | {masked} | {result["type"]}', 'trial')
            else:
                self.add_console_log(f'VALID | {masked} | {result["type"]}', 'valid')
                
        elif result['status'] == 'invalid':
            self.invalid += 1
            self.add_console_log(f'INVALID | {masked}', 'invalid')
            
        elif result['status'] == 'locked':
            self.locked += 1
            self.add_console_log(f'LOCKED | {masked}', 'locked')
            
        else:
            self.add_console_log(f'ERROR | {masked} | {result.get("error", "Unknown")}', 'error')
        
        self.update_stats()
        self.update_token_count()
    
    def update_stats(self):
        self.screen.ids.stat_valid.text = f'Valid: {self.valid}'
        self.screen.ids.stat_invalid.text = f'Invalid: {self.invalid}'
        self.screen.ids.stat_nitro.text = f'Nitro: {self.nitro}'
        self.screen.ids.stat_trial.text = f'Trials: {self.trial}'
        self.screen.ids.stat_locked.text = f'Locked: {self.locked}'
        self.screen.ids.stat_stage3.text = f'Stage 3: {self.stage3}'
        self.screen.ids.stat_stage2.text = f'Stage 2: {self.stage2}'
        self.screen.ids.stat_stage1.text = f'Stage 1: {self.stage1}'
        self.screen.ids.nitro_count.text = str(self.nitro)
        self.screen.ids.trial_count.text = str(self.trial)
    
    def update_progress(self, value):
        self.screen.ids.progress_bar.value = value
    
    def finish_checking(self):
        self.screen.ids.status_text.text = 'Check Complete'
        self.screen.ids.status_icon.icon = 'check-circle'
        self.screen.ids.status_icon.text_color = COLORS['success']
        self.screen.ids.progress_bar.value = 100
        self.add_console_log('Check complete!', 'success')
        SoundManager.play('success')
    
    def stop_checking(self):
        self.is_checking = False
        self.screen.ids.status_text.text = 'Stopped'
        self.screen.ids.status_icon.icon = 'stop-circle'
        self.add_console_log('Check stopped by user', 'info')
        SoundManager.play('click')
    
    # ============== CONSOLE ==============
    def add_console_log(self, message, type='info'):
        icons = {
            'valid': 'check-circle-outline',
            'invalid': 'close-circle-outline',
            'locked': 'lock-outline',
            'nitro': 'diamond-stone',
            'trial': 'gift-outline',
            'success': 'check-circle',
            'error': 'alert-circle-outline',
            'info': 'information-outline',
            'warning': 'alert-outline'
        }
        icon = icons.get(type, 'information-outline')
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_text = f'[{timestamp}] {message}'
        
        log_entry = LogItem(text=log_text)
        Clock.schedule_once(lambda dt, e=log_entry: self.screen.ids.console_log.add_widget(e), 0)
    
    def clear_console(self):
        self.screen.ids.console_log.clear_widgets()
        self.add_console_log('Console cleared', 'info')
        SoundManager.play('click')
    
    def export_results(self):
        data = {
            'app': 'Frost Mart Trial Checker',
            'developer': 'Frosty (@seller.wave)',
            'timestamp': datetime.now().isoformat(),
            'valid': self.valid,
            'invalid': self.invalid,
            'locked': self.locked,
            'nitro': self.nitro,
            'trial': self.trial,
            'stage1': self.stage1,
            'stage2': self.stage2,
            'stage3': self.stage3,
            'nitro_tokens': self.nitro_tokens,
            'trial_tokens': self.trial_tokens,
            'valid_tokens': self.valid_tokens
        }
        
        filename = f'frostmart_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            self.add_console_log(f'Results exported to {filename}', 'success')
            SoundManager.play('success')
        except Exception as e:
            self.add_console_log(f'Export failed: {str(e)}', 'error')
            SoundManager.play('error')
    
    # ============== UTILITY FUNCTIONS ==============
    def open_discord(self):
        import webbrowser
        webbrowser.open('https://discord.gg/Tdkh9cTQmG')
        self.add_console_log('Opening Discord community...', 'info')
        SoundManager.play('click')
    
    def show_profile(self):
        self.screen.ids.bottom_nav.switch_tab('profile')
        SoundManager.play('click')

# ============== RUN APP ==============
if __name__ == '__main__':
    FrostMartApp().run()