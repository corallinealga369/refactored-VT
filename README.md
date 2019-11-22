# refactored-VT
This is a spot for scripts I write involving the VirusTotal API

# Requirements
You will need: 

A VirusTotal API key

	python3

	requests

	json

	io

	tarfile

Use pip to install these if you don't have them already like so: 

	pip3 install json

# About the API Key

In this script, I have imported my VirusTotal API key from another file so that I don't have to wory about accidentally sharing it on GitHub. In order to do this: 

	1.Sign up with VirusTotal to get an API key
	
	2.Save this key in an API variable in the script or in a seperate file
	
	3.If you save it in a seperate file, you will need to import it just like 'json' or other modules. 
		Your apikey file should be saved as a python file, which can then be imported like so: 
		
			from <filename> import apikey
