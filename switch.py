class Switch:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def backup(self, time):
        '''
            It will make a configuration backup
            at given time.
        '''
        pass

    def health_status(self, time):
        '''
            It returens helth checked parameters
            like memory usage, cpu usage, 
        '''

    def location(self, site, building, room, rack, he):
        self.site = site
        self.building = building
        self.room = room
        self.rack = rack
        self.he = he

    def __str__(self):
        return f"""\nSwitch: 
        Hostname: {self.hostname}
        Site:: {self.site}
        Building: {self.building}
        Room: {self.room}
        Rack: {self.rack}
        Height Unit (HE): {self.he}
        """
