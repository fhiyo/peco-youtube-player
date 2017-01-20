# youtubeのplaylistをローカルで再生またはランダムで連続再生する

## 概要
youtubeの広告がうっとおしいのでmpvでyoutubeのplaylistを見られるようにした．
youtube API使ってmyplaylistの一覧をjsonデータとして取得し，
pecoを使って選択したものをmpvで再生する．
また，ランダムに順番を変更したplaylistを作成してmpvで連続再生できるようにもした．


## 前提
youtube APIが使えるようAPIキーを取得している必要がある．

## how to use

```sh
git clone git@github.com:fhiyo/peco-youtube-player.git
```

でcloneした後，`settings/MyPlaylistId.py`を作成し，
` my_playlist_id = "<自分のプレイリストのid>"`
を記述する．
保存して終了後，play.shかrandom_containuous_playback.shを実行する．

プレイリストを更新したとき，
`./play.sh --update`のように`--update`のオプションをつけて
実行するとローカルのプレイリストを更新する．


## 使用しているソフトウェア
- peco
- mpv
