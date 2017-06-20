AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'basalt'
BUILD_TYPE = 'rocky'
BUNDLE_BIN_DIR = 'basalt'
BUNDLE_NAME = 'stars.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['basalt']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = []
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}
MESSAGE_KEYS_DEFINITION = '/Users/thomas/Documents/Develop/Pebble/stars/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/thomas/Documents/Develop/Pebble/stars/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/thomas/Documents/Develop/Pebble/stars/build/js/message_keys.json'
NODE = '/usr/local/bin/node'
NODE_PATH = '/Users/thomas/Library/Application Support/Pebble SDK/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/Users/thomas/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/thomas/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/basalt'
PEBBLE_SDK_ROOT = '/Users/thomas/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['basalt', 'color', 'rect', 'mic', 'strap', 'strappower', 'compass', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'basalt', 'BUNDLE_BIN_DIR': 'basalt', 'BUILD_DIR': 'basalt', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'basalt'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}, u'sdkVersion': u'3', u'projectType': u'rocky', u'uuid': u'c5591da1-15c4-4f91-9ba7-337c09c05ecd', 'messageKeys': {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}, 'companyName': u'\u4f50\u4f2f\u697d', u'enableMultiJS': True, u'watchapp': {u'watchface': True}, 'versionLabel': u'1.0', 'longName': u'Stars', u'displayName': u'Stars', 'shortName': u'Stars', u'main': {u'rockyjs': u'src/rocky/index.js'}, u'resources': {u'media': []}, 'name': u'Stars'}
REQUESTED_PLATFORMS = []
RESOURCES_JSON = []
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['emery', 'diorite', 'chalk', 'basalt']
TIMESTAMP = 1497923625
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/Users/thomas/Library/Application Support/Pebble SDK/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
