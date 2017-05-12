import sys

try:
    import webview

except ImportError:
    sys.stderr.write("Could not import pywebview. (Try installing it using `pip install pywebview`)")

