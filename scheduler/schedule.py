import __init__
import asyncio
import settings.settings as settings
import scheduler.on_time as on_time
import scheduler.on_change as on_change
import internal.see_all_variables as see_all_variables
import internal.global_stats as global_stats

"""
Purpose: This files holds the main scheduler that runs the needs to be ran at specific times
    or on change.
"""
class Scheduler:
    def __init__(self):
        pass
    
    def run(self, test_mode=False):
        """
        Purpose: Run both the onchange and ontime scheduler
        """
        # settings.GLOBAL_CANCELLABLE_LOOPS.append(asyncio.create_task(on_time.OnTime().add_watcher_reversed(60*60*24, all_exchanges.AllExchanges.all_process_api_exchange_list())))
        on_change_monitor_task = asyncio.create_task(on_change.OnChange().monitor_changes())
        return on_change_monitor_task


if __name__ == '__main__':
    Scheduler().run()