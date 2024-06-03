# 人工言語リスト 処理用プログラム群

[みかぶる](https://twitter.com/Mikanixonable)さんによって纏められた[『日本語圏人工言語リスト』](https://migdal.jp/mikanixonable/%E6%97%A5%E6%9C%AC%E3%81%AE%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E%E7%B0%A1%E6%98%93%E4%B8%80%E8%A6%A7-2023-%E5%B9%B4-12-%E6%9C%88-3k46)や、それを自由に編集できる形で各種Wiki上に公開された記事に関する処理を行うためのリポジトリです。

## このリポジトリが行うこと

- Wikiからの自動データ取得、またCotec形式データへの加工（Cotecについては[こちら](https://migdal.jp/cl_kiita/cotec-conlang-table-expression-powered-by-csv-clakis-rfc-2h86)を参照）
	- 毎月1日のUTC 0時頃に自動実行されます。
	- 現在は人工言語学Wiki上のリストからのみ取得を行っています。
- 万が一に備えてのデータ保全

## リポジトリの内容物

- `conlinguistics-wiki-list.ctc`
	- 人工言語学Wiki上のリストから取得、生成しているCotecデータであり、月1度の更新で最新版に保たれます。
- `migdal-wiki-list.ctc`
	- Migdal ConLang Wiki上のリストから取得、生成したCotecデータです。現在は更新を停止しています。
- `conlang-list.ctc`
	- みかぶるさんの第6版リストから生成したCotecデータです。
- `py/*`
	- プログラム本体です。

## 各リストへのリンク

### Wiki上

- [日本語圏の人工言語一覧 (人工言語学Wiki)](https://wiki.conlinguistics.jp/%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%9C%8F%E3%81%AE%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E%E4%B8%80%E8%A6%A7)
	- 現在主流な人工言語リスト。みかぶるさんの第6版リストを基に、自由に編集できる形で公開されたものである。編集や参照が必要である場合はこのリストを利用することを推奨。（コミュニティベース）
	- このリポジトリでもこのリストからデータ取得を行っています。
- [日本語圏の人工言語の一覧表 (Migdal ConLang Wiki)](https://wiki.conlinguistics.jp/%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%9C%8F%E3%81%AE%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E%E4%B8%80%E8%A6%A7)
	- 人工言語学Wikiが利用可能になるまで一時的に設置されていた人工言語リスト。みかぶるさんの第6版リストを基に、自由に編集できる形で公開されたものである。現在は利用が推奨されていない。（コミュニティベース）

### みかぶるさんによる元データ

- [日本の人工言語簡易一覧 (Migdal)](https://migdal.jp/mikanixonable/%E6%97%A5%E6%9C%AC%E3%81%AE%E4%BA%BA%E5%B7%A5%E8%A8%80%E8%AA%9E%E7%B0%A1%E6%98%93%E4%B8%80%E8%A6%A7-2023-%E5%B9%B4-12-%E6%9C%88-3k46)
	- 2023/12/17、みかぶるさんによって初めにMigdalで公開されたもの。（第6版まで）
- [日本語圏人工言語リスト (Github Pages)](https://mikanixonable.github.io/conlangList/conlang)
	- みかぶるさんのホームページで公開されているもの。Migdal記事と同内容と思われる。（第6版まで）
- [日本語圏人工言語リスト (CSV)](https://mikanixonable.github.io/conlangList/conlang)
	- 上記2つの元になっているCSVファイル。（第6版の底本）

## 連絡先

このリポジトリに関して何らかの問題が発生している場合、リポジトリ管理者である[かえる](https://twitter.com/kaeru2193)までお問い合わせください。