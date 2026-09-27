"""Blenderで動作確認用の軽量テストモデルを生成するスクリプト。

Blenderの「Scripting」タブのPythonコンソール、または
`blender --background --python scripts/create_test_model.py`
のようにコマンドラインから実行する。

生成するもの:
    - 立方体(Cube)を1つ
    - シンプルな赤色マテリアルを割り当て
    - 出力先を指定すると .glb でエクスポートする(任意)

MCP(Model Context Protocol)経由でBlenderを操作するツール
(例: blender-mcp)からも、このスクリプトのロジックをそのまま
`bpy` 経由で呼び出して利用できる。
"""

from __future__ import annotations

import sys

import bpy


def clear_scene() -> None:
    """シーン内の全オブジェクトを削除する。"""
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def create_test_cube(name: str = "TestCube", size: float = 2.0) -> bpy.types.Object:
    """テスト用の立方体を作成して返す。"""
    bpy.ops.mesh.primitive_cube_add(size=size, location=(0.0, 0.0, 0.0))
    cube = bpy.context.active_object
    cube.name = name
    return cube


def assign_red_material(obj: bpy.types.Object, name: str = "TestRed") -> bpy.types.Material:
    """オブジェクトにシンプルな赤色マテリアルを割り当てる。"""
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    principled = material.node_tree.nodes.get("Principled BSDF")
    if principled is not None:
        principled.inputs["Base Color"].default_value = (0.8, 0.05, 0.05, 1.0)

    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)

    return material


def export_glb(filepath: str) -> None:
    """シーンを .glb としてエクスポートする(任意)。"""
    bpy.ops.export_scene.gltf(filepath=filepath, export_format="GLB")


def main(export_path: str | None = None) -> None:
    clear_scene()
    cube = create_test_cube()
    assign_red_material(cube)

    if export_path:
        export_glb(export_path)
        print(f"[create_test_model] エクスポート完了: {export_path}")
    else:
        print("[create_test_model] シーン内にテストモデルを生成しました。")


if __name__ == "__main__":
    # `blender --background --python scripts/create_test_model.py -- output.glb`
    # のように `--` の後ろに出力パスを渡すとエクスポートも行う。
    argv = sys.argv
    export_arg: str | None = None
    if "--" in argv:
        after = argv[argv.index("--") + 1 :]
        if after:
            export_arg = after[0]

    main(export_arg)
