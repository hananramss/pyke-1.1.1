import sys


# Using raw string literals
sys.path.append(r'C:\Users\Acer\Downloads\Pyke\pyke-1.1.1\examples\family_relations')

# Import the driver module
import driver


# Run this cell
driver.fc_test('michael_k') 

# Run this cell
driver.fc_test('ryan') 

# Run this cell
driver.fc_test() 

# uses example.krb
driver.test('gary')

# uses bc2_example.krb
driver.general(person1='bruce', person2='david_a', relationship=('father', 'son')) 