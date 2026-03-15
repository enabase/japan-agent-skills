# 🇯🇵 Japan Agent Skills

日本語ビジネス自動化に特化したAgent Skillsコレクション。

## プロジェクト概要

MCP Market / Agent Skills エコシステム向けに、日本語圏のビジネスユーザーが直面する
固有の課題を AI エージェントで解決するスキルセットを開発・販売するプロジェクトです。

## ディレクトリ構成（PARA メソッド）

```
スキルフォルダ/
├── 1_Projects/          # 現在アクティブなスキル開発プロジェクト
│   └── skills/          # Agent Skills 本体（公式仕様準拠）
│       ├── jp-business-email/
│       ├── jp-meeting-minutes/
│       └── jp-invoice-checker/
│
├── 2_Areas/             # 継続的に管理する領域
│   ├── marketing/       # マーケティング素材・戦略
│   ├── analytics/       # KPI・ダウンロード数トラッキング
│   └── quality/         # 品質管理・テスト基準
│
├── 3_Resources/         # 参照用リソース・テンプレート
│   ├── spec/            # Agent Skills 公式仕様
│   ├── templates/       # スキル作成テンプレート
│   └── research/        # 市場調査・競合分析
│
└── 4_Archive/           # 完了・非アクティブなアイテム
```

## スキル一覧

| スキル名 | 状態 | カテゴリ |
|---|---|---|
| jp-business-email | 🟢 開発中 | 生産性 |
| jp-meeting-minutes | 🟢 開発中 | 生産性 |
| jp-invoice-checker | 🟢 開発中 | ビジネスコンプライアンス |

## 技術仕様

- **フォーマット**: [Agent Skills Specification](https://agentskills.io/specification)
- **ライセンス**: Apache-2.0
- **対応プラットフォーム**: Claude Code, Claude.ai, Cursor, GitHub Copilot

## クイックスタート

```bash
# Skillfish CLI でインストール
npx skillfish add enabase/japan-agent-skills jp-business-email
```
