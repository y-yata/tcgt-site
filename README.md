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
- `tcg-t/guide/probability/`：確率計算（ドロー計算機・コンボ確率・確率の読み）
- `tcg-t/guide/online/`：オンライン
- `tcg-t/guide/custom/`：発展（詳細設定・クイック操作）
- `tcg-t/guide/zip/`：発展（ZIP作成）
- `tcg-t/guide/decorations/`：装飾（スリーブ・プレイマット・利用条件）
- `tcg-t/guide/billing/`：料金・ポイント・Premium（価格はストアの表示に合わせる）
- `tcg-t/support/`：FAQ・問い合わせ
- `tcg-t/updates/`：更新情報

- TCG-T 配下はビルド不要の HTML/CSS/JavaScript。各 HTML を直接編集する。共通のヘッダー・フッターを変えるときは全ページに反映する
- 操作アイコンは各機能の手順に併記している。共通スタイルは `tcg-t/assets/inline-icons.css`、画像は `tcg-t/assets/icons/`
- 文章のもとになった原稿・広報の資料は、アプリのリポジトリ（`~/work/TCG-T`）の `docs/marketing/`。公開物の一覧は同じリポジトリの `docs/public-inventory.md`
- 画面例はデモ用のカードで撮ったもの。実在のカードゲームの名前・画像を載せない

## 公開日に直すところ（2026-10-24 時点）

- `tcg-t/index.html`・`tcg-t/updates/index.html` の「ストア公開準備中」を、App Store・Google Play へのリンクに差し替える
- 問い合わせの Google フォームは公開済み。受信の確認が済んだら `tcg-t/support/` に載せる（今はメール窓口だけ）

## ローカル確認

リポジトリ直下で `python3 -m http.server 8765 --bind 127.0.0.1` を実行し、`http://127.0.0.1:8765/tcg-t/` を開く。法律まわりのページも組み立て済みの HTML なので、この簡易サーバーで確認できる。

## 公開

`main` に push すると GitHub Pages から配信される。**push は毎回ユーザーの確認を取ってから。** push したら実 URL を開いて確かめる。
