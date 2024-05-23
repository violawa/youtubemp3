Berikut adalah README.md yang telah disesuaikan dan ditambahkan bagian lisensi untuk proyek YouTube MP3 Downloader:

```markdown
# YouTube MP3 Downloader

This is a simple Python application for downloading audio from YouTube videos and converting them to MP3 format.

## Prerequisites
Before using this application, ensure that you have Tkinter installed. Tkinter is usually bundled with Python installations on Windows and macOS but may need to be installed separately on Linux distributions.

### Installation Instructions:

**Windows and macOS:**
Tkinter is typically installed along with Python. You can check by running the following command in Command Prompt or Terminal:
```bash
python -m tkinter
```

**Linux:**
- **Debian/Ubuntu:**
  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk
  ```
- **Fedora:**
  ```bash
  sudo dnf install python3-tkinter
  ```
- **CentOS:**
  ```bash
  sudo yum install python3-tkinter
  ```

## Usage
1. Enter the YouTube URL of the video you want to download audio from.
2. Specify the output folder where you want to save the downloaded MP3 file.
3. Click on the "Download and Convert" button to initiate the download and conversion process.

## Features
- Download audio from YouTube videos.
- Convert downloaded audio to MP3 format.
- Simple user interface.

## Dependencies
- [Pytube](https://github.com/pytube/pytube): For downloading YouTube videos.
- [MoviePy](https://github.com/Zulko/moviepy): For audio conversion.
- Tkinter: Python's standard GUI toolkit.

## How to Run
Simply execute the Python script `youtube_mp3_downloader.py`.

## User Interface
![GUI](https://github.com/violawa/ytmp3downloader/blob/87101dbb6b2125939391cd0c5bc43502aa11d625/GUI.png)

## Disclaimer
This application is for personal and educational use only. Respect copyright laws and terms of service of the respective platforms.

## Author
This application is developed by [Viola Wulan Az Zahro].

## License
This project is licensed under the MIT License - see the (https://github.com/violawa/ytmp3downloader/blob/main/LICENSE) file for details.

## Contributions
Contributions are welcome! Feel free to submit issues and pull requests.

## Acknowledgments
- Special thanks to the developers of Pytube and MoviePy for their fantastic libraries.
- Hat tip to anyone whose code was used as inspiration.
```

### LICENSE File (MIT License)
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
