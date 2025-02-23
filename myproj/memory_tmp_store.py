class MemoryTmpStore(dict):
    """
    A memory-based temporary file store implementation.
    Stores files in RAM during form processing.
    """
    def __init__(self):
        super().__init__()
        self._cleanup_callbacks = []
    
    def preview_url(self, name):
        """Return URL for previewing uploaded files."""
        return None  # No preview URLs for memory storage
    
    def __setitem__(self, key, value):
        """Override dict.__setitem__ to track file additions."""
        super().__setitem__(key, value)
        # Track cleanup callback for this file
        self._cleanup_callbacks.append(key)
    
    def __getitem__(self, key):
        """Override dict.__getitem__ to check for expired items."""
        value = super().__getitem__(key)
        if isinstance(value, bytes) and len(value) == 0:
            raise KeyError(f"Expired or invalid temp file: {key}")
        return value
    
    def __delitem__(self, key):
        """Override dict.__delitem__ to remove cleanup tracking."""
        super().__delitem__(key)
        if key in self._cleanup_callbacks:
            self._cleanup_callbacks.remove(key)
    
    def keys(self):
        """Return list of active temporary file IDs."""
        return [k for k in super().keys() 
                if isinstance(self[k], bytes) and len(self[k]) > 0]
    
    def cleanup(self):
        """Clean up all stored files."""
        for key in self._cleanup_callbacks[:]:
            del self[key]