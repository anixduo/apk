[app]
title = Frost Mart Trial Checker
package.name = frostmartchecker
package.domain = com.frostmart
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3,json
version = 1.0.0
requirements = python3,kivy==2.1.0,kivymd==1.1.1,requests==2.28.2,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 26c
android.wakelock = True
android.icon = assets/icons/app_icon.png
android.presplash = assets/icons/splash_logo.png
android.allow_backup = True
android.logcat_filters = *:S python:D
android.debug = 1
android.copy_libs = 1
android.arch = armeabi-v7a, arm64-v8a
android.app_theme = @android:style/Theme.Material.Light.NoActionBar
[buildozer]
log_level = 2
warn_on_root = 1
p4a.branch = master
