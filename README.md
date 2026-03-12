# YouTube Video Summarizer

A Python tool that summarizes a YouTube video and generates a `.docx` report with relevant images.

## Features

- Fetches video metadata (title, channel, duration, description, tags)
- Extracts the video transcript (manual or auto-generated captions)
- Generates an extractive summary highlighting key points
- Downloads video thumbnails and keyframe images
- Creates a professional `.docx` document containing:
  - Video title, channel, and metadata
  - Main thumbnail image
  - Executive summary
  - Additional video snapshots
  - Detailed section-by-section breakdown
  - Original video description and tags

## Requirements

- Python 3.8+
- Internet connection

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Default video

Summarize the default video (`https://www.youtube.com/watch?v=SvXEAj7Mb48`):

```bash
python summarize_video.py
```

### Custom video URL

```bash
python summarize_video.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Custom output path

```bash
python summarize_video.py -o my_summary.docx
```

### Adjust summary length

```bash
python summarize_video.py -s 20  # 20 sentences in the executive summary
```

## Output

The generated `.docx` file is saved to the `output/` directory by default and includes:

1. **Video title and metadata** – channel name, duration, upload date
2. **Main thumbnail** – large hero image from the video
3. **Executive summary** – key points extracted from the transcript
4. **Video snapshots** – additional thumbnail images from the video
5. **Detailed section breakdown** – time-segmented summaries (5-minute intervals)
6. **Original description and tags** – from the video metadata

## Example

```bash
$ python summarize_video.py "https://www.youtube.com/watch?v=SvXEAj7Mb48"

Video ID: SvXEAj7Mb48
Video URL: https://www.youtube.com/watch?v=SvXEAj7Mb48

Fetching video metadata...
  Title: Example Video Title
  Channel: Example Channel
  Duration: 10:30

Fetching transcript...
  Transcript length: 12345 characters

Generating summary...
  Summary length: 2000 characters

Segmenting transcript...
  Number of segments: 3

Fetching images...
  Keyframe thumbnails: 4
  Metadata thumbnails: 2
  Total unique images: 5

Creating document: output/Example_Video_Title_summary.docx

Done! Document saved to: output/Example_Video_Title_summary.docx
```
