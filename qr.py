import qrcode as qr
img =qr.make("https://www.youtube.com/watch?v=4ZRJdTvtobI&list=RD4ZRJdTvtobI&start_radio=1")
img.save("youtube_qr.png")
