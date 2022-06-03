# PostmanToJMeterConvertor
Code that converts your postman collection in to JMeter script.

## Pre-requisites
Python should be installed on system where this code will run.
To verify python installation you can run "python -V" command in command prompt it should return python version installed, if its not returning python version, please fix your python installation.

## How do I get set up?
1. Clone the repository on your local system where python is installed.
2. Verify requests are working as expected in Postman.
3. Export Postman collection along with global and/or environment variables if any. Keep these exports in one folder.
4. Rename Postman files respectively to `collection.json`, `environment.json`, `globals.json`.
5. Run command in command line on your machine "python P2JConvert_v2203.py". It will return input prompt asking for path where exports are parked.
6. Provide the full path and press enter.
7. In case of successful conversion, it should return successful message along with path to JMETER script.

## Recommanded best practices to avoid issues. 
1. Add headers explicitly even if same header is covered in hidden Postman default header. Hidden headers will not be exported in collection hence need to add explicitly.
2. While exporting environment and global variables click on persist all otherwise it will export blank values.

 
## Who do I talk to?
In case of any issues, bugs or feedback please reach out to me on aniketaghodke@gmail.com
