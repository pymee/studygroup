# ファイルの説明
課題のサンプルプログラムは以下の通りになります。
ディレクトリ | ファイル名　| 用途
--- | --- | ---
. | readme.md  | 今読んでいるページのファイル
. | step2_pymee.py | 課題のサンプルプログラム

以下のファイルは試しに作ったテスト用ファイルになります。
興味がある方はご確認くださいませ:relaxed:
ディレクトリ | ファイル名　| 用途
--- | --- | ---
. |Test_step2_pymee.py | テスト用のプログラム
./test/input_file |test.csv | 読み込みファイル
./test/input_file |test_none.csv | 中身が空の読み込みファイル
./test/result |配下のファイル | 期待する出力結果ファイル

# 単体テストの実行方法
1. 7th_step2をクローン
   `git clone <URL>`
   詳細は[こちら](https://github.com/pymee/githandson/blob/master/textbook/git_markdown_and_handson.md)を参照くださいませ:smile:
1. 実行場所が7th_step2であることを確認
    ```
    $ pwd
    (中略)/7th_step2
    ```
1. テスト実行
    ```
    $python3 Test_step2_pymee.py -v
    ```
1. 「OK」と表示されればテスト問題なし！
    ```
    $ python3 Test_step2_pymee.py -v
    test_empty_file (__main__.TestInputFile) ... ok
    test_multi_file (__main__.TestInputFile) ... ok
    test_none_file (__main__.TestInputFile) ... ok
    test_not_specified (__main__.TestInputFile) ... ok
    test_fin (__main__.TestNormal) ... ok
    test_0_exist_output_file (__main__.TestOutputFile) ... ok
    test_1_output_file (__main__.TestOutputFile) ... ok

    ----------------------------------------------------------------------
    Ran 7 tests in 0.498s

    OK
    ```
