from integration.util.ssh import run_ssh


def loop_device_cleanup(password):
    print('cleanup')
    for mount in run_ssh('mount', password=password).splitlines():
        if 'loop' in mount:
            print(mount)
            run_ssh('umount /dev/loop0', throw=False, password=password)

    for loop in run_ssh('losetup', password=password).splitlines():
        if 'loop0' in loop:
            run_ssh('losetup -d /dev/loop0', throw=False, password=password)

    run_ssh('losetup', password=password)

    for loop in run_ssh('dmsetup ls', password=password).splitlines():
        if 'loop0p1' in loop:
            run_ssh('sudo dmsetup remove loop0p1', password=password)
        if 'loop0p2' in loop:
            run_ssh('sudo dmsetup remove loop0p2', password=password)

    for loop_disk in run_ssh('ls -la /tmp', password=password).splitlines():
        if '/tmp/disk' in loop_disk:
            run_ssh('rm -rf /tmp/disk', throw=False, password=password)
