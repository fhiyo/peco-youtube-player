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
git clone git@gist.github.com:3aea7faa2ebf78ee9a560248a6ee07b7.git
```

でcloneした後，get\_youtube\_playlist.pyのMY\_PLAYLIST\_IDを自分のプレイリストのIDに変更して
play.shかrandomContainuousPlayback.shを実行する．


### 使用しているソフトウェア
- peco
- mpv


