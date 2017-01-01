# PyCon PH 2016 Videos

## Requirements

- __MoviePy__

  You'll need the latest version of MoviePy:

  ```
  pip install git+https://github.com/Zulko/moviepy.git@master
  ```

  MoviePy installs its required dependencies.

- __ImageMagick__

  This is required for rendering text in our titles.

## Build

```
python build.py
```

## Notes

Paths are hardcoded since this is (for now) a one-time script.

The latest version of ImageMagick causes an error in MoviePy. I had to
comment out lines `1117-1128` and `1183-1184` of `moviepy.videos.VideoClip` for
text rendering to work.
