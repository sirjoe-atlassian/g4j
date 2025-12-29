"""Configuration reader utility for loading test configurations."""
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv


class ConfigReader:
    """Read and manage configuration from YAML and environment files."""
    
    def __init__(self):
        """Initialize the configuration reader."""
        self.config_path = Path(__file__).parent.parent / 'config' / 'config.yaml'
        self.env_path = Path(__file__).parent.parent / '.env'
        
        # Load environment variables
        if self.env_path.exists():
            load_dotenv(self.env_path)
        
        # Load YAML configuration
        self.config = self._load_yaml_config()
    
    def _load_yaml_config(self):
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def get_environment(self):
        """Get the current environment."""
        return os.getenv('ENVIRONMENT', self.config['environment']['default'])
    
    def get_base_url(self):
        """Get the base URL for the current environment."""
        env = self.get_environment()
        return os.getenv('BASE_URL', self.config[env]['base_url'])
    
    def get_timeout(self):
        """Get the timeout value for the current environment."""
        env = self.get_environment()
        return self.config[env]['timeout']
    
    def get_browser_config(self):
        """Get browser configuration."""
        return self.config['browser']
    
    def get(self, key, default=None):
        """Get a configuration value by key."""
        return self.config.get(key, default)


# Singleton instance
config_reader = ConfigReader()
