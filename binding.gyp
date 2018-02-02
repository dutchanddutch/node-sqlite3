{
  "includes": [ "deps/common-sqlite.gypi" ],
  "targets": [
    {
      "target_name": "<(module_name)",
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "libraries": [ "-lsqlite3" ],
      "sources": [
        "src/database.cc",
        "src/node_sqlite3.cc",
        "src/statement.cc"
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
          {
            "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
            "destination": "<(module_path)"
          }
      ]
    }
  ]
}
