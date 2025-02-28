import datetime
from typing import Optional, Union

import discord
from config import config
from musicbot.linkutils import Origins, Sites


class Song:
    def __init__(
        self,
        origin: Origins,
        host: Sites,
        base_url: Optional[str] = None,
        uploader: Optional[str] = None,
        title: Optional[str] = None,
        duration: Optional[int] = None,
        webpage_url: Optional[str] = None,
        thumbnail: Optional[str] = None,
    ):
        self.host = host
        self.origin = origin
        self.base_url = base_url
        self.info = self.Sinfo(
            uploader, title, duration, webpage_url, thumbnail
        )

    class Sinfo:
        def __init__(
            self,
            uploader: Optional[str],
            title: Optional[str],
            duration: Optional[int],
            webpage_url: Optional[str],
            thumbnail: Optional[str],
        ):
            self.uploader = uploader
            self.title = title
            self.duration = duration
            self.webpage_url = webpage_url
            self.thumbnail = thumbnail

        def format_output(self, playtype):
            embed = discord.Embed(
                title=playtype,
                description="[{}]({})".format(self.title, self.webpage_url),
                color=config.EMBED_COLOR,
            )

            if self.thumbnail is not None:
                embed.set_thumbnail(url=self.thumbnail)

            embed.add_field(
                name=config.SONGINFO_UPLOADER,
                value=self.uploader,
                inline=False,
            )

            embed.add_field(
                name=config.SONGINFO_DURATION,
                value=(
                    str(datetime.timedelta(seconds=self.duration))
                    if self.duration is not None
                    else config.SONGINFO_UNKNOWN_DURATION
                ),
                inline=False,
            )

            return embed

    def update(self, data: Union[dict, "Song"]):
        if isinstance(data, Song):
            self.base_url = data.base_url
            self.info = data.info
            return

        self.base_url = data.get("url")
        self.info.uploader = data.get("uploader")
        self.info.title = data.get("title")
        self.info.duration = data.get("duration")
        self.info.webpage_url = data.get("webpage_url")
        thumbnails = data.get("thumbnails")
        if thumbnails:
            # last thumbnail has the best resolution
            self.info.thumbnail = thumbnails[-1]["url"]
