

import random
import pyautogui

# کاراکترهای مجاز برای رمز عبور
chare = "abcdfghijklmnopqrstuvwxyz0123456789"
allcher = list(chare)

# دریافت رمز عبور از کاربر
pwd = pyautogui.password("enter a password: ")

# متغیر برای ذخیره رمز عبور تصادفی
samlp_pwd = ""

# حلقه تا زمانی که رمز عبور تصادفی با رمز عبور ورودی برابر نشود
while samlp_pwd != pwd:
    # تولید یک رمز عبور 
    
    
    samlp_pwd = ''.join(random.choices(allcher, k=len(pwd)))
    
    print("<===============" + samlp_pwd + "===============>")

# در صورتی که رمز عبور درست باشد
print("your password is: " + samlp_pwd)
















