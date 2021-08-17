# SerpAPI Data Aquisition
Initially Started this project using the Scholarly Request API. Found that this API did not offer the nesseccary materials for me to complete my coding objectives.
Moved into using SerpAPI to properly web scrape for the required data.


Purpose:
To gather Google Scholar data regarding popular workes cited and the journals in which they were published in. Additionally expanded the project to include the data related to the number of works cited each year after publishing.

My Method:
The code was built using Python and a simple API request format. The author created this data to first send a request to collect the relevant unique Author IDs that are created by Google and return information about the response author's affiliations in order to ensure relevant data retrieval. Next the code sends another request with the Author IDs found in the first request in order to return the information about the works cited and journal publishment information. This final information is returned in a CSV file format.

How the Code works:
I use the Pandas Data library to collect the data from the input file and to make data formatting easier later on. The API returs data in the JSON format which works well with the pandas library and further data formating. The second API request again makes use of taking the previous files csv data to send the more specific request for information. The returned data is then split up into different DataFrames to properly merge the data up at the end. Each itteration will append the DataFrame that is created into a large list of DataFrames which then comes together at the end of the code once it has run for each name on the input file. The data will then output in a csv file format which should display clearly named collumns of the returned data.

How to Run my Code:
This code is built entirly using Python version 3.9.6. This code makes use of the Pandas Library, the SerpAPI library and some fundamental libraries like csv. To make this code work, your input file must have data stored in three collumns named: university, name, projectid. The projectid collumn is largly useless for other works so if you wanted to you could go through my code and delete every refrence to proejctid you find. You will also need to include a text file of your api key stored in a file called secret.txt so that the code can run for you. The first file that you will be working with is the getAuthorID.py file. This file has has hardcoded values for the input file name and output file name so you will need to go into this file to change the name of the input to be what you want it to be and the oputupt should be relevant to your work. It is important to not ethat as of right now the next file you will run requries the output name of the first file to be identical to the input name of the second. Run the first file, getAuthorID.py and make sure that hthe file was created properly. Next it is time to run the second file, getArticles. Remember to wait an hour if you have not purchases a very large throughput plan from SerpAPI. This file should properly create the output csv file that is your final results.

Output File Collumn Names:
university , name , projectid , author_id , affiliations , Article Title , Article Publication , Year of Citation , Number of Citations that Year

Known Issues:
The error handling has been written in however there could still be problems that occur if the API request does not return properly. In addition, this code runs under the assumption that you have purchased a SerpAPI plan which has a large enough throughput to run all of the names at once wihtout maxing out the number. If there are more names in the input file then you will need to break up the input file into chunks that are smaller than what you are paying for.
