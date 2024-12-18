import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from login import Login
from newCase import NewCase
from categories1 import Categories1
from categories2 import Categories2
from categories3 import Categories3

async def main():
   
    file_path = "D:\\AlgoSpring\\python\\ISON\\ISON.xlsx"
    df1 = pd.read_excel(file_path, sheet_name="Sheet1") 
    df2 = pd.read_excel(file_path, sheet_name="Sheet2") 

    # Extract unique categories
    unique_categories_letters = sorted(df2['Category'].unique().tolist())  
    print(f"Unique categories in letters: {unique_categories_letters}")
  

    browser = None 
    try:
        async with async_playwright() as playwright:
            # Launch the browser
            browser = await playwright.chromium.launch(headless=False)
            context = await browser.new_context()
            context.set_default_timeout(60000)
            page = await context.new_page()

            # Login and process
            while True:
  
                login = Login(page)
                if (await login.perform_login("lokesh.l@gargash", "Lokesh.l@#2g")):

                    new_case = NewCase(page, df1, df2)
                    await new_case.fill_company_information()

                     # Process categories based on unique categories in letters
                    if 'A' in unique_categories_letters:
                        cat1 = df2[df2['Category'] == 1]
                        categories1 = Categories1(page, df2, cat1)
                        await categories1.categories1_information()

                    if 'B' in unique_categories_letters:
                        cat2 = df2[df2['Category'] == 2]
                        categories2 = Categories2(page, df2, cat2)
                        await categories2.categories2_information()

                    if 'C' in unique_categories_letters:
                        cat3 = df2[df2['Category'] == 3]
                        categories3 = Categories3(page, df2, cat3)
                        await categories3.categories3_information()

                        await asyncio.sleep(3)

                    break

    finally:
        if browser:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
