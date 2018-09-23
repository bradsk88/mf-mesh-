# mf-mesh-

Not sure why I put a dash in the name.  Whipped this up while trying (and often
succeeding) to recover videos from SD cards formatted by a Panasonic GX camera.

# How to (potentially) recover video files from a formatted SD card

Ideally, you *just* formatted the card.  If you've used the card since formatting,
there is a risk that your data is gone forever.

To reduce the risk of further loss (and in general) I would recommend making an 
image of your SD card before proceeding.

On linux you can run this command, assuming your SD card is loaded at `/dev/sd`:
```
dd if=/dev/sd of=~/mybackup.img --progress
```

Once you have an image file, run [photorec](https://wiki.archlinux.org/index.php/file_recovery#Testdisk_and_PhotoRec)
to recover any .mov files from `mybackup.img`.

Once that's finished, you should have many `_ftyp.mov` and `_mdat.mov` files. 
These are the data from your videos, but they need to be paired up before you 
can use the videos.  Problem is: they don't appear to pair up in any particular 
order.

Copy `recover.py` from this repo into the folder with all of the `_ftyp/mdat` 
and run it:

```
$ python recover.py
```

This will run a brute-force algorithm to pair up every combination of 
`ftyp/mdat` files in the directory.  *This will take a very long time.*
