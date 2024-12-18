import asyncio
import time

class Categories2:
    def __init__(self, page, df2, cat2):
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

    async def categories2_information(self):
        
        # Plan
        plan = self.get_value("Plan")
        await self.page.select_option('#ContentBoady1_ddl_plan2', value=plan)
        time.sleep(3)

        # Network
        network = self.get_value("Network")
        await self.page.select_option('#ContentBoady1_ddl_network2', value=network)
        time.sleep(3)

        # Dental
        dental = self.get_value("Dental")
        await self.page.select_option('#ContentBoady1_ddl_Dentben2', value=dental)
        time.sleep(1)

        # Optical
        optical = self.get_value("Optical")
        await self.page.select_option('#ContentBoady1_ddl_Optben2', value=optical)        
        time.sleep(1)

        # Psychiatry
        psychiatry = self.get_value("Psychiatry")
        await self.page.select_option('#ContentBoady1_ddl_psch2', value=psychiatry)             
        time.sleep(1)

        # physiotherapy
        physiotherapy = self.get_value("Physio")
        await self.page.select_option('#ContentBoady1_ddl_phy2', value=physiotherapy)             
        time.sleep(1)

        # Alternative Medicine
        alternative_medicine = self.get_value("Alternative Medicine")
        await self.page.select_option('#ContentBoady1_ddl_alterMedben2', value=alternative_medicine)           
        time.sleep(1)

        # PreExisting and Chronic Conditions
        preExisting = self.get_value("Pre-existing")
        await self.page.select_option('#ContentBoady1_ddl_preexisting2', value=preExisting)           
        time.sleep(0.5)

