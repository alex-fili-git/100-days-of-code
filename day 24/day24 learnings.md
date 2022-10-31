# file system in python
## Reading and writing
### very straightforward way
Can use text file in a folder with
open(fileName using string) -> file = open("the_file.txt")
contents = file.read(file)
We also needs to close the file because it uses resources
file.close()

### pythonic way
Now you don't have to close the file any more
with open("file.txt") as file:
    contents = file.read()
    print(contents)

with open("file.txt", mode="w") as file:
    file.write("text")

Modes "r" for reading. "w" deletes text, "a" appends and thus adds text.

## Paths
### Absolute file paths
The root (where it all starts) is represented by /
So the folder "work" which exists in the root is
/work
The report.doc is in work so path
/work/report.doc
The presentations folder in work is
/work/presentations
The ppt in presentations is
/work/presentations/talk.ppt
### Relative file paths
If you are inside presentations you can access talk by
talk.ppt
To go up use "..", so if you are in presentations and want report.doc
You have to go back to work and into doc
../report.doc