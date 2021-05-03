from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
cwd = os.getcwd()

opts = Options()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument("--start-fullscreen")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
path_browser = f"{cwd}\chromedriver.exe"
print("[*] Automation Bitbucket Registration + Import Repository")
print("[*] Author: RJD")

def fill_repo(email, link_repo):
    sleep(10)
    try:
        element = wait(browser,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_url')))
        element.send_keys(link_repo)
        #id_project_name
    except:
        reload(email, password) 
    try:
        try:
            element = wait(browser,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_project_name')))
            element.send_keys('Project')
            print(f"[*] [ {email} ] Input Project Name*")
        except:
            wait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#s2id_id_project'))).click()
            print(f"[*] [ {email} ] Input Project Name**")
            sleep(5)
    except:
        pass
    try:
        try:
            wait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#select2-drop > ul > li.select2-results-dept-0.select2-result.select2-result-selectable.select2-highlighted'))).click()
        except:
            wait(browser,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-drop"]/ul/li[1]/div/span[2]'))).click()
    except:
        pass  
    #id_name
    sleep(0.5)
    wait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#import-form > div.buttons-container > div > button'))).click()
    sleep(5)

def import_repo(email, password):
    browser.save_screenshot("IMPORT_REPO_2.png")
 
    file_list = "link_repo.txt"
    myfile = open(f"{cwd}/{file_list}","r")
    link_repo = myfile.read()
    print(f"[*] [ {email} ] URL Repo: {link_repo}")
    fill_repo(email, link_repo)
    try:
        browser.save_screenshot("COMPLETE.png")
        print(f"[*] [ {email} ] Loading Import...")
        sleep(15)
        get_title = wait(browser,120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div.css-kyhvoj > div.css-e48442 > div > div > div > div > header > div > div > div > div.sc-hmXxxW.hsWFox > h1'))).text
        print(f"[*] [ {email} ] Import Repo Success: {get_title}")
        with open('SuccessIMPORT.txt','a') as f:
            f.write('{0}|{1}|{2}\n'.format(email,password,link_repo))
        browser.quit()
    except:
        print(f"[*] [ {email} ] Import Repo Failed!")
        import_repo(email, password)
    
def set_username(email, password):
    sleep(20)
    browser.save_screenshot("BEFORE_SET_USERNAME.png")
    browser.get('https://bitbucket.org/atlassianid/bb-signup/?next=/account/signin/?redirectCount=1&next=%2Fdashboard%2Foverview')
    print(f"[*] [ {email} ] Set Username")
    sleep(5)
    browser.save_screenshot("SET_USERNAME.png")
    try:
        element = wait(browser,25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-username-field"]')))
        get_user = email.split('@')
        get_number = str(random.randint(10, 99))
        username = get_user[0]+get_number
        element.send_keys(username)
        element.send_keys(Keys.ENTER)
        print(f"[*] [ {email} ] Success Set Username")
        browser.save_screenshot("SUCCESS_SET.png")
    except:
        print(f"[*] [ {email} ] Skip Set Username")

    print(f"[*] [ {email} ] IMPORT REPO")
    sleep(5)
    browser.get('https://bitbucket.org/repo/import?workspace')
    sleep(5)
    browser.save_screenshot("IMPORT_REPO.png")
    import_repo(email, password)    

def reload(email, password):
    browser.get('https://bitbucket.org/repo/import?workspace')
    sleep(5)
    browser.save_screenshot("IMPORT_REPO.png")
    import_repo(email, password)  

def accept():
    sleep(0.5)
    browser.save_screenshot("GET_ACCEPT.png")
    wait(browser,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maia-main > form > p > input"))).click()

def get_started():
    sleep(5)
    wait(browser,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.Yi > div.Yi-Jl > button"))).click()
    sleep(5)
    wait(browser,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.T-P.bgX.Yv > div.T-P-aut-UR.T-P-aut"))).click()
    
def login_email(email, password):
    
    global element
    global browser
     
    # try:        
    sleep(5)
    browser.save_screenshot("ProcessLOGIN_0.png")
 
    element = wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#identifierId")))
    element.send_keys(email)
        
    sleep(0.5)
    element.send_keys(Keys.ENTER) 
    sleep(3)  
    element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    
    element.send_keys(password)
    sleep(0.5)
    element.send_keys(Keys.ENTER)  
    browser.save_screenshot("beforeAFTERLOGIN.png")
    try: 
        wait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#accept"))).click()
    except:
        pass
    try:
        test_saja = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didnt-get-an-email-start-again"]/span/span/span'))).click()
        test_saja.sendKeys(Keys.PAGE_DOWN);
    except:
        browser.refresh()
        sleep(5)
        test_saja = wait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="didnt-get-an-email-start-again"]/span/span/span'))).click()
     
    try:
       sleep(2)
       wait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ' #\34 c7e890a-96f1-4769-ac22-715ac8bcf7cf > div > div.sc-dVhcbM.bRszlg > button > span'))).click()
    except:
       pass
    
    sleep(5)
    browser.execute_script("window.open('https://mail.google.com/mail/?ui=html');")
    browser.switch_to.window(browser.window_handles[1])
    get_otp(email,password)
        
    # except Exception as e:
    #     sleep(2)
    #     print(e)

def extract_otp(email, password):
    global filter_otp
    try:
        browser.save_screenshot("GET_OTP_BEFORE_TIGA.png")
        sleep(2)
        filter_otp = wait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > table:nth-child(16) > tbody > tr > td:nth-child(2) > table:nth-child(1) > tbody > tr > td:nth-child(2) > table:nth-child(4) > tbody > tr > td > table:nth-child(5) > tbody > tr:nth-child(4) > td > div > div > table > tbody > tr > td > div > div > table > tbody > tr > td > h3"))).text 
        print(f"[*] [ {email} ] Extract OTP")
    except:
        try:
            print(f"[*] [ {email} ] Trying to Extract OTP")
            filter_otp = browser.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[7]/tbody/tr[4]/td/div/div/table/tbody/tr/td/div/div/table/tbody/tr/td/h3").text 
        except:
            print(f"[*] [ {email} ] Extract OTP Failed, Try Again!")
            browser.get('https://mail.google.com/mail/?ui=html')
            otp_next(email, password)

def otp_next(email,password):
    sleep(5)
    # try:#select2-drop > ul > li.select2-results-dept-0.select2-result.select2-result-selectable.select2-highlighted
    browser.save_screenshot("GET_OTP_BEFORE_SATU.png")
    try:
        browser.save_screenshot("GET_OTP_BEFORE_DUA.png")
        wait(browser,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > table:nth-child(16) > tbody > tr > td:nth-child(2) > table:nth-child(1) > tbody > tr > td:nth-child(2) > form > table.th > tbody > tr:nth-child(1) > td:nth-child(3) > a > span"))).click()
        print(f"[*] [ {email} ] Open Email")
    except:
 
        print(f"[*] [ {email} ] Trying to Open Email")
        tsest = wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a/span"))) 
        tsest.send_keys(Keys.ENTER)
    
    extract_otp(email, password)     
    print(f"[*] [ {email} ] OTP: {filter_otp} ")
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    sleep(0.5)
    input_otp(email, password, filter_otp)

def get_otp(email, password):
    sleep(10)
    browser.save_screenshot("GET_OTP_BEFORE.png")
    print(f"[*] [ {email} ] Get OTP")
 
    try:
        accept()
    except:
        pass
    otp_next(email,password)

    # except:
    #     reload(email)
def input_otp(email, password, filter_otp):
    print(f"[*] [ {email} ] Go To Input OTP")
    enter_otp = wait(browser,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="code"]')))
    
    sleep(0.5)
    enter_otp.send_keys(filter_otp)
    sleep(0.5)
    browser.save_screenshot("INPUT_OTP.png")
    try:    
        wait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-submit"]/span/span/span'))).click()
        print(f"[*] [ {email} ] Success Input OTP")
    except:
        try:
            browser.refresh()
            enter_otp.send_keys(filter_otp)
            sleep(1)
            wait(browser,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-submit"]/span/span/span'))).click()
            print(f"[*] [ {email} ] Success Input OTP")
        except:
            enter_otp.send_keys(Keys.ENTER)
    try:
        set_username(email,password)
    except:
        browser.quit()

def regis(k):
    global browser
    global element
     
    k = k.split("|")
    email = k[0]
    password = k[1]
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc, executable_path=path_browser)
    browser.get('https://id.atlassian.com/signup')
    click_element_gsuite(email,password)

def click_element_gsuite(email,password):
    element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="google-auth-button"]/span/span/span')))
    element.click() 
    sleep(5)
    print(f"[*] [ {email} ] Login google")
    browser.save_screenshot("ID_at.png") 
    login_email(email,password)

def main():
    file_list_akun = "list_akun.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split() 
    for i in list_accountsplit:
        regis(i)
        
    print("[*] AUTOMATION SUCCESSFULLY COMPLETE!")

main()
