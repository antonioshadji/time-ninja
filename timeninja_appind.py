#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
displays days to end of year/month
'''

from gi.repository import Gtk, Gdk, GObject, GLib

try:
    from gi.repository import AppIndicator3 as AppIndicator
except:
    from gi.repository import AppIndicator

import sys
from datetime import date

class GoalCountdown(GObject.GObject):
    '''create date specific countdown timer'''
    year = 365
    month = 31

    def __init__(self):
    # Create Indicator with icon and label
        #icon_image = '/usr/share/unity/icons/panel-shadow.png'
        icon_image = '/home/antonios/bin/timeninja/hourglass.png'
        self.ind = AppIndicator.Indicator.new("time-ninja",
                icon_image,
                AppIndicator.IndicatorCategory.APPLICATION_STATUS)
        self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)

        # GTK menu
        self.menu = Gtk.Menu()
        #self.separator = Gtk.SeparatorMenuItem()
        self.exit = Gtk.MenuItem("Exit")
        self.exit.connect("activate", self.quit)

        #show menu
        #self.separator.show()
        self.exit.show()

        # Append menu
        #self.menu.append(self.separator)
        self.menu.append(self.exit)

        self.ind.set_menu(self.menu)
        
        #calculate days
        self.set_vars()

        # Set label
        self.ind.set_label(str(self.year.days)+" Days "+
                str(self.month.days)+" Days", "")

        # Refresh indicator
        GLib.timeout_add_seconds(60*60*1000, self.set_vars)

    def set_vars(self):
        self.year = date(date.today().year + 1, 1, 1) - date.today()
        if date.today().month == 12:
            self.month = date(date.today().year + 1, 1, 1) - date.today()
        else:
            self.month = date(date.today().year , date.today().month + 1, 1) - date.today()

    def quit(self, menu_item):
        ''' exit application from dropdown menu'''
        sys.exit(0)

if __name__ == "__main__":
    indicator = GoalCountdown()
    Gtk.main()
