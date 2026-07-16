#Function to load mock classes to avoid library conflicts between versions
def load_mock_classes():
    load_sentinel_mock()
    load_trio_mock()
        

def load_sentinel_mock():
    import sys
    import typing_extensions

    if not hasattr(typing_extensions, 'Sentinel'):
        # Sentinel Mock class
        class Sentinel:
            def __init__(self, name, repr=None):
                self._name = name
                self._repr = repr if repr is not None else f'<{name}>'
            def __repr__(self):
                return self._repr
            def __copy__(self): return self
            def __deepcopy__(self, memo): return self

        # We added Sentinel to the typing_extension library
        typing_extensions.Sentinel = Sentinel
        sys.modules['typing_extensions'].Sentinel = Sentinel


def load_trio_mock():
    import sys
    import types
    import pathlib

    if 'trio._path' not in sys.modules:
        
        mock_path_module = types.ModuleType("trio._path")
        class MockPath(pathlib.Path):
            pass
            
        mock_path_module.Path = MockPath
        sys.modules['trio._path'] = mock_path_module