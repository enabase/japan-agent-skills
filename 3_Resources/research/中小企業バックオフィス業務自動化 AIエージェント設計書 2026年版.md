# 中小企業バックオフィス業務自動化 AIエージェント設計書 2026年版
**SaaS間転記作業を自動化するスクリプト/設定指示書 自動生成システム**

- バージョン：1.0
- 作成日：2026年3月
- 対象：従業員5〜100名規模の日本の中小企業

---

## 目次

1. [第1章：中小企業が抱える「手作業TOP20」ランキング](#第1章)
2. [第2章：自動化ツール完全比較（2026年版）](#第2章)
3. [第3章：頻出連携パターン「レシピ集」](#第3章)
4. [第4章：AIが「自動化指示書」を生成するためのフレームワーク](#第4章)
5. [第5章：セキュリティ・権限管理とよくあるトラブル](#第5章)
6. [附録A：ツール別料金比較一覧表](#附録A)
7. [附録B：参考リンク集](#附録B)

---

## エグゼクティブサマリー

日本の中小企業（従業員5〜100名）では、バックオフィス業務の多くが未だに手作業で行われており、1人あたり月平均40〜80時間もの転記・連携作業が発生しているとされる（経済産業省DXレポート2023）。

本設計書は、以下の5つの観点から中小企業のバックオフィス業務自動化を包括的に解説する：

1. **何を自動化すべきか**：工数・頻度・ROIの高い手作業TOP20の特定
2. **どのツールを使うか**：2026年時点の主要9ツールの詳細比較
3. **どう設定するか**：即実践できる8種の連携レシピ（コード付き）
4. **AIによる自動化指示書生成**：要件ヒアリング→ツール選定→設定書自動生成のフレームワーク
5. **安全に運用するか**：セキュリティ・法的注意事項・トラブル対策

---

<a name="第1章"></a>
## 第1章：中小企業が抱える「手作業TOP20」ランキング

### 1-1. 背景

日本の中小企業（従業員5〜100名）では、バックオフィス業務の多くが未だに手作業で行われており、1人あたり月平均40〜80時間もの転記・連携作業が発生しているとされる（経済産業省DXレポート2023）。

SaaSの導入が進む一方で、「SaaS同士が連携していない」という問題が深刻化しており、担当者がデータを手でコピーアンドペーストする「デジタルの手作業」が新たなボトルネックとなっている。

### 1-2. 手作業TOP20ランキング

| 順位 | 業務カテゴリ | 具体的な手作業内容 | 月間発生頻度 | 推定工数(時間/月) | 自動化可能性 | 推奨ツール |
|------|------------|-----------------|------------|----------------|------------|----------|
| 1位 | 経理 | 請求書PDFからfreee/マネーフォワード/弥生への手入力転記 | 週3〜5回 | 8〜15時間 | ★★★★★ | Yoom/Make/OCR連携 |
| 2位 | 人事 | 勤怠管理SaaS（KING OF TIME等）→給与計算ソフトへのCSVダウンロード→アップロード | 月2回 | 5〜10時間 | ★★★★☆ | Power Automate/GAS |
| 3位 | 営業 | 名刺スキャン→Sansan等→SalesforceやHubSpot、kintoneへの手動入力 | 日常的 | 5〜8時間 | ★★★★★ | Zapier/Yoom |
| 4位 | EC・在庫 | Shopify/BASE等の受注データ→在庫管理・出荷システムへの転記 | 日次 | 10〜20時間 | ★★★★★ | Make/Zapier |
| 5位 | カスタマーサポート | Gmailの問い合わせメール→ZendeskやFreshDeskへの手動チケット作成 | 日次 | 4〜8時間 | ★★★★★ | Zapier/Make |
| 6位 | データ集計 | 各SaaSからのデータをGoogleスプレッドシートに手動コピペして月次レポート作成 | 月1回 | 8〜16時間 | ★★★★☆ | GAS/Make |
| 7位 | 社内連絡 | 特定イベント発生時にSlack/Teams/Chatworkへのコピーアンドペーストや手動通知 | 日次 | 2〜4時間 | ★★★★★ | Zapier/Yoom |
| 8位 | 経理 | 経費精算データ（マネーフォワードExpense等）→承認後→会計仕訳への手動入力 | 月2回 | 3〜6時間 | ★★★★☆ | API連携/Yoom |
| 9位 | 人事・採用 | 求人媒体（Indeed/リクナビ等）の応募者情報→社内管理シートへの転記 | 日次 | 3〜5時間 | ★★★★☆ | GAS/Make |
| 10位 | 営業 | Googleフォームのお問い合わせ→CRM（kintone/HubSpot）への手入力 | 日次 | 2〜4時間 | ★★★★★ | GAS/Zapier |
| 11位 | 経理 | 銀行入出金データのダウンロード→会計ソフトへのCSVインポート | 月2回 | 2〜4時間 | ★★★★☆ | freee自動連携/API |
| 12位 | 営業 | 商談後の議事録作成→CRM/Notionへの手動入力 | 日次 | 3〜5時間 | ★★★☆☆ | AI文字起こし+Zapier |
| 13位 | 在庫 | 受注確認→倉庫担当者へのメール/FAX通知 | 日次 | 2〜3時間 | ★★★★★ | GAS/Zapier |
| 14位 | 社内総務 | 備品発注・申請のメール管理→承認フロー | 週1〜2回 | 2〜4時間 | ★★★★☆ | kintone/Power Automate |
| 15位 | HR | 入退社手続き→各SaaSアカウント手動作成・削除 | 月1〜2回 | 2〜4時間 | ★★★☆☆ | Yoom/SCIM連携 |
| 16位 | マーケ | Web広告データ（Google/Meta広告）→スプレッドシートへの手動転記 | 週1回 | 2〜3時間 | ★★★★★ | GAS API/Supermetrics |
| 17位 | 経理 | 紙/メール請求書の電子保存（電子帳簿保存法対応） | 月次 | 2〜4時間 | ★★★★☆ | freee/マネーフォワード OCR |
| 18位 | 営業 | 見積書作成→PDF化→メール送信 | 日次 | 1〜3時間 | ★★★★☆ | GAS/kintone帳票 |
| 19位 | カスタマー | FAQ対応のコピーアンドペースト返信 | 日次 | 3〜5時間 | ★★★☆☆ | ChatGPT+Zapier |
| 20位 | データ管理 | 複数部署のExcel/スプレッドシートのデータを統合してPivotテーブル作成 | 月1回 | 4〜8時間 | ★★★★☆ | GAS/Power Query |

### 1-3. 優先度マトリクス

自動化の優先度は以下のマトリクスで判断する：

```
高工数 × 高頻度 × 高自動化可能性 ＝ 最優先（1〜5位）
高工数 × 低頻度 × 高自動化可能性 ＝ 次点（6・11・17・20位）
低工数 × 高頻度 × 高自動化可能性 ＝ 積極推進（7・10・13・16位）
```

---

<a name="第2章"></a>
## 第2章：自動化ツール完全比較（2026年版）

### 2-1. ツール概要マップ

```
難易度(低)  ←────────────────────────────→  難易度(高)
              IFTTT → Yoom → Zapier → Make → Power Automate
                                              → GAS → n8n → Python
              ↑非エンジニア向け              ↑エンジニア向け
```

---

### 2-2. 各ツール詳細

#### (1) Zapier

| 項目 | 内容 |
|------|------|
| 種別 | クラウド型iPaaS（グローバル最大手） |
| 設立 | 2011年（米国） |
| **無料プラン** | **月100タスク、2ステップZapのみ** |
| 有料プラン | Professional $19.99/月〜、Team $69/月〜 |
| 連携アプリ数 | 8,500以上 |
| 日本語UI | △（一部日本語化、基本英語） |
| 日本語ドキュメント | ○（公式日本語ヘルプあり） |
| freee連携 | △（非公式または間接連携） |
| マネーフォワード連携 | △ |
| kintone連携 | ○（公式コネクタあり） |
| LINE連携 | △（LINE Notify経由） |
| 非エンジニア適性 | ★★★★★（最高水準のGUI） |
| 日本語コミュニティ | ★★★☆☆ |

**特徴・強み**
- 世界最大規模の連携アプリ数（8,500以上）
- AIを活用したZap自動生成機能（Copilot）
- 豊富なテンプレート集

**弱み・注意点**
- 国内SaaS（サイボウズOffice、Misoca等）は未対応の場合がある
- 無料プランは月100タスクと少ない
- 価格が上がるにつれて割高感

**向いている企業**
グローバルSaaS（Salesforce/HubSpot/Shopify/Slack）中心で英語に抵抗ない企業

---

#### (2) Make（旧Integromat）

| 項目 | 内容 |
|------|------|
| 種別 | クラウド型iPaaS（ビジュアルフロー型） |
| 設立 | 2012年（チェコ） |
| **無料プラン** | **月1,000オペレーション、2シナリオ** |
| 有料プラン | Core $10.59/月〜、Pro $18.82/月〜 |
| 連携アプリ数 | 1,800以上 |
| 日本語UI | ○（日本語対応あり） |
| freee連携 | ○ |
| マネーフォワード連携 | △ |
| kintone連携 | ○ |
| LINE連携 | ○（LINE Messaging API） |
| 非エンジニア適性 | ★★★★☆（ビジュアルフローが直感的） |
| 日本語コミュニティ | ★★★☆☆ |

**特徴・強み**
- ビジュアルフロー（キャンバス型）で複雑な処理が組みやすい
- Zapierと比較して安価
- エラーハンドリング・ロールバック機能が充実

**弱み・注意点**
- 「オペレーション」の概念が直感的でなく、コスト計算が難しい
- テクニカルな設定は英語ドキュメントが必要な場合あり

**向いている企業**
複雑なフロー設計が必要な企業、コスト重視の企業、Zapierからの乗り換え検討企業

---

#### (3) n8n

| 項目 | 内容 |
|------|------|
| 種別 | オープンソースiPaaS（セルフホスト可） |
| 設立 | 2019年（ドイツ） |
| **無料プラン** | **セルフホスト版は無制限** |
| クラウド有料プラン | Starter €20/月〜 |
| 連携アプリ数 | 400以上（カスタム可能） |
| 日本語UI | △（一部日本語） |
| 日本語ドキュメント | △（英語中心） |
| freee連携 | API経由でカスタム実装可 |
| kintone連携 | API経由でカスタム実装可 |
| LINE連携 | Webhookで実装可 |
| 非エンジニア適性 | ★★★☆☆（技術者向け） |
| 日本語コミュニティ | ★★☆☆☆ |

**特徴・強み**
- オープンソース＆セルフホスト可能（データが外部に出ない）
- コード記述可能でカスタマイズ性が最高水準
- 金融・官公庁系などセキュリティ要件が高い環境に適合

**弱み・注意点**
- エンジニア不在の企業には導入ハードル高
- セルフホストはサーバー管理コスト・脆弱性対応が必要
- 日本語情報が少ない

**向いている企業**
エンジニアが在籍する企業、セキュリティ要件が高くオンプレ希望の企業

---

#### (4) Google Apps Script（GAS）

| 項目 | 内容 |
|------|------|
| 種別 | スクリプト型自動化（Google Workspace内） |
| 費用 | **完全無料**（Google Workspaceアカウントで利用可） |
| 主な制限 | スクリプト実行時間6分/回、API呼び出し数制限（日次） |
| 日本語対応 | ◎ |
| Google連携 | ◎（Sheets/Docs/Drive/Gmail/Calendar/Forms完全対応） |
| freee連携 | ○（API経由） |
| kintone連携 | ○（API経由） |
| LINE連携 | ○（LINE Notify/Messaging API） |
| 非エンジニア適性 | ★★☆☆☆（JavaScript知識が必要） |
| 日本語コミュニティ | ★★★★★（Qiita/Zennに記事が豊富） |

**特徴・強み**
- Google Workspaceユーザーなら追加費用ゼロ
- Googleサービスとの連携は他ツールの追随を許さない
- 日本語の参考記事・コミュニティが最も充実

**弱み・注意点**
- JavaScriptの知識が必要（最低限の読み書きができること）
- 実行時間6分制限（長いバッチ処理には工夫が必要）
- 外部SaaS連携はAPIを自分で叩く必要がある

**向いている企業**
Google Workspace利用企業、コスト重視、技術に興味がある担当者がいる企業

---

#### (5) Power Automate（Microsoft）

| 項目 | 内容 |
|------|------|
| 種別 | クラウド型iPaaS（Microsoft 365連携最強） |
| **無料プラン** | **Microsoft 365プランに含まれる** |
| 有料プラン | Power Automate Premium $15/ユーザー/月 |
| 連携アプリ数 | 1,000以上（コネクタ） |
| 日本語UI | ◎（完全日本語） |
| 日本語ドキュメント | ◎ |
| Microsoft連携 | ◎（Teams/SharePoint/Excel/Outlook完全対応） |
| freee連携 | △（カスタムコネクタ経由） |
| kintone連携 | △（カスタムコネクタあり） |
| LINE連携 | ○（HTTPコネクタ経由） |
| 非エンジニア適性 | ★★★★☆ |
| 日本語コミュニティ | ★★★★☆ |

**特徴・強み**
- Microsoft 365ユーザーは追加費用なしで利用可能
- Teamsとの連携・承認フローが業界最強
- Power Automate Desktopでブラウザ/デスクトップ操作も自動化可能

**弱み・注意点**
- Microsoft以外のSaaSとの連携はカスタムコネクタが必要な場合あり
- UIが複雑で学習コストがかかる
- プレミアムコネクタは追加費用が発生

**向いている企業**
Microsoft 365利用企業、Office系業務が多い企業、Teamsが社内コミュニケーションの中心の企業

---

#### (6) IFTTT

| 項目 | 内容 |
|------|------|
| 種別 | シンプル連携サービス |
| **無料プラン** | **3アプレット（レシピ）まで** |
| 有料プラン | Pro $2.5/月〜、Pro+ $5/月〜 |
| 連携アプリ数 | 800以上 |
| 日本語UI | △（一部のみ） |
| freee連携 | ✕ |
| kintone連携 | ✕ |
| LINE連携 | ○（LINE公式対応） |
| 非エンジニア適性 | ★★★★★（最も簡単） |
| 日本語コミュニティ | ★★★☆☆ |

**特徴・強み**
- 圧倒的なシンプルさ（If This Then That）
- スマートホームデバイスとの連携が強い
- 個人ユーザーに人気

**弱み・注意点**
- 1対1の単純連携のみ（複雑なフロー不可）
- 無料プランが3アプレットと極めて少ない
- 業務SaaS（freee/kintone等）との連携が弱い

**向いている企業**
個人・超小規模事業者、シンプルな通知連携のみでよい企業

---

#### (7) Yoom（日本発iPaaS）⭐ 中小企業最推奨

| 項目 | 内容 |
|------|------|
| 種別 | クラウド型iPaaS（日本特化） |
| 運営 | Yoom株式会社（日本） |
| **無料プラン** | **月100タスク、フローボット5個** |
| パーソナルプラン | ¥2,400/月〜（1,000タスク/月、1名） |
| ミニプラン | ¥16,000/月〜（5,000タスク/月、20名） |
| チームプラン | ¥40,000/月〜（15,000タスク/月、100名） |
| サクセスプラン | ¥80,000/月〜（45,000タスク/月、無制限） |
| 連携アプリ数 | 500以上（日本SaaS特化） |
| 日本語UI | ◎（完全日本語） |
| 日本語サポート | ◎（チャット・Web会議） |
| freee連携 | ◎（公式対応） |
| マネーフォワード連携 | ◎（公式対応） |
| kintone連携 | ◎（公式対応） |
| LINE連携 | ◎（公式対応） |
| Chatwork連携 | ◎ |
| 非エンジニア適性 | ★★★★★ |
| 日本語コミュニティ | ★★★★★ |

**特徴・強み**
- 日本のSaaSに特化した最高水準の連携対応
- OCR機能内蔵（請求書の自動読み取りが可能）
- RPA・AI・OCRを1ツールで統合
- 完全日本語、日本語サポート

**弱み・注意点**
- グローバルSaaS（Salesforce等）との連携はZapierに劣る場合がある
- チームプラン以上は費用がかかる

**向いている企業**
日本SaaS中心の中小企業、非エンジニア担当者、コンプライアンス重視の企業

---

#### (8) Python + API直接連携

| 項目 | 内容 |
|------|------|
| 種別 | コード型カスタム自動化 |
| 費用 | Python無料（ホスティング費用別途：VPS月数百円〜） |
| 柔軟性 | ★★★★★ |
| 連携対象 | APIがあれば全SaaSに対応可能 |
| 非エンジニア適性 | ★☆☆☆☆（プログラミング必須） |
| 日本語コミュニティ | ◎（最大規模） |

**特徴・強み**
- 制限なしの完全カスタマイズ
- コスト最安（サーバー代のみ）
- 複雑なビジネスロジックも実装可能

**弱み・注意点**
- プログラミング知識が必須
- 保守・引き継ぎコストが高い
- エンジニア依存度が高い

**向いている企業**
エンジニアが在籍する企業、複雑なビジネスロジックが必要な企業

---

#### (9) ブラウザRPA（UiPath / Power Automate Desktop / Robocorp）

| 項目 | 内容 |
|------|------|
| 種別 | デスクトップRPA・ブラウザ自動化 |
| 主な用途 | APIが存在しないWebサービスの操作自動化 |
| UiPath | Community Edition（無料）、Enterprise（要問合せ） |
| Power Automate Desktop | Windows 10/11無料付属 |
| Robocorp | オープンソース（無料） |
| 非エンジニア適性 | ★★★☆☆（ローコード） |
| 日本語コミュニティ | ★★★★☆（UiPath日本コミュニティが活発） |

**特徴・強み**
- APIが公開されていないレガシーシステムにも対応
- 画面録画でロボット作成が可能
- 既存業務フローをほぼそのまま自動化できる

**弱み・注意点**
- SaaS側のUI変更で突然動作停止するリスク
- 保守コストが高い
- クラウドSaaSには過剰なケースが多い

**向いている企業**
レガシーWebシステムが多い企業、API非公開サービスへの対応が必要な企業

---

<a name="第3章"></a>
## 第3章：頻出連携パターン「レシピ集」

---

### パターン1：Googleフォーム回答 → Googleスプレッドシート → Slack通知

**概要**  
お問い合わせや申込みフォームの回答を自動でSlack通知する最もポピュラーなレシピ。

**推奨ツール**：Google Apps Script（無料）

#### トリガー設定

```javascript
// GASコード例：フォーム送信時にSlack通知
function onFormSubmit(e) {
  const responses = e.values;
  const timestamp = responses[0];
  const name = responses[1];
  const email = responses[2];
  const message = responses[3];

  // Slack Webhook URL（Properties Serviceで管理 ← 直書き禁止）
  const props = PropertiesService.getScriptProperties();
  const SLACK_WEBHOOK = props.getProperty('SLACK_WEBHOOK_URL');

  const payload = {
    text: `📨 新しいお問い合わせ\n名前：${name}\nメール：${email}\n内容：${message}\n受信時刻：${timestamp}`
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  };

  UrlFetchApp.fetch(SLACK_WEBHOOK, options);
}
```

#### セットアップ手順（5ステップ）

1. GASエディタを開く（スプレッドシート → 拡張機能 → Apps Script）
2. Slack Incoming Webhookを作成してURLを取得
3. GASのスクリプトプロパティにSLACK_WEBHOOK_URLを設定（直書き禁止）
4. フォーム送信時トリガーを設定（トリガー → 新規 → フォーム送信時）
5. テスト送信で動作確認

#### エラーハンドリング

```javascript
function onFormSubmit(e) {
  try {
    // メイン処理
    const props = PropertiesService.getScriptProperties();
    const SLACK_WEBHOOK = props.getProperty('SLACK_WEBHOOK_URL');
    // ... 処理 ...
    UrlFetchApp.fetch(SLACK_WEBHOOK, options);
  } catch(error) {
    Logger.log('Slack通知エラー: ' + error.message);
    // バックアップ：メール通知
    GmailApp.sendEmail(
      'admin@example.com',
      'Slack通知エラー発生',
      'エラー内容：' + error.message
    );
  }
}
```

---

### パターン2：Gmail受信 → 添付ファイル → Googleドライブ保存 → Slack通知

**推奨ツール**：Google Apps Script

#### コード例

```javascript
function saveAttachmentsFromGmail() {
  const props = PropertiesService.getScriptProperties();
  const FOLDER_ID = props.getProperty('DRIVE_FOLDER_ID');
  const SLACK_WEBHOOK = props.getProperty('SLACK_WEBHOOK_URL');

  // 「請求書」ラベルのある未処理メールを検索
  const threads = GmailApp.search('label:請求書 is:unread has:attachment');
  const folder = DriveApp.getFolderById(FOLDER_ID);

  threads.forEach(thread => {
    thread.getMessages().forEach(msg => {
      msg.getAttachments().forEach(att => {
        // ファイルをドライブに保存
        const file = folder.createFile(att);
        const fileUrl = file.getUrl();

        // Slack通知
        const payload = {
          text: `📎 請求書ファイル保存完了\nファイル名：${att.getName()}\nURL：${fileUrl}\n送信元：${msg.getFrom()}`
        };
        UrlFetchApp.fetch(SLACK_WEBHOOK, {
          method: 'post',
          contentType: 'application/json',
          payload: JSON.stringify(payload)
        });
      });
      msg.markRead();
    });
  });
}
// 時間ベーストリガー：毎時実行
```

#### エラーハンドリングの観点
- 添付ファイルサイズ上限（Driveの空き容量）チェック
- 重複ファイル名時の自動リネーム処理
- メール検索失敗時のログ記録

---

### パターン3：Googleスプレッドシートの新行追加 → freee請求書作成

**推奨ツール**：Yoom（ノーコード）またはGAS + freee API（コード型）

#### Yoomでの設定手順

1. Yoomにログイン → 「フローボット」 → 「+ 新しいフローボット」
2. トリガー選択：「Googleスプレッドシート」 → 「行が追加されたとき」
3. シートID・シート名を指定
4. アクション1：「freee」 → 「請求書を作成する」を追加
5. スプレッドシートの列データをfreeeの各フィールドにマッピング
   - A列（取引先名）→ freee「取引先」
   - B列（品目）→ freee「品目」
   - C列（金額）→ freee「単価」
6. テスト実行で確認

#### GAS + freee API版（上級者向け）

```javascript
function createFreeeInvoice(rowData) {
  const props = PropertiesService.getScriptProperties();
  const FREEE_ACCESS_TOKEN = props.getProperty('FREEE_ACCESS_TOKEN');
  const COMPANY_ID = props.getProperty('FREEE_COMPANY_ID');

  const invoiceData = {
    company_id: parseInt(COMPANY_ID),
    issue_date: rowData.issueDate,
    due_date: rowData.dueDate,
    invoice_status: 'draft',
    partner_name: rowData.partnerName,
    invoice_lines: [{
      name: rowData.itemName,
      quantity: rowData.quantity,
      unit_price: rowData.unitPrice,
      tax_code: 1  // 消費税10%
    }]
  };

  const response = UrlFetchApp.fetch(
    `https://api.freee.co.jp/api/1/invoices`,
    {
      method: 'post',
      headers: {
        'Authorization': `Bearer ${FREEE_ACCESS_TOKEN}`,
        'Content-Type': 'application/json'
      },
      payload: JSON.stringify(invoiceData)
    }
  );

  return JSON.parse(response.getContentText());
}
```

---

### パターン4：kintoneのレコード更新 → Chatwork通知

**推奨ツール**：Yoom（最推奨）またはkintone Webhook + GAS

#### kintone Webhookの設定

1. kintone管理画面 → アプリの設定 → Webhook
2. 「レコードの編集」のイベントを選択
3. Webhook URL（GAS Web App URLまたはYoomのURL）を設定

#### GAS Web App コード例

```javascript
// GAS Web App として公開（doPost関数）
function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  const record = data.record;

  const props = PropertiesService.getScriptProperties();
  const CHATWORK_TOKEN = props.getProperty('CHATWORK_TOKEN');
  const CHATWORK_ROOM_ID = props.getProperty('CHATWORK_ROOM_ID');

  const message = `[info][title]kintone レコード更新通知[/title]
アプリ：${data.app.name}
レコードID：${record.$id.value}
更新者：${data.updater ? data.updater.name : '不明'}
ステータス：${record.status ? record.status.value : '変更なし'}[/info]`;

  UrlFetchApp.fetch(
    `https://api.chatwork.com/v2/rooms/${CHATWORK_ROOM_ID}/messages`,
    {
      method: 'post',
      headers: { 'X-ChatWorkToken': CHATWORK_TOKEN },
      payload: { body: message }
    }
  );

  return ContentService.createTextOutput('OK');
}
```

#### GAS Web Appの公開手順

1. GASエディタ → 「デプロイ」 → 「新しいデプロイ」
2. 種類：「Webアプリ」を選択
3. アクセス権：「全員（匿名ユーザーを含む）」
4. デプロイ → WebアプリURLをコピー
5. kintoneのWebhook URLに貼り付け

---

### パターン5：Shopify新注文 → Googleスプレッドシート記録 → 在庫数更新

**推奨ツール**：Make（ビジュアルフロー型で最適）

#### Makeシナリオ設定手順

1. Make新規シナリオ作成
2. **モジュール1（トリガー）**：Shopify「Watch Orders」→ 新規注文時
3. **モジュール2（アクション）**：Google Sheets「Add a Row」
   - 注文ID / 商品名 / 数量 / 顧客情報 / 注文日時をマッピング
4. **モジュール3（アクション）**：Google Sheets「Search Rows」で在庫シートから現在在庫を検索
5. **モジュール4（アクション）**：Google Sheets「Update a Row」で在庫数を（現在値 - 注文数量）に更新
6. **モジュール5（条件分岐）**：在庫数が閾値（例：5個）以下になったら分岐
7. **モジュール6（アクション）**：Slack「Send a Message」で発注担当者に通知

#### エラーハンドリング
- **Rollback機能**：スプレッドシート更新失敗時に処理を巻き戻し
- **Error handler**：エラー発生時に管理者にメール通知
- **在庫マイナス防止**：在庫がマイナスになる場合のアラート処理

---

### パターン6：Googleカレンダーの予定15分前 → LINE通知

**推奨ツール**：Google Apps Script

#### GASコード例

```javascript
function checkCalendarAndNotifyLine() {
  const props = PropertiesService.getScriptProperties();
  const LINE_TOKEN = props.getProperty('LINE_NOTIFY_TOKEN');

  const now = new Date();
  const in15min = new Date(now.getTime() + 15 * 60 * 1000);
  const in16min = new Date(now.getTime() + 16 * 60 * 1000);

  const calendar = CalendarApp.getDefaultCalendar();
  const events = calendar.getEvents(in15min, in16min);

  events.forEach(event => {
    const message = `\n⏰ 15分後に予定があります\n📅 ${event.getTitle()}\n🕐 ${event.getStartTime().toLocaleString('ja-JP')}\n📍 ${event.getLocation() || '場所未設定'}`;

    UrlFetchApp.fetch('https://notify-api.line.me/api/notify', {
      method: 'post',
      headers: {
        'Authorization': `Bearer ${LINE_TOKEN}`,
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      payload: { message: message }
    });
  });
}
// トリガー設定：1分ごとに実行
```

#### セットアップ手順

1. LINE Notify（https://notify-bot.line.me/）にログイン
2. 「マイページ」 → 「トークンを発行する」
3. トークン名を設定 → 通知先（個人またはグループ）を選択
4. 発行されたトークンをGASのスクリプトプロパティに「LINE_NOTIFY_TOKEN」として保存
5. GASトリガー：1分ごとに実行するよう設定

> ⚠️ **注意**：LINE Notifyは2025年3月末でサービス終了予定のため、LINE Messaging APIへの移行を検討すること。

---

### パターン7：Slack特定チャンネルの投稿 → Notion/Googleドキュメントに自動議事録

**推奨ツール**：Zapier または Make

#### Zapier設定手順

1. **トリガー**：Slack「New Message Posted to Channel」→ 議事録チャンネル指定
2. **フィルター**：メッセージに「#議事録」タグが含まれる場合のみ処理
3. **アクション1**：OpenAI「Send Prompt」でメッセージを議事録フォーマットに整形
   - プロンプト例：「以下のSlackメッセージを議事録形式（日時・参加者・決定事項・TODO）にまとめてください：{message}」
4. **アクション2（Notion版）**：Notion「Append Block to Page」
   - 議事録用のNotionページIDを指定
5. **アクション2（Google Docs版）**：Google Docs「Create Document from Template」

---

### パターン8：毎月1日にGoogleスプレッドシートの月次データを集計 → PDF → メール送信

**推奨ツール**：Google Apps Script

#### GASコード例

```javascript
function monthlyReport() {
  const props = PropertiesService.getScriptProperties();
  const SHEET_ID = props.getProperty('MONTHLY_REPORT_SHEET_ID');
  const RECIPIENT = props.getProperty('REPORT_RECIPIENT_EMAIL');

  const ss = SpreadsheetApp.openById(SHEET_ID);
  const sheet = ss.getSheetByName('月次集計');

  // 先月のデータ範囲を取得
  const today = new Date();
  const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1, 1);
  const year = lastMonth.getFullYear();
  const month = lastMonth.getMonth() + 1;

  // 集計処理（例：売上合計）
  const data = sheet.getDataRange().getValues();
  let totalSales = 0;
  data.forEach((row, index) => {
    if (index === 0) return; // ヘッダー行をスキップ
    totalSales += row[3]; // D列が売上金額と仮定
  });

  // PDF出力
  const pdfBlob = DriveApp.getFileById(SHEET_ID).getAs('application/pdf');
  const reportName = `月次レポート_${year}年${month}月.pdf`;
  pdfBlob.setName(reportName);

  // メール送信
  GmailApp.sendEmail(
    RECIPIENT,
    `【月次レポート】${year}年${month}月度 売上：¥${totalSales.toLocaleString()}`,
    `${year}年${month}月度の月次レポートを添付します。\n\n` +
    `■ ${year}年${month}月度 売上合計：¥${totalSales.toLocaleString()}\n\n` +
    `詳細は添付PDFをご確認ください。`,
    { attachments: [pdfBlob] }
  );

  Logger.log(`月次レポートを${RECIPIENT}に送信しました`);
}

// トリガー設定：毎月1日の午前9時に実行
// スクリプトトリガー → 新規 → 時間ベース → 月ベースのタイマー → 毎月1日 → 午前9時
```

---

<a name="第4章"></a>
## 第4章：AIが「自動化指示書」を生成するためのフレームワーク

### 4-1. ヒアリング項目（構造化インテーク8項目）

AIが自然言語の要件を受け取った際に収集すべき8つの情報：

| # | 質問 | 観点 | 回答例 |
|---|------|------|------|
| Q1 | 何を自動化したいか？（What） | 業務種別 | 転記作業 / 通知 / データ集計 / ファイル操作 / 承認フロー |
| Q2 | データのソースはどこか？（From） | 起点SaaS | Gmail / Googleフォーム / スプレッドシート / kintone / Shopify |
| Q3 | データの転送先はどこか？（To） | 終点SaaS | freee / マネーフォワード / Slack / LINE / Chatwork / Notion |
| Q4 | いつ実行するか？（When） | トリガー種別 | イベント型（フォーム送信時）/ 時間型（毎日9時）|
| Q5 | どのくらいの頻度か？（Frequency） | 実行頻度 | 月次 / 週次 / 日次 / リアルタイム |
| Q6 | エラー発生時はどうするか？（Error Handling） | 異常系 | 管理者メール / Slack通知 / スキップ / リトライ |
| Q7 | 技術的な制約は？（Constraints） | 制約条件 | 利用可能ツール / 予算 / 担当者の技術レベル |
| Q8 | 個人情報は含まれるか？（Privacy） | コンプライアンス | 含まれる場合：どの情報か / 海外サーバー利用可否 |

---

### 4-2. ツール選定ディシジョンツリー

```
START
│
├─[Q1] Google Workspace（Gmail/Sheets/Drive）が中心のフローか？
│   ├─ YES → Google Apps Script（GAS）が最適
│   │         ※ただしJavaScript知識がある担当者がいる場合
│   └─ NO  → 次の質問へ
│
├─[Q2] Microsoft 365（Teams/Excel/Outlook）が中心のフローか？
│   ├─ YES → Power Automate が最適
│   └─ NO  → 次の質問へ
│
├─[Q3] freee/マネーフォワード/kintone/LINE等、日本SaaSが中心か？
│   ├─ YES → Yoom が最適（日本SaaS最高対応）
│   │         ※非エンジニアでも設定可能
│   └─ NO  → 次の質問へ
│
├─[Q4] グローバルSaaS（Salesforce/HubSpot/Shopify/Zendesk等）が多いか？
│   ├─ YES → Zapier または Make
│   │   ├─ 複雑なロジックが必要         → Make
│   │   └─ シンプルな2ステップ連携のみ  → Zapier
│   └─ NO  → 次の質問へ
│
├─[Q5] APIが存在しないWebシステムの操作が必要か？
│   ├─ YES → ブラウザRPA（Power Automate Desktop / UiPath）
│   └─ NO  → 次の質問へ
│
├─[Q6] セキュリティ要件が高く、自社サーバーで管理したいか？
│   ├─ YES → n8n（セルフホスト）または Python
│   └─ NO  → 予算に応じてZapier/Make/Yoomから選択
│
END
```

---

### 4-3. 自動化指示書テンプレート

```markdown
# 自動化指示書
**バージョン：** 1.0
**作成日：** YYYY/MM/DD
**作成者：** AIエージェント自動生成

---

## 【概要】
[1行で何を自動化するかを記述]
例：Googleフォームへの問い合わせ回答を受信した際に、kintoneに顧客レコードを
    自動作成し、担当者にSlackで通知する。

---

## 【必要なアカウント・ツール】

| ツール名 | 用途 | 必要な権限・設定 |
|---------|------|--------------|
| Google Workspace | フォーム・スプレッドシート管理 | 編集者権限 |
| Yoom | 自動化ハブ | 管理者アカウント |
| kintone | 顧客DB | APIトークン発行権限 |
| Slack | 通知先 | Incoming Webhook設定権限 |

---

## 【セットアップ手順】

### Step 1: 事前準備（所要時間：30分）

1. kintoneにてAPIトークンを発行する
   - 管理者 → アプリの設定 → APIトークン → 追加
   - 権限：「レコードの閲覧」「レコードの追加」にチェック

2. SlackにIncoming Webhookを設定する
   - Slack App Directory → Incoming WebHooks → 追加
   - 通知先チャンネルを選択 → Webhook URLをコピー

3. Yoomに各サービスを接続する
   - Yoom管理画面 → マイアプリ → + 新しいアプリ
   - Google / kintone / Slackをそれぞれ認証

### Step 2: フローボット作成（所要時間：20分）

1. Yoomダッシュボード → フローボット → + 新規作成
2. トリガー：「Googleスプレッドシート」→「行が追加されたとき」
3. アクション1：「kintone」→「レコードを追加する」
   - マッピング：回答列 → kintoneフィールド
4. アクション2：「Slack」→「チャンネルにメッセージを送る」
   - メッセージテンプレートを設定

---

## 【テスト方法】

### 正常系テスト

1. テスト用Googleフォームを開く
2. テストデータを入力して送信
3. 期待される結果：
   - ✅ スプレッドシートに行が追加される
   - ✅ kintoneに新規レコードが作成される
   - ✅ Slackの#通知チャンネルにメッセージが届く

### エラー系テスト

1. kintoneのAPIトークンを意図的に無効化
2. フォームを送信
3. 期待される結果：
   - ✅ Yoomのエラーログに記録される
   - ✅ 管理者にエラー通知メールが届く
   - ⚠️ kintoneへの書き込みは失敗するが他処理は継続

---

## 【メンテナンスガイド】

### APIキー・トークンの更新
- kintone APIトークン：有効期限なし（定期的な更新を推奨）
- Yoomのアプリ接続：OAuth2.0の場合、90日で再認証が必要な場合あり

### 接続切れ時の対応
1. Yoomダッシュボード → フローボット → 該当フロー
2. 「接続エラー」の赤いアイコンが表示されている場合
3. 「マイアプリ」→ 該当サービスを再認証

### 担当者退職時の対応
1. 退職前に「サービスアカウント（共有アカウント）」への移行を実施
2. Yoomのアプリ接続を共有アカウントで再設定
3. 個人アカウントの削除は移行完了後に実施
```

---

### 4-4. コード生成プロンプト設計

GAS/Python等のコード生成に使用するプロンプトテンプレート：

```
あなたはGoogle Apps Scriptの専門家です。
以下の要件に基づいて、本番環境で使用可能なGASコードを生成してください。

【要件】
- トリガー：{trigger_type}（{trigger_detail}）
- ソース：{source_service}（{source_detail}）
- アクション：{action_detail}
- 通知先：{notification_service}（{channel_or_address}）

【必須要件】
1. APIキー・トークンは必ずPropertiesService.getScriptProperties()から取得すること（直書き禁止）
2. try-catch でエラーハンドリングを実装すること
3. エラー発生時は Logger.log() でログを記録し、{error_notification_method}で通知すること
4. 日本語コメントを各処理に付与すること
5. 冪等性を考慮し、二重実行を防ぐ仕組みを実装すること

【コード構造】
- メイン関数名：{main_function_name}
- セットアップ関数：setupProperties()を別途作成し、初期設定方法をコメントに記載すること
```

---

<a name="第5章"></a>
## 第5章：セキュリティ・権限管理とよくあるトラブル

### 5-1. APIキー・OAuthトークンの安全な管理

#### ❌ やってはいけないこと（初心者の典型的ミス）

**NG例1：スプレッドシートへの直書き**

| サービス名 | APIキー |
|-----------|--------|
| freee | freeee_prod_xxxxxxx ← **絶対NG！** |
| LINE | xxxxxxxxxxxxx ← **絶対NG！** |

**NG例2：GASコードへのハードコーディング**

```javascript
// ❌ 絶対やってはいけない
const API_KEY = 'sk-xxxx-xxxxxxxx';  // コードをシェアすると漏洩！
const SLACK_WEBHOOK = 'https://hooks.slack.com/...';  // GitHubに上げたら終わり
```

**NG例3：Slackのパブリックチャンネルへのトークン貼り付け**
- 「このAPIキー使ってください → sk-xxxx」← **絶対NG！**

---

#### ✅ 正しい管理方法

**方法1：GAS PropertiesService（推奨・無料）**

```javascript
// ============================================
// ★ セットアップ時に1回だけ実行する関数
// ============================================
function setProperties() {
  const props = PropertiesService.getScriptProperties();
  props.setProperties({
    'FREEE_ACCESS_TOKEN': '←ここに実際のトークンを入力（この関数はローカルで実行後削除）',
    'SLACK_WEBHOOK_URL': 'https://hooks.slack.com/services/xxx/yyy/zzz',
    'KINTONE_API_TOKEN': 'xxxxxxxxxxxxxxxxxx',
    'LINE_NOTIFY_TOKEN': 'yyyyyyyyyyyyyyy'
  });
  Logger.log('プロパティ設定完了');
}

// ============================================
// ★ 実際の自動化コードでの使用方法
// ============================================
function main() {
  // ✅ PropertiesServiceから安全に取得
  const props = PropertiesService.getScriptProperties();
  const token = props.getProperty('FREEE_ACCESS_TOKEN');
  const webhook = props.getProperty('SLACK_WEBHOOK_URL');

  // 以降の処理で変数を使用...
}
```

**方法2：Yoom/ZapierのOAuth認証機能を利用**
- 各iPaaSツールには「シークレット変数」や「接続情報の暗号化保存」機能がある
- 接続設定画面でOAuth認証を行えば、トークンはツール側で暗号化管理される
- 担当者がトークンの実体を見ることなく設定可能

**方法3：Google Secret Manager（エンタープライズ向け）**

```python
# Python + Google Secret Managerの例
from google.cloud import secretmanager

def get_secret(secret_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# 使用例
freee_token = get_secret("freee-access-token")
```

---

### 5-2. 自動化でよく起こるトラブルTOP10

| # | トラブル内容 | 主な原因 | 対策 | 検知方法 |
|---|------------|---------|------|---------|
| 1 | **APIレートリミット超過** | 短時間に大量リクエスト送信 | バッチ処理 + `Utilities.sleep()` / 指数バックオフ実装 | エラーレスポンス監視（HTTP 429） |
| 2 | **OAuthトークン期限切れ** | アクセストークンの有効期限（通常1〜2時間）切れ | リフレッシュトークンの自動更新実装 / iPaaSに任せる | 401 Unauthorizedエラー検知 |
| 3 | **データ形式の不一致** | 日付フォーマット違い（2024/01/01 vs 2024-01-01）、数値の型違い | バリデーション処理実装、フォーマット変換関数を追加 | テスト時の詳細チェック |
| 4 | **二重実行（重複処理）** | ワークフローが複数回トリガーされる | べき等性設計（処理済みフラグ列をSpreadsheetに追加）、ロック機構 | ログで重複検出 |
| 5 | **ブラウザRPAの動作停止** | SaaS側のUI変更でセレクタが変わる | UI要素のセレクタを堅牢に設定、定期的な再録画 | 定期テスト実行 |
| 6 | **Webhookの署名検証失敗** | タイムスタンプのズレ、ヘッダー設定ミス | HMAC署名検証ロジックの正確な実装、NTPによる時刻同期 | エラーログ（HTTP 400） |
| 7 | **退職者アカウントに紐づいた認証切れ** | 退職者の個人OAuth接続が失効 | 共有サービスアカウントへの移行、定期的な接続確認 | 月次チェックリスト |
| 8 | **SSL/TLS証明書エラー** | 外部サービスの証明書期限切れ | エラー通知で早期検知、ツール側のアップデート対応 | SSL証明書期限監視 |
| 9 | **ファイルエンコーディング問題** | CSVの文字コード不一致（Shift-JIS vs UTF-8） | iconv等でエンコーディング変換処理を追加 | 文字化け検知 |
| 10 | **スクリプト実行時間超過** | GASの6分制限 / iPaaSのタイムアウト | バッチ分割処理、非同期処理への変更、継続トークンの活用 | タイムアウトエラー |

#### 対策コード例：APIレートリミット対応（指数バックオフ）

```javascript
/**
 * 指数バックオフ付きAPIリクエスト
 * @param {string} url - APIエンドポイント
 * @param {object} options - fetchオプション
 * @param {number} maxRetries - 最大リトライ回数（デフォルト3回）
 */
function fetchWithRetry(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = UrlFetchApp.fetch(url, options);
      const code = response.getResponseCode();

      if (code === 429) {
        // レートリミット: 指数バックオフ（1秒, 2秒, 4秒...）
        const waitTime = Math.pow(2, attempt) * 1000;
        Logger.log(`レートリミット。${waitTime}ms待機後リトライ（試行${attempt + 1}/${maxRetries}）`);
        Utilities.sleep(waitTime);
        continue;
      }

      return response;
    } catch (error) {
      if (attempt === maxRetries - 1) throw error;
      Utilities.sleep(Math.pow(2, attempt) * 1000);
    }
  }
  throw new Error(`${maxRetries}回リトライしましたが失敗しました`);
}
```

#### 対策コード例：二重実行防止（Lock Service）

```javascript
function processOnce() {
  // スクリプトロックを取得（同時実行を防止）
  const lock = LockService.getScriptLock();

  try {
    // 最大30秒待機してロック取得を試みる
    lock.waitLock(30000);

    // ここに実際の処理を記述
    Logger.log('処理開始');
    // ... 処理 ...
    Logger.log('処理完了');

  } catch (e) {
    Logger.log('ロック取得失敗または処理エラー: ' + e.message);
    throw e;
  } finally {
    // 必ずロックを解放
    lock.releaseLock();
  }
}
```

---

### 5-3. 個人情報保護法の注意事項

#### 個人情報保護委員会ガイドラインに基づく3大チェックポイント

**①適切なクラウドサービスの選定**
- クラウド事業者が適切な安全管理措置を講じているかを利用規約で確認
- ISO 27001 / SOC2 / ISO 27018 等のセキュリティ認証取得状況を確認
- データの保存先（国内/海外）を確認
- 海外サーバー利用時は海外提供規制（個人情報保護法24条）への対応を確認

**②委託契約の締結**
- 利用規約に不足がある場合は別途覚書を締結
- 必須条項：
  - 個人データの取扱制限（目的外利用の禁止）
  - 漏洩発生時の通知・報告義務
  - 再委託先への監督義務
  - 委託終了時のデータ削除義務

**③継続的な監督**
- 年1回以上の安全管理措置の確認（チェックリストの活用）
- 情報漏洩発生時の連絡体制の整備
- 定期的な監査の実施またはサービス事業者からの報告受領

#### 自動転送で特に注意すべきシナリオ

| シナリオ | リスク | 対策 |
|---------|------|------|
| Gmailの問い合わせ内容を海外サーバーのZapierで処理 | 個人情報の海外送信 | Yoom（国内）を優先検討、または利用規約で十分な保護を確認 |
| 顧客データをSlackに自動転送 | Slackへの個人情報流入 | マスキング処理を追加（氏名→頭文字のみ等） |
| 履歴書・個人情報ファイルをGoogleドライブに自動保存 | アクセス権限の管理不備 | 専用フォルダに制限付きアクセスで保存、共有設定を「特定のユーザーのみ」に |
| 退職した担当者経由でAPIキーが残存 | 不正アクセスリスク | 担当者変更時のAPIキーローテーション手順を整備 |
| 自動化フローが顧客の決済情報を処理 | PCI DSS違反リスク | 決済情報は専用の準拠済みサービスでのみ処理、自動化フローを通過させない |

---

### 5-4. 退職者アカウントリスクの対策

#### 問題の本質

多くの中小企業では、自動化フローが「担当者個人のGoogleアカウント」や「個人のfreeeアカウント」に紐づいており、その人が退職するとフロー全体が停止するリスクがある。

**典型的な失敗事例：**
- GASが退職した山田さんの個人Googleアカウントで動いていた
- Yoomの接続がすべて退職者のOAuth認証に紐づいていた
- kintoneのAPIトークンが退職者アカウントに発行されていた

#### 解決策：「サービスアカウント運用」の確立

**ステップ1：自動化専用アカウントの作成**

```
推奨メールアドレス例：
  automation@yourcompany.co.jp   （GAS/Googleサービス用）
  rpa-service@yourcompany.co.jp  （iPaaS連携用）
  api-system@yourcompany.co.jp   （APIキー管理用）
```

**ステップ2：アカウント管理台帳の整備**

| サービス名 | 接続アカウント | 担当者 | 最終更新日 | トークン種別 | 有効期限 |
|-----------|-------------|-------|----------|-----------|--------|
| Yoom | automation@company.co.jp | 山田太郎 | 2026/01/15 | OAuth2.0 | 再認証時に更新 |
| freee | automation@company.co.jp | 山田太郎 | 2026/01/15 | OAuth2.0 | 再認証時に更新 |
| kintone | system-api@company.co.jp | 情報システム部 | 2026/01/15 | APIトークン | なし |
| Slack Webhook | — | 情報システム部 | 2026/01/15 | Webhook URL | なし |

**ステップ3：退職時チェックリスト**

```
□ 自動化フローの接続アカウントを全てリストアップ
□ 共有アカウントへの移行（移行前に動作確認）
□ 旧アカウントのAPIキー・OAuthを失効
□ kintoneのAPIトークンを再発行
□ Yoom等iPaaSの「マイアプリ」接続を共有アカウントで再認証
□ GASのオーナーシップを共有アカウントに移行
□ 新担当者への引き継ぎドキュメントの更新
□ 引き継ぎ後の動作確認テスト実施
□ 旧アカウント削除（移行完了後）
```

---

<a name="附録A"></a>
## 附録A：ツール別料金比較一覧表（2026年版）

| ツール名 | 無料プラン制限 | 最安有料プラン | 日本語UI | 日本SaaS対応 | 技術レベル | 向いている規模 |
|---------|------------|------------|--------|------------|---------|------------|
| **Zapier** | 100タスク/月 | $19.99/月 | △ | △ | ★☆☆☆☆ | 小〜中 |
| **Make** | 1,000ops/月 | $10.59/月 | ○ | △ | ★★☆☆☆ | 小〜中 |
| **n8n** | 無制限(自己ホスト) | €20/月 | △ | △ | ★★★★☆ | 中〜大 |
| **GAS** | 完全無料 | 無料 | ◎ | ○ | ★★★☆☆ | 小 |
| **Power Automate** | M365に含む | $15/ユーザー/月 | ◎ | △ | ★★☆☆☆ | 中〜大 |
| **IFTTT** | 3アプレット | $2.5/月 | △ | ✕ | ★☆☆☆☆ | 個人〜超小 |
| **Yoom** ⭐ | 100タスク/月 | ¥2,400/月 | ◎ | **◎** | ★☆☆☆☆ | 小〜中 |
| **Python+API** | 無制限 | ホスティング代のみ | ◎ | ◎ | ★★★★★ | 制限なし |
| **ブラウザRPA** | Community有 | 要問合せ | ◎ | ◎ | ★★★☆☆ | 中〜大 |

### 日本SaaS連携対応マトリクス

| ツール | freee | マネーフォワード | kintone | LINE | Chatwork | Slack | Gmail |
|-------|-------|--------------|---------|------|---------|-------|-------|
| Zapier | △ | △ | ○ | △ | △ | ◎ | ◎ |
| Make | ○ | △ | ○ | ○ | △ | ◎ | ◎ |
| n8n | カスタム | カスタム | カスタム | カスタム | カスタム | ◎ | ◎ |
| GAS | ○(API) | ○(API) | ○(API) | ○ | ○ | ○ | ◎ |
| Power Automate | △ | △ | △ | ○ | △ | ◎ | ◎ |
| Yoom | **◎** | **◎** | **◎** | **◎** | **◎** | ◎ | ◎ |

> 凡例：◎=公式対応 / ○=対応あり / △=制限あり・間接対応 / カスタム=要カスタム実装 / ✕=非対応

---

<a name="附録B"></a>
## 附録B：参考リンク集

### 公式ドキュメント

| サービス | URL |
|---------|-----|
| Zapier 公式ドキュメント | https://help.zapier.com/ |
| Make 公式ドキュメント | https://www.make.com/en/help/ |
| n8n 公式ドキュメント | https://docs.n8n.io/ |
| GAS 公式リファレンス | https://developers.google.com/apps-script |
| Power Automate 公式 | https://learn.microsoft.com/ja-jp/power-automate/ |
| Yoom 公式サイト | https://yoom.fun/ |

### 日本SaaS API ドキュメント

| サービス | URL |
|---------|-----|
| freee API 公式 | https://developer.freee.co.jp/ |
| kintone API 公式 | https://kintone.dev/ |
| マネーフォワード クラウド請求書 API | https://invoice.moneyforward.com/docs/api/v3/ |
| LINE Messaging API | https://developers.line.biz/ja/ |
| Chatwork API | https://developer.chatwork.com/ |

### 法令・ガイドライン

| 文書 | URL |
|-----|-----|
| 個人情報保護委員会 公式サイト | https://www.ppc.go.jp/ |
| PPC クラウドサービス提供事業者ガイド | https://www.ppc.go.jp/files/pdf/240325_alert_cloud_service_provider.pdf |
| 経済産業省 IT導入補助金 | https://www.it-hojo.jp/ |
| IPA クラウドサービス安全利用の手引き | https://www.ipa.go.jp/ |

### 学習リソース（日本語）

| リソース | 内容 |
|---------|-----|
| Qiita（GAS関連） | https://qiita.com/tags/gas |
| Zenn（自動化関連） | https://zenn.dev/topics/automation |
| Yoom テンプレート集 | https://lp.yoom.fun/blog-posts |
| kintone 開発者コミュニティ | https://cybozudev.zendesk.com/hc/ja |

---

*本設計書は2026年3月時点の情報に基づいて作成されています。各ツールの仕様・価格は変更される場合があります。最新情報は各サービスの公式サイトでご確認ください。*

---

**文書終了**
```
