import pandas as pd

def convert_csv_to_frame(filename):

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
  df = pd.read_csv(filename, header=0)
  return df

def main():

  # 全体のデータフレームを作成
  frame = convert_csv_to_frame(filename='output/extract_jrtokai.csv')

  sum_frame = frame.loc[:,['【出場】駅名','【出場】事業者名','【出場】路線名','人数']].groupby(['【出場】駅名','【出場】事業者名','【出場】路線名']).sum()

  print(sum_frame)

  # 抽出データをcsvファイルに書き出し
  sum_frame.to_csv('output/exit_count.csv', index=True)

if __name__ == "__main__":
  main()
