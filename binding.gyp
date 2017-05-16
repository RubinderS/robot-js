{
  "conditions": [
    ["OS=='linux'", {"variables": {"target_platform": "linux"}}],
    ["OS=='win'", {"variables": {"target_platform": "win32"}}],
    ["OS=='mac'", {"variables": {"target_platform": "darwin"}}],
  ],
  "variables": {
    "target_module_version": "<!(node <(module_root_dir)/abi.js <(node_root_dir))",
  },
  "target_defaults": {
    "conditions": [
      ["OS=='linux'", {
        "libraries": [
          "-lrt",
          "-lX11",
          "-lXtst",
          "-lXinerama",
        ],
      }],
      ["OS=='win'", {
        "libraries": [
          "-lPsapi",
        ],
      }],
      ["OS=='mac'", {
        "libraries": [
          "-framework ApplicationServices",
          "-framework AppKit",
        ],
      }],
    ],
    "configurations": {
      "Debug": {
        "defines": [
          "DEBUG",
        ],
      },
      "Release": {
        "defines": [
          "NDEBUG",
        ],
      },
    },
  },
  "targets": [
    {
      "target_name": "librobot",
      "type": "static_library",
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1,
        },
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "OTHER_CPLUSPLUSFLAGS": [
          "-x objective-c++",
          "-Wno-sign-compare",
          "-Wno-unused-variable",
          "-Wno-missing-field-initializers",
        ],
      },
      "cflags_cc!": [
        "-fno-exceptions",
      ],
      "cflags_cc": [
        "-fexceptions",
        "-Wno-strict-aliasing",
        "-Wno-unused-variable",
        "-Wno-missing-field-initializers",
      ],
      "sources": [
        "src/Robot/Bounds.cc",
        "src/Robot/Clipboard.cc",
        "src/Robot/Color.cc",
        "src/Robot/Hash.cc",
        "src/Robot/Image.cc",
        "src/Robot/Keyboard.cc",
        "src/Robot/Memory.cc",
        "src/Robot/Module.cc",
        "src/Robot/Mouse.cc",
        "src/Robot/Point.cc",
        "src/Robot/Process.cc",
        "src/Robot/Range.cc",
        "src/Robot/Screen.cc",
        "src/Robot/Size.cc",
        "src/Robot/Timer.cc",
        "src/Robot/Window.cc",
      ],
    },
    {
      "target_name": "<(target_platform)-<(target_arch)-<(target_module_version)",
      "dependencies": ["librobot"],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1,
        },
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "OTHER_CPLUSPLUSFLAGS": [
          "-x objective-c++",
          "-Wno-sign-compare",
          "-Wno-unused-variable",
          "-Wno-missing-field-initializers",
        ],
      },
      "cflags_cc!": [
        "-fno-exceptions",
      ],
      "cflags_cc": [
        "-fexceptions",
        "-Wno-strict-aliasing",
        "-Wno-unused-variable",
        "-Wno-missing-field-initializers",
      ],
      "defines!": [
        "V8_DEPRECATION_WARNINGS=1",
      ],
      "include_dirs": [
        "src/Robot",
      ],
      "sources": [
        "src/Addon/Clipboard.cc",
        "src/Addon/Image.cc",
        "src/Addon/Keyboard.cc",
        "src/Addon/Memory.cc",
        "src/Addon/Mouse.cc",
        "src/Addon/Process.cc",
        "src/Addon/Robot.cc",
        "src/Addon/Screen.cc",
        "src/Addon/Window.cc",
      ],
    },
    {
      "target_name": "copy_binary",
      "type": "none",
      "dependencies": ["<(target_platform)-<(target_arch)-<(target_module_version)"],
      "copies": [
        {
          "files": ["<(PRODUCT_DIR)/<@(_dependencies).node"],
          "destination": "<(module_root_dir)/lib",
        },
      ],
    },
  ],
}