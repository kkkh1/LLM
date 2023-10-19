import subprocess
import re

# Nmapコマンドを実行して結果を取得
def run_nmap_scan(ip_address):
    try:
        # Nmapコマンドを実行
        command = ["nmap", "-sV", "-O", "-sC", ip_address]
        result = subprocess.check_output(command, universal_newlines=True)

        # Nmapの結果を返す
        print(result)
        result1=result.encode("utf-8")

        return result1
    except subprocess.CalledProcessError as e:
        # エラーが発生した場合
        print(f"Error: {e}")
        return None

# Nmapスキャン結果を解析して出力
def parse_nmap_result(nmap_result):
    # 改行で結果を分割
    result_lines = nmap_result.split('\n')

    # サービス情報を格納するリスト
    services = []

    # ポートとサービス名を抽出
    for line in result_lines:
        match = re.search(r'(\d+/tcp|udp)\s+open\s+([^\s]+)\s+(.*)', line)
        if match:
            port = match.group(1)
            service = match.group(2)
            version = match.group(3)
            services.append((port, service, version))

    # サービスを優先度順にソート
    services.sort(key=lambda x: x[2])

    # 出力
    for service in services:
        print(f"{service[1]} ?{service[2]}?")

# IPアドレス
target_ip = "10.0.0.5"

# Nmapスキャンを実行して結果を取得
nmap_result = run_nmap_scan(target_ip)

if nmap_result:
    # Nmapスキャン結果を出力
    print(nmap_result)

    # Nmap結果を解析してサービス情報を出力
    parse_nmap_result(nmap_result)
else:
    print("Nmapスキャンに失敗しました。")
