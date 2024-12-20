import undetected_playwright as playwright
from PIL import Image, ImageEnhance
import pytesseract
import time
import io
import asyncio

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sudeepa.w\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class Login:
    def __init__(self, page):
        self.page = page

    async def perform_login(self, username: str, password: str):
        # while True:
            try:
                # Go to the login page and wait for it to load
                await self.page.goto("https://ison.dubins.ae/")
                await self.page.wait_for_load_state('networkidle')

                # Enter login credentials
                await self.page.locator("#txt_userName").fill(username)
                await self.page.locator("#txt_password").fill(password)

                # Take screenshot of the CAPTCHA image with a longer timeout
                captcha_image = await self.page.locator("div.col-sm-6 img").screenshot()

                # Preprocess image before OCR
                image = Image.open(io.BytesIO(captcha_image))
                image = image.convert('L')  # Convert to grayscale
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(2)  # Increase the contrast

                captcha_text = pytesseract.image_to_string(image)
                print("CAPTCHA is:", captcha_text.strip())

                # Fill in the CAPTCHA text
                await self.page.locator("#txt_captcha").fill(captcha_text.strip())

                # Wait for the button to be clickable
                await self.page.locator("#btn_proceed").wait_for(state="visible")
                await self.page.locator("#btn_proceed").click()

                # Explicitly wait for the next page or element to load
                await asyncio.sleep(3)

                # Check if the element is visible to determine success
                if await self.page.locator('//*[@id="navbarSupportedContent"]/ul/ul[4]').is_visible():
                    print("Login successful!")
                    return True

                else:
                    print("Retrying CAPTCHA...")
                    await asyncio.sleep(1)  # Wait a bit before retrying
                    return False
         

            except Exception as e:
                print(f"Failed to capture or read CAPTCHA: {e}")
                await asyncio.sleep(3)  # Optionally, wait before retrying on error