import os

from moviepy.editor import *

FOOTAGES_DIR = "/Volumes/Kulafu/PyCon PH 2016 Videos/footages"
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


def isabel_sy():
    cam_1 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d1", "02_isabel_sy_cam_1.mp4")
    ).resize(SIZE)
    cam_2 = VideoFileClip(
        os.path.join(FOOTAGES_DIR, "d1", "02_isabel_sy_cam_2.mp4")
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
    section_title = "Isabel Sieh"
    section_subtitle = "Building a Coding Community"
    section = CompositeVideoClip([
        section_clip.set_duration(None),
        TextClip(txt=section_title, color="#d14e4d", font="Arial",
                 fontsize=60).set_pos((60, 570)),
        TextClip(txt=section_subtitle, color="#333333", font="Arial",
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
    video.write_videofile(os.path.join("output", "isabel_sy.mp4"))


def main():
    isabel_sy()


if __name__ == "__main__":
    main()

