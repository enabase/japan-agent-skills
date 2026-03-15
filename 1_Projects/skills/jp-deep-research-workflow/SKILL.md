---
name: jp-deep-research-workflow
description: |
  ユーザーとAIエージェントによる「Deep Research 連携によるAgent Skills開発ワークフロー」を
  実行・ガイドするスキル。ユーザーが「ディープリサーチでスキルを作りたい」「高度なリサーチに基づくスキル開発」
  「Deep Researchワークフローを開始して」「専門知識を入れたい」と言及した場合に必ずこのスキルを使用すること。
  トピックの決定から、Deep Research用プロンプトの自動生成、調査結果の取り込み、
  そして最終的なスキルファイルの出力までを一元管理する。
license: Apache-2.0
metadata:
  author: enabase
  version: "1.0"
  language: ja
  category: developer-tools
---

# Deep Research Collaboration Workflow

このスキルは、AIエージェントと人間（ユーザー）が協力し、外部の強力な Deep Research ツール（OpenAI O3-mini / ChatGPT Deep Research, Gemini Advanced 等）の調査能力を活用して、最高品質かつ専門知識（ドメイン知識）に基づいた Agent Skills を開発するための「メタ・ワークフロー」です。

## ワークフロー

### Step 1: トピックの決定とプロンプト策定（Agent側のタスク）
1. ユーザーから「作成したいスキルのテーマ（例：下請法チェッカー）」をヒアリングする。
2. そのテーマにおいて、AIエージェントが論理的に判定・動作するために必要な「専門知識の要件」を洗い出す。
3. 洗い出した要件をベースに、**外部のDeep Researchツールに入力するための「完璧なリサーチ用プロンプト」**を生成し、ユーザーに提示する。

**【リサーチ用プロンプトに必ず含めるべき要件】**
- 法定要件やマトリクス票（表形式での出力指示）
- エッジケースと例外規定
- AIが機械的に判定するための具体的なチェック項目（判断基準）

### Step 2: Deep Research の実行（User側のタスク）
1. ユーザーは、Step 1で発行されたプロンプトをそのまま自身のDeep Researchツールに入力する。
2. 徹底的な調査結果（Markdownテキストやファイル）が出力されたら、その結果をこのチャットに貼り付ける、またはファイルとして提供する。
※ エージェントはユーザーからのデータ提供を待ちます。

### Step 3: リサーチ資料の解析とスキル仕様策定（Agent側のタスク）
1. ユーザーから提供されたDeep Researchの資料を徹底的に読み込む。
2. 以下を特定・抽出する：
   - スキルに組み込むべき主要なフレームワークやチェックリスト
   - 提供された表や判断ツリー（これは `references/*.md` に保存する候補となる）
   - 例外処理（Edge Cases）
3. `ag-skill-creator` のガイドラインに準拠し、新しいスキルの `name` と概要設計をユーザーに提案し、合意形成を図る。

### Step 4: スキル実装（Agent側のタスク）
1. 合意した設計に基づき、`1_Projects/skills/{skill-name}/` に新しいスキルディレクトリを作成する。
2. 以下の構成でファイルを出力する。
   - `SKILL.md` (500行以内)
   - `evals/evals.json` (テストケース2件以上。Deep Research内の具体例を利用する)
   - `references/...` (リサーチ内で得た巨大な知識体系や表データ)

### Step 5: 検証とデプロイ（Agent側のタスク）
1. 作成後、必ず `python 3_Resources/spec/validate_skills.py 1_Projects/skills` を実行し、公式仕様（Agent Skills Specification）に準拠しているか確認する。
2. 全てのテストをパスしたら、ユーザーに報告し、Gitでのコミット・プッシュの許可を求める。

## Examples

**Example 1: ワークフローの起票**
Input: 「Deep Researchワークフローで下請法チェッカーを作りたい」
Output: 「承知しました。下請法チェッカーを作成するためのDeep Research用プロンプトを生成します...」

## Edge Cases

- **リサーチデータが不十分**: ユーザーから渡されたテキストに判定基準（マトリクス等）が含まれていない場合、再度プロンプトを生成して再調査を促す。
- **データが巨大すぎる**: 500行に収まらない場合は、ルールセットを複数の `references/*.md` ファイル群に分割してロードさせる。

## Guidelines
- 当スキルの最大の価値は「人間が外部から調達してきた非常に濃いドメイン知識」を取りこぼすことなく、Agent Skillsのプロンプト（Progressive Disclosure構造など）として体系化することにあります。
- 情報量が多い場合は、絶対に一度に `SKILL.md` へ詰め込まず、`references/` フォルダを積極的に活用（ファイル分割）してください。
- エージェント自身が中途半端にウェブ検索するのではなく、ユーザーのDeep Research結果を完全な「真実（Source of Truth）」として扱って設計します。
