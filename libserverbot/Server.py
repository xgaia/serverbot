import psutil
import time
import datetime
import decimal

from wakeonlan import send_magic_packet
from subprocess import call, check_output

class Server():

    def __init__(self, disks, slaves):

        self.disks = disks
        self.slaves = slaves


    def disk_usage(self, disk):
        usage = psutil.disk_usage(disk['path'])
        return {
            'name': disk['name'],
            'path': disk['path'],
            'total': round(usage.total / 1024 / 1024 / 1024, 2),
            'used': round(usage.used / 1024 / 1024 / 1024, 2),
            'free': round(usage.free / 1024 / 1024 / 1024, 2),
            'percent': usage.percent
        }

    def ismounted(self, disk):

        return disk['path'] in self.available_mountpoint()

    def available_mountpoint(self):

        return [part.mountpoint for part in psutil.disk_partitions()]


    def get_disks_usage(self):

        disks_usage = []
        for disk in self.disks:
            if self.ismounted(disk):
                disks_usage.append(self.disk_usage(disk))
        return disks_usage

    def uptime(self):

        boot_time = psutil.boot_time()
        now = time.time()
        uptime = now - boot_time

        days = int(decimal.Decimal(uptime/3600/24).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_DOWN))
        hours = int(decimal.Decimal((uptime/3600) - (24 * days)).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_DOWN))
        minutes = int(decimal.Decimal((uptime/60) - (3600 * hours) - (24 * days)).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_DOWN))

        return {
            'days': days,
            'hours': hours,
            'minutes': minutes
        }

    def memory(self):

        memory = psutil.virtual_memory()

        return {
            'percent': memory.percent,
            'total': round(memory.total / 1024 / 1024 / 1024, 2),
            'used': round(memory.used / 1024 / 1024 / 1024, 2),
            'free': round(memory.free / 1024 / 1024 / 1024, 2),
            'buffers': round(memory.buffers / 1024 / 1024 / 1024, 2),
            'cached': round(memory.cached / 1024 / 1024 / 1024, 2)
        }


    def swap(self):

        swap = psutil.swap_memory()

        return {
            'percent': swap.percent,
            'total': round(swap.total / 1024 / 1024 / 1024, 2),
            'used': round(swap.used / 1024 / 1024 / 1024, 2),
            'free': round(swap.free / 1024 / 1024 / 1024, 2)
        }

    def wakeonlan(self, mac):

        send_magic_packet(mac)

    def shutdown(self):

        call(['sudo', 'shutdown', '1'])

    def cmd(self, cmd):

        return check_output(cmd.split()).decode('utf-8')




