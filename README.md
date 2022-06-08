# Postman To JMeter Convertor
Tool that converts your Postman collection in to JMeter script.

## Pre-requisites
Python 3 should be installed on system where this code will run.
To verify python installation you can run "python -V" command in command prompt it should return python version installed, if its not returning python version, please fix your python installation.

## How do I get set up?
1. Clone the repository.
2. Verify requests are working as expected in Postman and keep requests directly under collection without any folders.
3. Export Postman collection along with global and/or environment variables if any. Keep these exports in one folder.
4. Run command in command line on your machine "python P2JConvert_v2207.py". It will return input prompt asking for folder where exports are parked.
5. Provide the folder path and press enter.
6. In case of successful conversion, it should return successful message along with path to JMETER script.

## Recommanded best practices to avoid issues. 
1. Add headers explicitly even if same header is covered in hidden Postman default headers. Hidden headers will not be exported in collection hence need to add explicitly.
2. While exporting environment and global variables click on persist all otherwise it will export blank values.
3. How to export? Read here - https://learning.postman.com/docs/getting-started/importing-and-exporting-data/

 
## Known Issues / Bugs / Future Enhancements
1. Does't support Postman "binary" and "GraphQL" body types. 
   - In case if you have any requests with "binary" and "GraphQL" body types then kindly share Postman collections over email for future enhancement.
   
2. Doesn't support in case Postman collection have folders and subfolders. Need to keep requests directly under collection.
   - No plan for enhancement.

3. Special Characters Handling   

## Who do I talk to?
In case of any issues, bugs or feedback please reach out to me on "aniketaghodke@gmail.com"