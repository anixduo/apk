#define BOOTSTRAP "sdl2"
#define IS_SDL2 1
#define IS_SDL3 0
#define PY2 0
#define ANDROID_LIBS_DIR "/workspaces/apk/.buildozer/android/platform/build-armeabi-v7a_arm64-v8a/build/libs_collections/frostmartchecker/armeabi-v7a:/workspaces/apk/.buildozer/android/platform/build-armeabi-v7a_arm64-v8a/build/bootstrap_builds/sdl2/obj/local/armeabi-v7a"
#define JAVA_NAMESPACE "org.kivy.android"
#define JNI_NAMESPACE "org/kivy/android"
#define ACTIVITY_CLASS_NAME "org.kivy.android.PythonActivity"
#define ACTIVITY_CLASS_NAMESPACE "org/kivy/android/PythonActivity"
#define SERVICE_CLASS_NAME "org.kivy.android.PythonService"
JNIEnv *SDL_AndroidGetJNIEnv(void);
#define SDL_ANDROID_GetJNIEnv SDL_AndroidGetJNIEnv
