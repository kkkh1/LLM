# WSLについて
- powershell or commandpromptで、
  ```wsl --install```
- Windowsの機能をオンまたはオフにする　を検索し、Linuxサブシステムにチェックをいれる。

# 権限付与について、Linux
- 特権昇格: Sudo su
- ログ検索　：　```tail -n 1 /data/cowrie/log/cowrie.json```
- ```scp -r -P 66666 tsec@192.168.16.7:/data/log ./``` -rでディレクトリ設定
- Chmod はファイルに権限を付与するコマンド、０からま７までで、所有者、グループ権限その他のユーザ権限の順番で例、chmod 777 、実行権限はxで、chmod +xですべてに実行権限付与 
- カレントディレクトリ配下すべてに（再帰的に）同じパーミッションを反映させたいとき、
- chmod -R 644 ./
- [参考サイト](https://qiita.com/ntkgcj/items/6450e25c5564ccaa1b95)

# GPU,nvidia全般
- ホストPCに[Nvidia_driver](https://www.nvidia.co.jp/Download/index.aspx?lang=jp)からダウンロード
- 実行環境（WSLなど）に、[Cuda](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)をインストールする。
- ```nvcc -V```で導入されているか確認
- ```nvidia-smi -l``` nvidiaドライバの確認
  
