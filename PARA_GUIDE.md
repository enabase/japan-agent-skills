# PARA メソッド運用ガイド

## 概要

このプロジェクトは **PARA メソッド** に基づいて構造化されています。
どのAIエージェント（Claude, Gemini, ChatGPT, Cursor等）が操作しても
一貫した品質と管理が維持されるよう設計されています。

## 各フォルダの役割

### 1_Projects/ — アクティブなプロジェクト
- **中身**: 現在開発中のAgent Skills本体
- **ルール**: 完成したらすべてのファイルを `4_Archive/` に移動
- **命名規則**: `skills/{skill-name}/` の形式で公式仕様に準拠

### 2_Areas/ — 継続管理領域
- **marketing/**: SNS投稿テンプレート、ブログ記事案、ローンチ計画
- **analytics/**: ダウンロード数、売上、GitHub Stars等のKPIトラッキング
- **quality/**: テストケース基準、レビューチェックリスト、品質基準

### 3_Resources/ — 参照リソース
- **spec/**: Agent Skills公式仕様のローカルコピー
- **templates/**: SKILL.md テンプレート、evals.json テンプレート
- **research/**: 市場調査レポート、競合分析、トレンド情報

### 4_Archive/ — アーカイブ
- 完了したプロジェクト、使わなくなったリソースを保管
- 日付付きフォルダで整理: `YYYY-MM_プロジェクト名`

## AIエージェント向け指示

### スキル作成時
1. `3_Resources/templates/skill-template/` をコピーして開始
2. `3_Resources/spec/` 内の仕様を必ず参照
3. 完成したスキルは `1_Projects/skills/{name}/` に配置
4. テストケースは `1_Projects/skills/{name}/evals/` に保存

### 品質基準
- SKILL.md は500行以下
- description は「何をするか」+「いつ使うか」を含む
- name はディレクトリ名と完全一致（小文字・ハイフン区切り）
- 日本語の指示は明確で曖昧さがないこと
