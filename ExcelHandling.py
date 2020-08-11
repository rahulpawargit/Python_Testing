import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
Fname = driver.find_element(By.ID, 'Form_submitForm_FirstName')
Lname = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
JTitle = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
eCount = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
Cname = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
Ind = driver.find_element(By.ID, 'Form_submitForm_Industry')
Contact = driver.find_element(By.ID, 'Form_submitForm_Contact')
country = driver.find_element(By.ID, 'Form_submitForm_Country')

workbook = xlrd.open_workbook("excelread.xlsx")
sheet = workbook.sheet_by_name("Sheet1")

rowcount = sheet.nrows
print(rowcount)

colscount = sheet.ncols
print(colscount)

for currentrow in range (1, rowcount):

    URL = str(sheet.cell_value(currentrow, 0))
    Firstname = str(sheet.cell_value(currentrow, 1))
    Lastname = str(sheet.cell_value(currentrow, 2))
    Email = str(sheet.cell_value(currentrow, 3))
    JobTitle = str(sheet.cell_value(currentrow, 4))
    Noofemp = str(sheet.cell_value(currentrow, 5))
    company = str(sheet.cell_value(currentrow, 6))
    Industy = str(sheet.cell_value(currentrow, 7))
    Phonenumber = str(sheet.cell_value(currentrow, 8))
    conuty = str(sheet.cell_value(currentrow, 9))

    # print(URL +" "+Firstname )
    url.clear()
    url.send_keys(URL)
    Fname.clear()
    Fname.send_keys(Firstname)
    Lname.clear()
    Lname.send_keys(Lastname)
    email.clear()
    email.send_keys(Email)
    # JTitle.clear()
    JTitle.send_keys(JobTitle)
    # eCount.clear()
    eCount.send_keys(Noofemp)
    Cname.clear()
    Cname.send_keys(company)
    # Ind.clear()
    Ind.send_keys(Industy)
    Contact.clear()
    Contact.send_keys(Phonenumber)
    # country.clear()
    country.send_keys(conuty)

    time.sleep(3)