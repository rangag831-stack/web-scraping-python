import pandas as pd
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=samsung+5g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+5g+mobile%7CMobiles&requestId=e3d483a6-7ae7-4ebb-be76-6d8dcc781509&as-searchtext=samsung%205g%20mobile")
print(response)

soup=BeautifulSoup(response.content,'html.parser')
# raw html received from a website and convert it into a structure that python can easily search and extract data from 
# a person convert raw html code into a structured format so that python can understand navigate and extract and extract information from it

# print(soup)

names=soup.find_all("div",class_="RG5Slk")
## This code searches for all div tags with the class name "RG5Slk" and stores the matching elements in the names variable .
# print(names)

name=[] ## This code extracts the text from each element in names, appends it to the name list, and prints all the extracted names.
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)

rating=soup.find_all("div",class_="MKiFS6")## This code finds all div elements with the class name "MKiFS6" and stores them in the rating variable.

#print(rating)  ## This line prints all the extracted rating elements.


# Create an empty list to store the extracted ratings
rate = []

# Loop through the first 10 elements in the rating list
for i in rating[0:10]:
    # Extract the text from each element
    d = i.get_text()

    # Add the extracted text to the rate list
    rate.append(d)

# Print all the extracted ratings
# print(rate)

price=soup.find_all("div",class_="hZ3P6w DeU9vF")
# print(price)
# Create an empty list to store the extracted product prices
prices = []

# Loop through the first 10 elements in the price list
for i in price[0:10]:
    # Extract the text from each price element
    d = i.get_text()

    # Add the extracted price to the prices list
    prices.append(d)
result=[i.replace("₹"," ") for i in prices]


# # Print all the extracted product prices
# print(result)




# Find all image tags with the class name "UCc1lI"
image = soup.find_all("img", class_="UCc1lI")
# print(image)

# Create an empty list to store image URLs
images = []

# Loop through the first 10 image elements
for i in image[0:10]:
    # Extract the image URL from the src attribute
    data = i.get("src")

    # Add the image URL to the images list
    images.append(data)

# Print all extracted image URLs
# print(images)



# Create an empty DataFrame
df = pd.DataFrame()

# Add mobile names to the Name column
df["Name"] = name

# Add mobile prices to the Price column
df["Price"] = result

# Add mobile ratings to the Ratings column
df["Ratings"] = rate

# Add mobile image URLs to the Image column
df["Image"] = images

# Display the DataFrame
print(df)

# Save the DataFrame as a CSV file
df.to_csv("mobile.csv")

