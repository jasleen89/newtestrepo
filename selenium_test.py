# Importing Selenium WebDriver to control a web browser
# Importing By to locate elements in the browser

from selenium import webdriver  
import pymysql  
from selenium.webdriver.common.by import By  

# Launch the browser using Chrome
driver = webdriver.Chrome()  

# Open the web app's login page (Flask app running locally)
driver.get('http://127.0.0.1:5000/login')  # Access the login page of the Flask app

# Interact with the login form
username = driver.find_element(By.NAME, 'username')  # Find the username input field
password = driver.find_element(By.NAME, 'password')  # Find the password input field

# Simulate user typing 'jkaur' into the username field and 'testdatabase' into the password field
username.send_keys('jkaur')  # Enter username 'jkaur'
password.send_keys('1234')  # Enter password 'testdatabase'

# Submit the login form
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # Click the submit button (assuming the form has this submit button type)

# Close the browser after interacting with the login form
driver.quit()

# Now, verify the user data by connecting to the MySQL database
db = pymysql.connect(user='root', password='jasleen123', host='localhost', database='newdb')
cursor = db.cursor()

# Query the database to retrieve the user data for the user 'jkaur'
cursor.execute("SELECT * FROM users WHERE username = 'jkaur'")
user_data = cursor.fetchone()  # Fetch the first matching result from the query

# Print the fetched user data to check it
print(user_data)

# Verify that the username fetched from the database matches 'jkaur'
assert user_data[1] == 'jkaur', "Username does not match!"  # Check if the username in the DB matches

# Close the database connection after the verification
db.close()

# Print the success message if the test passed
print("Test passed: User data is correct.")
