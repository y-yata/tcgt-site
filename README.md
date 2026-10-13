# AIyabane / TCG-T サイト

既存の GitHub Pages サイトです。ドメイン・Jekyll設定・法務ページは従来の構成を使います。

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

リポジトリ直下で `python3 -m http.server 8765 --bind 127.0.0.1` を実行し、`http://127.0.0.1:8765/tcg-t/` を開きます。この簡易サーバーはMarkdownを変換しないため、既存のトップ・法務ページの表示確認にはJekyllが必要です。

## 公開前の確認

ストアリンクとGoogleフォームは未確定のため準備中です。確定後に差し替えてください。掲載画像は既存のiOSデモスクリーンショットです。公開候補版で手順・表示を照合し、必要な画面を追加撮影してください。フォームの運用と公開時には問い合わせ情報の取り扱いも確定してください。

この変更だけでは公開されません。既存のGitHub Pagesの配信対象へ反映してから実URLを確認してください。

操作アイコンは各機能の手順に併記しています。共通スタイルは `tcg-t/assets/inline-icons.css`、元画像は `tcg-t/assets/icons/` です。

- `tcg-t/guide/billing/`：料金・ポイント・Premium。ストアの実価格は公開前に確認し、固定額を掲載する場合は表示の整合性を確認してください。
