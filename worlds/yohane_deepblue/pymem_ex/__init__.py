"""
A wrapper for Pymem to extent its functionality
"""
import copy
import functools

import pymem
import pymem.exception
import pymem.memory
import pymem.process
import pymem.thread


class PymemEX(pymem.Pymem):
    @property
    @functools.lru_cache(maxsize=1)  # noqa: B019
    def main_thread(self):
        """Retrieve ThreadEntry32 of main thread given its creation time.

        Raises
        ------
        ProcessError
            If there is no process opened or could not list process thread

        Returns
        -------
        Thread
            Process main thread
        """
        if not self.process_id:
            raise pymem.exception.ProcessError("You must open a process before calling this method")
        threads = [copy.deepcopy(t) for t in pymem.process.enum_process_thread(self.process_id)]
        threads = sorted(threads, key=lambda k: k.creation_time)

        if not threads:
            raise pymem.exception.ProcessError("Could not list process thread")

        main_thread = threads[0]
        return pymem.thread.Thread(self.process_handle, main_thread)

