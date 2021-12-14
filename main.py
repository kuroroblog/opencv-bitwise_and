import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread("image.jpg")
img2 = cv2.imread("mask.png")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img2 is None:
    sys.exit("Could not read the image.")

# 画像サイズを合わせるために、調整する。
# ※ 今回imgの画像が640x447だったため、(640, 447)とする。
# resizeについて : https://kuroro.blog/python/KznX7CJ9axPuNSYBQN6m/
img2 = cv2.resize(img2, (640, 447))

print(type(img))
print(img.shape)
print(type(img2))
print(img2.shape)

# bitwise_and関数 : 元画像をマスク(覆い隠す)するために利用する関数

# 第一引数(必須) : 多次元配列(numpy.ndarray)
# 第二引数(必須) : 多次元配列(numpy.ndarray)
# 戻り値 : 多次元配列(numpy.ndarray)
output = cv2.bitwise_and(img, img2)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', output)
