import requests

# URL of the audio file to be downloaded
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"

# Path where the audio file will be saved in the current directory
audio_file_path = 'audio_file.mp3'

def download_audio_file(url, file_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        '''
        response.raise_for_status() is a method from the requests library that checks the HTTP 
        response status code.

        If the response was successful (status code 2xx), it does nothing and execution continues 
        normally.
        
        If the response indicates an error (status code 4xx or 5xx), it raises an HTTPError exception. 
        The raised exception is then caught by the except requests.exceptions.RequestException block, 
        which prints a descriptive error message.
        '''
        response.raise_for_status()  # Check if the request was successful

        # Write the content of the response (the audio file) to a local file
        with open(file_path, 'wb') as audio_file:
            audio_file.write(response.content)
        
        print(f"Audio file downloaded successfully and saved to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the audio file: {e}")


# Call the function to download the audio file
download_audio_file(url, audio_file_path)
