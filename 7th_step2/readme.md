# ファイルの説明
ディレクトリ | ファイル名　| 用途
--- | --- | ---
7th_step2 | step2_pymee.py | プログラム本体
7th_step2 |Test_step2_pymee.py | テスト用のプログラム
7th_step2/test/input_file |test.csv | データが入っているテスト用ファイル
7th_step2/test/input_file |test_none.csv | 中身が空のテスト用ファイル
7th_step2/test/result |配下のファイル | 期待する出力結果ファイル

# 単体テストの実行方法
1. 7th_step2フォルダをコピー
1. 7th_step2フォルダへ移動
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
