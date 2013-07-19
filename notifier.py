#!/usr/bin/env python

import dbus, sys

def notify(app_name='', replaces_id=0, icon='', summary='', body='', actions=[], hints=[], timeout=-1):
    bus_name       = 'org.freedesktop.Notifications'
    object_path    = '/org/freedesktop/Notifications'
    interface_name = 'org.freedesktop.Notifications'

    session_bus = dbus.SessionBus()
    obj = session_bus.get_object(bus_name, object_path)
    interface = dbus.Interface(obj, interface_name)
    interface.Notify(app_name, replaces_id, icon, summary, body, actions, hints, timeout)

if __name__ == '__main__':
    # Transient is true to clear the queue
    notify(summary=' '.join(sys.argv[1:]),
        hints=dbus.Dictionary({'transient':True}))
