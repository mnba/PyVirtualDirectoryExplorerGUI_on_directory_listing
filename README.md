# PyVirtualDirectoryExplorer_on_ls_dir_listing
This is Virtual Directory Explorer app (simple app), written with Python2 + wxWidgets.

Takes for input recursive directory listing from either:

#) Linux/Unix 'ls -laR' command output or 
#) Windows 'dir /s' command output and 
#) Provides GUI browser for it, the graphical interface to browse/explore the given virtual directory.

It can be considered as *Directory structure snapshot viewer / browser*.

Even entire disk filesystem structure can be examined.

### Designed-in Limitations

Since input does not contain other info besides directory/filesystem structure and metainformation, such as content of the files,
the browser can't show or provide them.
