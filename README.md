# PyVirtualDirectoryExplorer_on_ls_dir_listing
This is Virtual Directory Explorer app (simple app), written with Python2 + wxWidgets.

Takes for input recursive directory listing from either:

1.1) Linux/Unix `ls -laR' command output 
or 
1.2) Windows `dir /s' command output 
and 
2) Provides GUI browser for it, the graphical interface to browse/explore the given virtual directory.

It can be considered as directory structure snapshot viewer / browser.

Even entire filesystem structure of the disk can be provided as an input.

### Designed-in Limitations

Since input does not contain other info besides directory/filesystem structure and metainformation, such as content of the files,
the browser can't show or provide them.
