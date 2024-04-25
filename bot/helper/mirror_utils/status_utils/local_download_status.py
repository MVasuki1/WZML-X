#!/usr/bin/env python3
from bot.helper.ext_utils.bot_utils import EngineStatus, get_readable_file_size, MirrorStatus, get_readable_time


class LocalDownloadStatus:

    def __init__(self, name, size, gid, obj, message, upload_details):
        self.__obj = obj
        self.__name = name
        self.__size = size
        self.__gid = gid
        self.message = message
        self.upload_details = upload_details

    def name(self):
        return self.__name

    def progress_raw(self):
        return 100.0

    def progress(self):
        return f"{self.progress_raw()}%"

    def status(self):
        return MirrorStatus.STATUS_DOWNLOADING

    def processed_bytes(self):
        return 0

    def eta(self):
        try:
            return get_readable_time(0)
        except ZeroDivisionError:
            return '-'

    def size(self):
        return get_readable_file_size(0)

    def speed(self):
        return f'0 KB/s'

    def gid(self):
        return self.__gid

    def download(self):
        return self.__obj

    def eng(self):
        return EngineStatus().STATUS_LOCAL
