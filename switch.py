class Switch:
    all_switches = []

    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        Switch.all_switches.append(self)

    @classmethod
    # This class method is going to load all the switches from database
    def load_all_switches(cls):
        pass

    @classmethod
    # This class method is going to store all the switches to database
    def store_all_switches(cls):
        pass

    def backup(self, time):
        '''
            It will make a configuration backup
            at given time.
        '''
        pass

    def health_status(self, time):
        '''
            It returens health checked parameters
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
        IP: {self.ip}
        Site:: {self.site}
        Building: {self.building}
        Room: {self.room}
        Rack: {self.rack}
        Height Unit (HE): {self.he}
        """
