from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class FormTester:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, email, phone):
        """
        Fill the form with given details and submit.
        """
        try:
            # Locate fields
            first_name_input = self.driver.find_element(By.ID, "firstName")
            last_name_input = self.driver.find_element(By.ID, "lastName")
            email_input = self.driver.find_element(By.ID, "userEmail")
            phone_input = self.driver.find_element(By.ID, "userNumber")
            submit_button = self.driver.find_element(By.ID, "submit")

            # Clear and enter data
            first_name_input.clear()
            last_name_input.clear()
            email_input.clear()
            phone_input.clear()

            first_name_input.send_keys(first_name)
            last_name_input.send_keys(last_name)
            email_input.send_keys(email)
            phone_input.send_keys(phone)

            # Submit form
            submit_button.click()
            time.sleep(1)

            # Capture success or error message
            success = self.driver.find_elements(By.CLASS_NAME, "modal-title")
            if success:
                print(f"[SUCCESS] Form submitted successfully for {first_name} {last_name}")
                self.driver.find_element(By.ID, "closeLargeModal").click()
            else:
                print(f"[FAILED] Form submission failed for {first_name} {last_name}")

        except Exception as e:
            print(f"[ERROR] Exception while submitting form: {e}")

    def close(self):
        self.driver.quit()

# ------------------- MAIN SCRIPT -------------------

if __name__ == "__main__":
    tester = FormTester("https://demoqa.com/automation-practice-form")

    # Test with valid data
    tester.fill_form("John", "Doe", "john.doe@example.com", "9876543210")

    # Test with invalid email
    tester.fill_form("Alice", "Smith", "alice.smithexample.com", "1234567890")

    # Test with invalid phone
    tester.fill_form("Bob", "Brown", "bob.brown@example.com", "abcd1234")

    # Close browser
    tester.close()