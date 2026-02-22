# YT-Downloader

- Ensure FFMPEG is installed and is added to system `PATH` variable
- Or use similar to the below arg in `ydl_opts` (Windows example shown):

```python
'ffmpeg_location': r'\path\to\ffmpeg\bin\ffmpeg.exe'
```

Install FFMPEG (Ubuntu/Debian): `sudo apt update && sudo apt install ffmpeg -y`
Verify via: `ffmpeg -version`de

## Getting Started

### Linux

- Initialise a venv: `python3 -m venv .venv`
- Activate it: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Deactivate when Done: `deactivate`
