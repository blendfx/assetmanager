# Asset Localizer

Here at the studio we use linked libraries a lot. 
We also work with project repositories, that usually contain the various scene files, a folder for textures, and a library folder with all the different assets. Our goal is to have everything in a self-contained repository with relative paths.

So during set dressing we often link in assets from a library on our server or other repositories. If we decide to keep the asset in the scene we need to be able to "localize" it and move the linked blendfile into our local repository. 
This addon will follow the link of an instanced collection, pack the file, copy it to the library path of your local repository and update the link of the collection instance. 

Download the zip from this repository and install it as an addon.
Here you can see how to use it:

![diagram](/diagram.png)

A gif of a demonstration:

![explanational gif](/explain_small.gif)
