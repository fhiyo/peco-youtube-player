# youtubeのplaylistをローカルで再生またはランダムで連続再生する

## 概要
youtubeの広告がうっとおしいのでmpvでyoutube見られるようにした．
youtube API使ってmyplaylistの一覧をjsonデータとして取得し，
pecoを使って選択したものをmpvで再生する．
また，ランダムに順番を変更したplaylistを作成してmpvで連続再生できるようにもした．


## 前提
youtube APIが使えるようAPIキーを取得している必要がある．

## how to use

```sh
git clone https://github.com/fhiyo/youtube_myPlayList
```

でcloneした後，settings/MyPlaylistId.pyのmy\_playlist\_idの値をを自分のプレイリストのIDに変更して
play.shかrandomContainuousPlayback.shを実行する．


## 使用しているソフトウェア
- peco
- mpv


