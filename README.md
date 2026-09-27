# inu

Blenderの動作確認用に、軽量なテストモデルを生成するスクリプトを置いています。

## 内容

- `scripts/create_test_model.py`
  - Blender上に赤いマテリアル付きの立方体を1つ生成するだけの、シンプルなテストスクリプトです。
  - MCP(Model Context Protocol)経由でBlenderを操作するツール(例: blender-mcp)から
    このスクリプトの関数を呼び出して、疎通確認用のモデル生成に使うことを想定しています。

## 使い方

### Blenderのスクリプティングタブから実行する場合

1. Blenderを起動し、「Scripting」タブを開く
2. `scripts/create_test_model.py` の内容を貼り付けて実行(Run Script)

### コマンドラインから実行する場合

```bash
blender --background --python scripts/create_test_model.py
```

出力先を指定して `.glb` としてエクスポートする場合:

```bash
blender --background --python scripts/create_test_model.py -- output.glb
```

### MCP経由で利用する場合

blender-mcpなどのBlender操作用MCPサーバーを使う場合は、Blender側でこのスクリプトを
実行させるか、`create_test_cube` / `assign_red_material` などの関数をMCPツールの
実装から直接呼び出してください。
