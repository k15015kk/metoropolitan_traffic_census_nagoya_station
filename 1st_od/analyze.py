import pandas as pd
import glob
import gc


def convert_csv_to_frame(path):

  # ヘッダーを定義
  header = [
      "圏域",
      "カード種別",
      "【入場】圏域",
      "【入場】事業者名",
      "【入場】路線名",
      "【入場】駅名",
      "【入場】都道府県",
      "【入場】市町村区",
      "【入場】時間帯",
      "【出場】圏域",
      "【出場】事業者名",
      "【出場】路線名",
      "【出場】駅名",
      "【出場】都道府県",
      "【出場】市町村区",
      "所要時間（５分単位）",
      "人数"
  ]

  # データ読み込み

  # すべてのファイル名を取得
  filenames = glob.glob(path)

  # 読み込まないファイルを定義
  not_read_filenames = ['extract.csv']

  # ヘッダーが存在するファイル名を定義
  with_header_filenames = ['01.csv', '07.csv']

  frame_list = []

  for filename in filenames:

    print(f'reading: {filename}')

    # 読み込まないファイルの場合
    if filename in not_read_filenames:
      continue

    if filename in with_header_filenames:
      # ヘッダー行があるとき
      df = pd.read_csv(filename, header=0)
      frame_list.append(df)
    else:
      # ヘッダー行がないとき
      df = pd.read_csv(filename, header=None, names=header)
      frame_list.append(df)

    # 使わないデータフレームをメモリ解放
    del df
    gc.collect()

  # すべてのデータフレームを結合
  concat_frame = pd.concat(frame_list, ignore_index=True)

  print(concat_frame)
  return concat_frame


def extract_from_route_name(frame, company_name, line_name, station_name):

  # 引数で指定した事業者名と路線名からデータを抽出
  extract_frame = frame[
    (frame['【入場】事業者名'] == company_name) & 
    (frame['【入場】路線名'] == line_name) &
    (frame['【入場】駅名'] == station_name)
  ]

  print(extract_frame)
  return extract_frame


def main():

  # 全体のデータフレームを作成
  frame = convert_csv_to_frame(path='*.csv')

  # 事業者名と路線名を指定してデータを抽出（入場記録）
  extract_frame = extract_from_route_name(
    frame, 
    company_name='東海旅客鉄道', 
    line_name='東海道新幹線',
    station_name='名古屋'
  )

  # 抽出データをcsvファイルに書き出し
  extract_frame.to_csv('extract.csv', index=False)

if __name__ == "__main__":
  main()
