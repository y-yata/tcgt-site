# AIyabane / TCG-T サイト

既存の GitHub Pages サイトです（CNAME `aiyabane.com`）。2026-10-24 から、全ページを**ビルド不要の HTML**にそろえた（Jekyll のテーマは使っていない）。

## 構成

| URL | ファイル | 作り方 |
|---|---|---|
| `/` | `index.html` | 直接編集（AIyabane の入口・アプリ一覧・事業者情報） |
| `/privacy/`・`/privacy/en/`・`/tokushoho/`・`/delete-account/`・`/delete-account/en/` | 各 `index.html` | **原稿 `_src/*.md` を `python3 tools/build_pages.py` で組み立てる**。HTML を直接直さない |
| `/tcg-t/…` | 各 `index.html` | 直接編集（下記） |

- 見た目は全ページ `tcg-t/assets/site.css` を使う。ヘッダー・フッターを変えるときは、`tools/build_pages.py` のテンプレートと `index.html`・`tcg-t/` の各ページの両方を直す
- **URL を動かさない。** ストアの登録・アプリ内・AdMob の同意メッセージから指している
- 事業者の氏名は載せない（特商法・個人情報保護法とも「請求があれば遅滞なく開示」の書き方。方針は本部 `private/business-identity.md`）

## TCG-T のページ

- `tcg-t/index.html`：紹介
- `tcg-t/guide/index.html`：ガイド一覧・検索
- `tcg-t/guide/start/`：入門（設定・自分の画像・受け取ったZIP）
- `tcg-t/guide/deck/`：デッキ作成
- `tcg-t/guide/solo/`：一人回し
- `tcg-t/guide/online/`：オンライン
- `tcg-t/guide/custom/`：発展（詳細設定・クイック操作）
- `tcg-t/guide/zip/`：発展（ZIP作成）
- `tcg-t/guide/decorations/`：装飾（スリーブ・プレイマット・利用条件）
- `tcg-t/support/`：FAQ・問い合わせ
- `tcg-t/updates/`：更新情報

TCG-T配下はビルド不要のHTML/CSS/JavaScriptです。各HTMLを直接編集できます。共通のヘッダー・フッターを変更する場合は全ページに反映してください。文章の原稿はアプリリポジトリの `org/marketing/` にあります。

## ローカル確認

リポジトリ直下で `python3 -m http.server 8765 --bind 127.0.0.1` を実行し、`http://127.0.0.1:8765/tcg-t/` を開きます。法律まわりのページも組み立て済みの HTML なので、この簡易サーバーで確認できます。

## 公開前の確認

ストアリンクとGoogleフォームは未確定のため準備中です。確定後に差し替えてください。掲載画像は既存のiOSデモスクリーンショットです。公開候補版で手順・表示を照合し、必要な画面を追加撮影してください。フォームの運用と公開時には問い合わせ情報の取り扱いも確定してください。

この変更だけでは公開されません。既存のGitHub Pagesの配信対象へ反映してから実URLを確認してください。

操作アイコンは各機能の手順に併記しています。共通スタイルは `tcg-t/assets/inline-icons.css`、元画像は `tcg-t/assets/icons/` です。

- `tcg-t/guide/billing/`：料金・ポイント・Premium。ストアの実価格は公開前に確認し、固定額を掲載する場合は表示の整合性を確認してください。
