import asyncio
import undetected_playwright as playwright
from twocaptcha import TwoCaptcha
import aiofiles

class Login:
    def __init__(self, page):
        self.page = page

    async def perform_login(self, username: str, password: str):
        try:
            await self.page.goto("https://ison.dubins.ae/")
            await self.page.wait_for_load_state('networkidle')

            await self.page.locator("#txt_userName").fill(username)
            await self.page.locator("#txt_password").fill(password)

            captcha_image = await self.page.locator("#img").screenshot()

            # Asynchronously write the screenshot to a file
            async with aiofiles.open('captcha.png', 'wb') as file:
                await file.write(captcha_image)

            # Initialize TwoCaptcha solver
            solver = TwoCaptcha('12054431ec2fc8637b7ca76cd31c9401')

            # Solve the CAPTCHA using the file
            result = await asyncio.to_thread(solver.normal, 'captcha.png')
            captcha_code = result['code']
            print("Captcha Code :", captcha_code)

            await self.page.locator("#txt_captcha").fill(captcha_code)
            await self.page.locator("#btn_proceed").wait_for(state="visible")
            await self.page.locator("#btn_proceed").click()

            await asyncio.sleep(3)

            if await self.page.locator('//*[@id="navbarSupportedContent"]/ul/ul[4]').is_visible():
                print("Login successful!")
                return True
            else:
                print("Retrying CAPTCHA...")
                await asyncio.sleep(1)
                return False

        except Exception as e:
            print(f"Failed to capture or read CAPTCHA: {e}")
            await asyncio.sleep(3)
