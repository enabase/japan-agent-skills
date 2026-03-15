---
name: ag-skill-creator
description: |
  japan-agent-skills プロジェクト専用のスキル作成エージェントスキル。
  公式のAgent Skills仕様および当プロジェクトのPARAメソッドに完全に準拠した
  スキルディレクトリ（SKILL.md, evals.json, references等）を自動構築し、
  ローカルのバリデーションツールで品質を担保する。
  ユーザーが「新しいスキルを作って」「スキルを作成」「skill-creator」
  「Agent Skillsの開発」と言及した場合にこのスキルを使用すること。
license: Apache-2.0
metadata:
  author: enabase
  version: "1.0"
  language: ja
  category: developer-tools
---

# Antigravity Skill Creator (Japan Agent Skills Optimized)

このスキルは、あなた（AIエージェント）に `japan-agent-skills` プロジェクト内での正しいAgent Skillsの作り方を教えます。以下のワークフローに厳密に従って新しいスキルを作成してください。

## ワークフロー

### Step 1: 要件定義と仕様策定 (Capture Intent)
ユーザーと対話し、以下の情報を確定させます。
1. **スキルの目的**: 何を解決するスキルか？
2. **トリガー条件**: ユーザーがどう言ったときに発動すべきか？（description用）
3. **ターゲット**: 誰が使うのか？（日本のSME、エンジニア、経理等）
4. **名前**: `name`（小文字英数字とハイフンのみ、1-64文字。例: `jp-example-skill`）

### Step 2: PARAメソッドに基づく構造の初期化
定義したスキル名を用いて、`1_Projects/skills/` ディレクトリ直下にフォルダを作成し、必須ファイルを用意します。
必ず `3_Resources/templates/skill-template/` のテンプレートをコピーまたはベースにして作成してください。

作成すべき構造構成：
```
1_Projects/skills/[skill-name]/
├── SKILL.md                  # 必須（500行以内）
├── evals/
│   └── evals.json            # 必須（テストケース2つ以上）
└── references/               # 推奨（補足資料、長文テンプレート等）
```

### Step 3: SKILL.md の執筆 (Progressive Disclosure)
以下のルールを**厳守**して `SKILL.md` を執筆します。

- **フロントマター（YAML）**: `name`と`description`は必須。`description`は「何をするか」と「いつ発動するか」を含め、キーワードを豊富に入れること（Pushyであること）。
- **命令形（Imperative）**: AIエージェントに向けた指示は明確な命令形で記述する。
- **ファイル分割**: `SKILL.md` 本体は必ず500行以内に収める。長文のテンプレートや参考資料は `references/*.md` に分離し、`SKILL.md` からリンクを張る。
- **必須セクション**:
  - `## ワークフロー` または `## Instructions`
  - `## Examples`（具体的なInput/Output例）
  - `## Edge Cases`（エッジケースのハンドリング方法）
  - `## Guidelines`（全般的なルール）

### Step 4: テストケースの作成 (evals.json)
スキルを実行する際の具体的なシナリオを `evals/evals.json` に少なくとも2つ作成します。
（`3_Resources/templates/skill-template/evals/evals.json` のフォーマットに従う）

### Step 5: ローカルバリデーション
スキルファイルの作成が完了したら、必ず以下のコマンドを実行して公式仕様に準拠しているか確認します。
```bash
python 3_Resources/spec/validate_skills.py 1_Projects/skills
```
⚠️ エラーが出た場合は、指摘事項を自律的に修正し、全項目PASSするまで繰り返します。

### Step 6: Gitへのコミット
バリデーションを通過したら、ユーザーに報告し、Gitへコミット・プッシュする許可を取ります。

## Examples

**Example 1: スキル作成の開始**
Input: 「jp-sales-emailスキルを作って」
Output: 「承知しました。まずは要件定義から始めます。ターゲットと送付の目的を教えてください。」

## Guidelines
- 常に `3_Resources/spec/AGENT_SKILLS_SPEC_SUMMARY.md` の仕様を念頭に置いて作成してください。
- 作成を急がず、特に「要件定義（Step 1）」でのユーザーとのすり合わせを最重要視してください。
- ユーザーから Deep Research の資料が提供された場合は、それを最優先の情報源として活用し、正確な知識をエッジケースやガイドラインに組み込んでください。
