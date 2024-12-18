import asyncio
import datetime
import time
from datetime import datetime  
import pandas as pd


class NewCase:
    def __init__(self, page, df1, df2):
        self.page = page
        self.df1 = df1  
        self.df2 = df2      

    def get_value(self, df, key):
        return df[df['KEY'] == key]['VALUE'].values[0]
    

    async def fill_company_information(self):

        # Click 'SME' button
        await self.page.locator('//*[@id="navbarSupportedContent"]/ul/ul[4]').click()

        # Click 'New Quotation' Button
        await self.page.locator('//*[@id="Repeater2_Repeater2_3_lbl_User_0"]').click()

        # Fill in the Company Name from Sheet1
        await self.page.locator("#ContentBoady1_txt_CompanyName").fill(self.get_value(self.df1, "Company Name"))
        await asyncio.sleep(0.5) 
        print("Company")

        # Businesss Nature from Sheet1
        await self.page.select_option("#ContentBoady1_ddl_buisnessNature", "Other Services & Activities")
        await asyncio.sleep(0.5) 
        print('Businesss Nature')

        # Emirates from Sheet1
        await self.page.locator("#ContentBoady1_ddl_City").select_option("1")
        await asyncio.sleep(0.5) 
        print("Emirates")

        # City from Sheet1
        await self.page.locator("#ContentBoady1_txt_location").fill(self.get_value(self.df1,"City"))
        await asyncio.sleep(0.5) 
        print("City")

        # Contact Person from Sheet1
        await self.page.locator("#ContentBoady1_txt_contactperson").fill(self.get_value(self.df1,"Contatct Person"))
        await asyncio.sleep(0.5) 
        print("Contact person")

        # Contact Number from Sheet1
        contact_number = str(self.get_value(self.df1, "Contact  Number"))
        await self.page.locator("#ContentBoady1_txt_ContactNumber").fill(contact_number)
        await asyncio.sleep(0.5) 
        print("Contact Number")

        # Email from Sheet1
        await self.page.locator("#ContentBoady1_txt_email").fill(self.get_value(self.df1,"Email"))
        await asyncio.sleep(0.5) 
        print("Email")

        # Previous Insurance Company Name from Sheet1
        await self.page.locator("#ContentBoady1_txt_preInsur").fill(self.get_value(self.df1,"Contatct Person"))
        await asyncio.sleep(0.5) 
        print("Previous Insurance Company Name")

        # Target Premium Previous Insurance from Sheet1
        target_premium = str(self.get_value(self.df1,"Target Premium"))
        await self.page.locator("#ContentBoady1_txt_targetPrem").fill(target_premium)
        await asyncio.sleep(0.5) 
        print("Target premium")

        # New-Renew from Sheet1
        new_renew = str(self.get_value(self.df1,"New-Renew"))
        await self.page.locator("#ContentBoady1_ddl_NewRenew").select_option(new_renew)
        await asyncio.sleep(0.5) 
        print("New/Renew")

        await self.page.locator("#ContentBoady1_btn_submit").click()

        file_upload_locator = self.page.locator("#ContentBoady1_fileUpload_member")
        try:
            await asyncio.sleep(2)
            await file_upload_locator.wait_for(state="visible", timeout=15000)
            await file_upload_locator.set_input_files("D:\\AlgoSpring\\python\\ISON\\MemberUpload - IsonSecure and Dubaicare.xlsx")
            print("File uploaded successfully")
        except TimeoutError as e:
            print(f"Timeout Error: {e}")
        except Exception as e:
            print(f"Failed to upload file: {e}")

        # click Upload button
        await self.page.locator("#ContentBoady1_but_uploadUpload").click()
        await asyncio.sleep(0.5)

        # click Next button
        await self.page.locator("#ContentBoady1_btn_submit").click()

#-------------------------------------------Product Details----------------------------------------        

        # Extract the date from the dataframe
        date_value = self.get_value(self.df1, "Effective from")
        
        # Check if date_value is already a datetime object
        if isinstance(date_value, datetime):
            date_obj = date_value  # It's already a datetime object
        else:
            # Parse the date string into a datetime object if it's a string
            date_obj = datetime.strptime(date_value, "%m/%d/%Y")
        
        # Format the date into the desired format
        formatted_date = date_obj.strftime("%d-%b-%Y")

    # Wait for the date picker element to be available
        date_input_selector = "#ContentBoady1_Txt_pSdate"
        await self.page.wait_for_selector(date_input_selector, timeout=5000)

        # Remove the 'disabled' attribute using JavaScript
        await self.page.evaluate(f"document.querySelector('{date_input_selector}').removeAttribute('disabled');")

        # Fill the date input with the desired date
        await self.page.fill(date_input_selector, formatted_date)

        # Optionally, trigger the 'change' event if needed
        await self.page.evaluate(f"document.querySelector('{date_input_selector}').dispatchEvent(new Event('change'));")

        await asyncio.sleep(4)


