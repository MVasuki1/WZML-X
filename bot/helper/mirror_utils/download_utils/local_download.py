from random import SystemRandom
from string import ascii_letters, digits
from bot import LOGGER, config_dict, download_dict_lock, download_dict, non_queued_dl, queue_dict_lock
from bot.helper.mirror_utils.status_utils.queue_status import QueueStatus
from bot.helper.mirror_utils.status_utils.local_download_status import LocalDownloadStatus
import subprocess


async def add_local_dir(link, path, listener):
    gid = ''.join(SystemRandom().choices(ascii_letters + digits, k=8))
    async with download_dict_lock:
        download_dict[listener.uid] = LocalDownloadStatus(
            name='',
            size='',
            gid=gid, 
            obj=None,
            message=listener.message,
            upload_details=listener.upload_details)

    print(subprocess.check_output(f'mkdir -p {path}', shell=True).decode().strip())
    print(subprocess.check_output(f'cd {link} && ls', shell=True).decode().strip())
    print(subprocess.check_output(f'mv {link}/* {path}/', shell=True).decode().strip())
    await listener.onDownloadComplete()
