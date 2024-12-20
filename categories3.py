import asyncio
import time
import os

class Categories3:
    def __init__(self, page, df2, cat3):
        self.page = page
        self.df2 = df2

    def get_value(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df2[column_name].values[1])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def categories3_information(self):
        
        # Plan
        plan = self.get_value("Plan")
        await self.page.select_option('#ContentBoady1_ddl_plan3', value=plan)
        time.sleep(3)

        # Network
        network = self.get_value("Network")
        await self.page.select_option('#ContentBoady1_ddl_network3', value=network)
        time.sleep(3)

        # Dental
        dental = self.get_value("Dental")
        await self.page.select_option('#ContentBoady1_ddl_Dentben3', value=dental)
        time.sleep(1)

        # Optical
        optical = self.get_value("Optical")
        await self.page.select_option('#ContentBoady1_ddl_Optben3', value=optical)        
        time.sleep(1)

        # Psychiatry
        psychiatry = self.get_value("Psychiatry")
        await self.page.select_option('#ContentBoady1_ddl_psch3', value=psychiatry)             
        time.sleep(1)

        # physiotherapy
        physiotherapy = self.get_value("Physio")
        await self.page.select_option('#ContentBoady1_ddl_phy3', value=physiotherapy)             
        time.sleep(1)

        # Alternative Medicine
        alternative_medicine = self.get_value("Alternative Medicine")
        await self.page.select_option('#ContentBoady1_ddl_alterMedben3', value=alternative_medicine)           
        time.sleep(5)

        # PreExisting and Chronic Conditions
        preExisting = self.get_value("Pre-existing")
        await self.page.select_option('#ContentBoady1_ddl_preexisting3', value=preExisting)           
        time.sleep(0.5)

        # Click Get quote button
        await self.page.locator('#ContentBoady1_btn_quote').click()

        # Download the Quotation
        download_path = 'D:\\AlgoSpring\\python\\ISON'

        # Ensure the download directory exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        try:
            # Wait for the download to start
            async with self.page.expect_download(timeout=120000) as download_info:
                # Click the download button
                await self.page.locator('#ContentBoady1_btn_submit').click()

                # Wait for the download to complete and save it to the specified path
                download = await download_info.value
                download_path_full = os.path.join(download_path, "quotation1.pdf")
                await download.save_as(download_path_full)
                print(f"Downloaded quotation PDF to: {download_path_full}")

        except asyncio.TimeoutError:
            print("Error: Timeout exceeded while waiting for the download.")
        except Exception as e:
            print(f"Unexpected error during download: {e}")

        await asyncio.sleep(10)  
