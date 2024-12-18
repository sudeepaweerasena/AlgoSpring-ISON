import asyncio
import time
from categories2 import Categories2

class Categories1:
    def __init__(self, page, df2, cat1):
        self.page = page
        self.df2 = df2

    def get_value(self, column_name):
        try:
            # Fetch value from the specific column and convert to string
            return str(self.df2[column_name].values[0])
        except KeyError:
            print(f"KeyError: '{column_name}' column not found in DataFrame.")
            return None
        except IndexError:
            print(f"IndexError: No data found in column '{column_name}'.")
            return None

    async def categories1_information(self):
        
        # TPA
        tpa = self.get_value("TPA")
        print(tpa)
        await self.page.select_option('#ContentBoady1_ddl_tpa1', value=tpa)
        time.sleep(4)

        # Plan
        plan = self.get_value("Plan")
        await self.page.select_option('#ContentBoady1_ddl_plan1', value=plan)
        time.sleep(3)

        # Network
        network = self.get_value("Network")
        await self.page.select_option('#ContentBoady1_ddl_network1', value=network)
        time.sleep(3)

        # Dental
        dental = self.get_value("Dental")
        await self.page.select_option('#ContentBoady1_ddl_Dentben1', value=dental)
        time.sleep(1)

        # Optical
        optical = self.get_value("Optical")
        await self.page.select_option('#ContentBoady1_ddl_Optben1', value=optical)        
        time.sleep(1)

        # Psychiatry
        psychiatry = self.get_value("Psychiatry")
        await self.page.select_option('#ContentBoady1_ddl_psch1', value=psychiatry)             
        time.sleep(1)

        # physiotherapy
        physiotherapy = self.get_value("Physio")
        await self.page.select_option('#ContentBoady1_ddl_phy1', value=physiotherapy)             
        time.sleep(1)

        # Alternative Medicine
        alternative_medicine = self.get_value("Alternative Medicine")
        await self.page.select_option('#ContentBoady1_ddl_alterMedben1', value=alternative_medicine)           
        time.sleep(1)

        # PreExisting and Chronic Conditions
        preExisting = self.get_value("Pre-existing")
        await self.page.select_option('#ContentBoady1_ddl_preexisting1', value=preExisting)           
        time.sleep(0.5)
