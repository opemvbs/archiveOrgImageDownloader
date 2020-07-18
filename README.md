# archiveOrgImageDownloader

This is a modified and improved version of the [harrcor's](https://github.com/harrcorr/ArchiveOrgLibraryDownloader) repository.
The script is most useful to be used on a protected book that needs to be borrowed, and that you can't download it by using the encrypted epub/pdf links. So, this script will download the image of the borrowed book one by one.


## Requirements

- Operating system: Linux or Windows
I used Linux to modify this script, so in order to use Windows, you will need to change this one line from ```driver = webdriver.Chrome("./chromedriver", options=chrome_options)``` to ```driver = webdriver.Chrome("./chromedriver.exe", options=chrome_options)```
- Python 3.x
- Git


## Dependencies

This script depends on these few libraries:
- selenium
```pip3 install selenium```

- requests
```pip3 install requests```

- [Chrome WebDriver](https://chromedriver.chromium.org/downloads)
If you use Linux, then use the Linux version, same as Windows, use the Windows version.


## Usage
### Cloning the repository

You will need to clone the repostory by using the ```git clone``` command on Linux, or you can use GitHub Desktop application on Windows, or you can do whatever you want to clone it.

### Running the script
#### Linux

On Linux, open your terminal and change to your current working directory.
Then, you will need to execute this command to run the script.
```python3 scraper.py```
Fill in the details in order to download your book.

#### Windows

On Windows, open your command prompt and change to your current working directory.
Then, you will need to execute this command to run the script.
```python3 scraper.py```
Fill in the details in order to download your book.


### Example

Your archive.org email account: foo@gmail.com
Your archive.org password: bar123
Your archive.org book link (relative to your current working directory): https://archive.org/details/computationalmet00hann_0
Your download directory/folder: ./book/computationalmet00hann_0
Your pages that will be downloaded: 488
Your quality of images, from 0-10 (lower is better): 0