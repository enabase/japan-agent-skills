# Agent Skills 公式仕様サマリー

> ソース: https://agentskills.io/specification
> 最終確認: 2026-03-15

## ディレクトリ構成

```
skill-name/
├── SKILL.md          # 必須: メタデータ + 指示
├── scripts/          # オプション: 実行可能コード
├── references/       # オプション: ドキュメント
├── assets/           # オプション: テンプレート、リソース
└── evals/            # オプション: テストケース
    └── evals.json
```

## SKILL.md フォーマット

### フロントマター（必須）

```yaml
---
name: skill-name          # 1-64文字、小文字英数字+ハイフン
description: |            # 1-1024文字
  何をするか + いつ使うべきか。
  キーワードを含めて発見されやすく。
license: Apache-2.0       # オプション
compatibility: |          # オプション（1-500文字）
  Designed for Claude Code (or similar products)
metadata:                 # オプション
  author: enabase
  version: "1.0"
---
```

### name ルール
- 小文字英数字(a-z)とハイフン(-)のみ
- ハイフンで始まる・終わることは不可
- 連続ハイフン(--)は不可
- 親ディレクトリ名と一致必須

### description ベストプラクティス
- 「何をするか」と「いつ使うか」の両方を含める
- 少し「pushy」に（積極的にトリガーされるように）
- 具体的なキーワードを含める

### 本文
- 500行以下推奨
- 命令形で書く
- 入出力例を含める
- エッジケースを記述

## Progressive Disclosure（3層構造）

1. **メタデータ（~100トークン）**: name + description → 常時ロード
2. **本体（<5000トークン推奨）**: SKILL.md body → スキル発動時ロード
3. **リソース（必要時）**: scripts/, references/, assets/ → 要求時ロード

## テストケース

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "テスト用プロンプト",
      "expected_output": "期待される出力の説明",
      "files": []
    }
  ]
}
```
