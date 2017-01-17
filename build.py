import os

from moviepy.config import change_settings
from moviepy.editor import *

# FOOTAGES_DIR = "E:\\PyCon PH 2016\\footages"
FOOTAGES_DIR = "/Volumes/Kulafu/PyCon PH 2016 Videos/footages"
IMAGEMAGICK_BINARY = "D:\\MarkSteve\\Bin\\ImageMagick-7.0.1-9-portable-Q16-x64\\convert.exe"

SIZE = (1280, 720)
PIP_BIG = (1120, 630)
PIP_SMALL = (320, 180)

title_clip = ImageClip("title.png")
section_clip = ImageClip("section.png")
pip_clip = ImageClip("pip.png")


def trim_clips(clips):
    for i, p in enumerate(clips):
        offset, clip = p
        next_offset, next_clip = clips[i + 1]
        yield clip.subclip(offset, next_offset)
        if next_clip is None:
            return


def isabel_sieh():
    cam_1 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d1", "02_isabel_sieh_cam_1.mp4")
    ).resize(SIZE)
    cam_2 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d1", "02_isabel_sieh_cam_2.mp4")
    ).resize(SIZE)
    pip = CompositeVideoClip([
        pip_clip.set_duration(None),
        cam_1.resize(PIP_BIG).volumex(0),
        cam_2.resize(PIP_SMALL).set_pos(("right", "bottom")),
    ])
    talk = concatenate_videoclips(list(trim_clips([
        (0, cam_1),
        (17, cam_2),
        (42, cam_1),
        (105, cam_2),
        (120, cam_1),
        (131, pip),
        (1131, None),
    ])))
    name_txt = "Isabel Sieh"
    talk_txt = "Building a Coding Community"
    section = CompositeVideoClip([
        section_clip.set_duration(None),
        TextClip(name_txt, color="#d14e4d", font="Arial",
                 fontsize=60).set_pos((60, 570)),
        TextClip(talk_txt, color="#333333", font="Arial",
                 fontsize=40).set_pos((60, 630)),
    ])
    video = CompositeVideoClip([
        talk.set_start(2).crossfadein(1),
        (section
         .set_start(105)
         .set_duration(5)
         .crossfadein(1)
         .crossfadeout(1)),
        title_clip.set_duration(3).crossfadeout(1),
    ])
    video.write_videofile(os.path.join("output", "d1", "02_isabel_sieh.mp4"))


def dylan_jay():
    cam_1_1 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d2", "01_1_dylan_jay_cam_1.mp4")
    ).resize(SIZE)
    cam_1_2 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d2", "01_1_dylan_jay_cam_2.mp4")
    ).resize(SIZE)
    pip_1 = CompositeVideoClip([
        pip_clip.set_duration(None),
        cam_1_2.resize(PIP_BIG).volumex(0),
        cam_1_1.resize(PIP_SMALL).set_pos(("right", "bottom")),
    ])
    cam_2_1 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d2", "01_2_dylan_jay_cam_1.mp4")
    ).resize(SIZE)
    cam_2_2 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d2", "01_2_dylan_jay_cam_2.mp4")
    ).resize(SIZE)
    pip_2 = CompositeVideoClip([
        pip_clip.set_duration(None),
        cam_2_2.resize(PIP_BIG).volumex(0),
        cam_2_1.resize(PIP_SMALL).set_pos(("right", "bottom")),
    ])
    talk = concatenate_videoclips(list(trim_clips([
        (0, cam_1_2),
        (20, cam_1_1),
        (90, pip_1),
        (2109, None),
    ])) + list(trim_clips([
        (0, pip_2),
        (1879, None),
    ])))
    name_txt = "Dylan Jay"
    talk_txt = "A case study in customisable software"
    section = CompositeVideoClip([
        section_clip.set_duration(None),
        TextClip(name_txt, color="#d14e4d", font="Arial",
                 fontsize=60).set_pos((60, 570)),
        TextClip(talk_txt, color="#333333", font="Arial",
                 fontsize=40).set_pos((60, 630)),
    ])
    video = CompositeVideoClip([
        talk.set_start(2).crossfadein(1),
        (section
         .set_start(76)
         .set_duration(5)
         .crossfadein(1)
         .crossfadeout(1)),
        title_clip.set_duration(3).crossfadeout(1),
    ])
    video.write_videofile(os.path.join("output", "d2", "01_dylan_jay.mp4"))


def main():
    # change_settings({"IMAGEMAGICK_BINARY": IMAGEMAGICK_BINARY})
    # isabel_sieh()
    dylan_jay()


if __name__ == "__main__":
    main()

