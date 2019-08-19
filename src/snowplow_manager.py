from snowplow_tracker import logger
from snowplow_tracker import SelfDescribingJson
from snowplow_tracker import Subject, Tracker, Emitter


class SnowplowManager:
    def __init_(self, config):
        """
        Initialize service
        """
        with open('src/config.json') as config_file:
            self.defaultConfig = json.load(config_file)
        self.companyConfig = config
        self.tracker = None
        self.emitter = None
        self.subject = None

    def setup_tracker(self):
        """Setup an instance of a tracker"""
        self.companyConfig = self.setup_config(self.companyConfig)
        self.emitter = Emitter(
            self.companyConfig["COLLECTOR_HOST"],
            protocol = self.companyConfig["PROTOCOL"],
            port = self.companyConfig["PORT"],
            method = self.companyConfig["EMIT_METHOD"],
            buffer_size = self.companyConfig["BUFFER_SIZE"]
        )
        self.subject = Subject()
        self.tracker = Tracker(
            emitters = self.emitter,
            subject = self.subject,
            namespace = self.companyConfig["TRACKER_NAME"],
            app_id = self.companyConfig["APP_ID"],
            encode_base64 = self.companyConfig["ENCODE64"]
        )

    def setup_config(self, config):
        """Setup config with company and default config"""
        if config['TRACKER_NAME'] is None or \
            config['APP_ID'] is None:
            return

        keys = [
            'COLLECTOR_HOST',
            'PROTOCOL',
            'EMIT_METHOD',
            'BUFFER_SIZE',
            'DEBUG_MODE',
            'ENCODE64',
            'PORT'
        ]

        for key in keys:
            config[key] = self.defaultConfig[key]

        if "DEV_ENV" in config:
            if config["DEV_ENV"] == True:
                config["COLLECTOR_HOST"] = self.defaultConfig["COLLECTOR_HOST_DEV"]

        if "INSPETOR_ENV" in config:
            if config["INSPETOR_ENV"] == True:
                config["COLLECTOR_HOST"] = 'test'

        return config

    def flush(self):
        """
        Flush trackers
        """
        self.tracker.flush()
