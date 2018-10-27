## PyVirtualDirectoryExplorer_on_ls_dir_listing
This is **Virtual Directory Explorer app** (simple app), written with Python2 + wxWidgets.

* Takes for input recursive directory listing from either:
  * Linux/Unix/Macos '**ls -laR**' command output or 
  * Windows '**dir /s**' command output and 
* Provides GUI browser for it, the graphical interface to browse/explore the given virtual directory.

It can be considered as **_Directory structure snapshot browser or viewer_**.

Even entire disk filesystem structure can be examined.

### Supported Operating systems: Windows, Macos, Linux
This software supports all major desktop Operating Systems: Windows, Macos, Linux. Only required support is for Python 2.7 and wxWidgets 2.9+.

### Designed-in Limitations

Since input does not contain other info besides directory/filesystem structure and metainformation generated by dir /s of ls -laR command, it doesn't contain other information such as content of the files, so the browser can't show or provide them.

This is in the first head *directory **structure** snapshot browser*. 

## Screenshots
Screenshot of browser for **_tests/zCTdisk_laR.txt_** file, which was generated by the next command
```shell
cd /mount/CTDisk/
ls -laR > ../CTdisk_laR.txt
```
  
![Screenshot of v1.0 (Linux)](/screenshots/screenshot-linux1.0s1.png?raw=true "Screenshot of v1.0 (Linux)")

## How to Run it
From command line simply run: `./App.py`
