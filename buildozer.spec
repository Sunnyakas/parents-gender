[app]

# (str) Title of your application
title = Parents Gender

# (str) Package name
package.name = parentsgender

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = ./

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*, images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directory names to not include
# source.exclude_dirs = tests, bin, __pycache__

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license, images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Custom source folders for requirements
# requirements.pip = 

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 30

# (str) Android NDK version to use
# android.ndk = 23b

# (int) Android NDK API to use
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path = 

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
# android.add_src =

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) List of Java .jar files to add to the android project (can be java or a
# directory containing the files)
# android.add_jar =

# (list) List of Java .aar files to add to the android project (can be aar or a
# directory containing the files)
# android.add_aar =

# (list) List of gradle dependencies to add to the android project
# android.gradle_dependencies =

# (list) List of static library files to add to the android project
# android.add_static_lib =

# (list) List of dependencies to add to the android project
# android.add_dep =

# (str) python-for-android branch to use, if not master, useful to try
# not yet merged features.
# android.p4a_branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
# android.p4a_source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# android.p4a_local_recipes = 

# (str) The directory in which python-for-android should store downloaded files
# android.p4a_cache_dir = 

# (bool) If True, recompiles the python-for-android bootstrap even if the
# bootstrap has already been compiled for the specified API.
# android.recompile_bootstrap = False

# (str) python-for-android branch to use, if not stable, useful to try
# not yet merged features.
# android.p4a_branch = master

# (str) Android NDK directory to use (if empty, it will be automatically downloaded.)
# android.ndk_path = 

# (str) Android SDK directory to use (if empty, it will be automatically downloaded.)
# android.sdk_path = 

# (str) ANT directory to use (if empty, it will be automatically downloaded.)
# android.ant_path = 

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
# android.add_src =

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) List of Java .jar files to add to the android project (can be java or a
# directory containing the files)
# android.add_jar =

# (list) List of Java .aar files to add to the android project (can be aar or a
# directory containing the files)
# android.add_aar =

# (list) List of gradle dependencies to add to the android project
# android.gradle_dependencies =

# (list) List of static library files to add to the android project
# android.add_static_lib =

# (list) List of dependencies to add to the android project
# android.add_dep =

# (str) python-for-android branch to use, if not master, useful to try
# not yet merged features.
# android.p4a_branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
# android.p4a_source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# android.p4a_local_recipes = 

# (str) The directory in which python-for-android should store downloaded files
# android.p4a_cache_dir = 

# (bool) If True, recompiles the python-for-android bootstrap even if the
# bootstrap has already been compiled for the specified API.
# android.recompile_bootstrap = False

#
# iOS specific
#

# (str) iOS application name
# ios.appname = Parents Gender

# (str) iOS bundle identifier
# ios.bundle = org.example.parentsgender

# (str) iOS version
# ios.version = 0.1

# (str) iOS kivy version
# ios.kivy_version = 1.9.1

# (str) iOS required device
# ios.require_device = iphone

# (str) iOS deployment target
# ios.deployment_target = 9.0

# (list) iOS frameworks to add
# ios.frameworks = 

# (list) iOS plist keys
# ios.plist_keys = 

# (str) iOS team id (if you use Apple Developer Program)
# ios.team_id = 

# (str) iOS provisioning profile
# ios.provisioning_profile = 

# (str) iOS code signing identity
# ios.codesign_identity = 

# (str) iOS entitlements file
# ios.entitlements_file = 

# (str) iOS app store connect api key
# ios.api_key = 

# (str) iOS app store connect api issuer
# ios.api_issuer = 

# (str) iOS app store connect api key id
# ios.api_key_id = 

# (str) iOS app store connect api key file
# ios.api_key_file = 

# (bool) If True, then use the ios api key for code signing
# ios.use_api_key_for_code_sign = False

# (bool) If True, then use the ios api key for provisioning profile
# ios.use_api_key_for_provisioning_profile = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (bool) Enable platform dependency check
# check_dependencies = True

# (str) Path to the Android SDK
# android_sdk = 

# (str) Path to the Android NDK
# android_ndk = 

# (str) Path to the ANT
# android_ant = 

# (bool) If True, then use the android SDK from the system
# android.use_system_sdk = False

# (str) Path to the Java JDK
# java_jdk = 

# (list) List of additional Java JDK paths to add to the build
# java_jdk_paths = 

# (str) Path to the Java (javac)
# javac = 

# (str) Path to the Java (jar)
# jar = 

# (str) Path to the Java (keytool)
# keytool = 

# (str) Path to the Java (jarsigner)
# jarsigner = 

# (str) Path to the Android debug keystore
# android_debug_keystore = 

# (bool) If True, then use the Android debug keystore from the system
# android.use_system_debug_keystore = False

# (str) Path to the Android release keystore
# android_release_keystore = 

# (str) Alias for the Android release keystore
# android_release_alias = 

# (str) Password for the Android release keystore
# android_release_password = 

# (str) Password for the Android release keystore alias
# android_release_alias_password = 

# (str) Path to the Android debug keystore
# android_debug_keystore = 

# (str) Alias for the Android debug keystore
# android_debug_alias = 

# (str) Password for the Android debug keystore
# android_debug_password = 

# (str) Password for the Android debug keystore alias
# android_debug_alias_password = 

# (bool) If True, then use the Android debug keystore from the system
# android.use_system_debug_keystore = False

# (str) Path to the Android release keystore
# android_release_keystore = 

# (str) Alias for the Android release keystore
# android_release_alias = 

# (str) Password for the Android release keystore
# android_release_password = 

# (str) Password for the Android release keystore alias
# android_release_alias_password =
