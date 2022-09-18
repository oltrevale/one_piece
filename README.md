# DOWNLOAD  ONE-PIECE CHAPTERS from onepiecechapters.com
## Feautures
- download chapter or a range of chapters in pdf format 
- bookmarks
- add previous , next , last or range of chapter to a pdf (for now you can only add pdf created by this program)
## Guide
### Install requirements
```
pip install -r requirements.txt
 ```
### Commands
#### download
to download a single chapter

```
py main.py download {chapter}
```

to download from begin_chapter to end_chapter

```
py main.py download {start_chapter} {end_chapter}
```
#### remuntada
to download and add a range of chapter ,from last chapter in pdf to one piece latest chapter, to a file
```
py main.py remuntada {file without extension}
```
#### add
to download and add a chapter to a file created by this program

```
py main.py add {nome file without extension} {chapter to download}
```

to download and add a range of chapters to a file created by this program
```
py main.py add {nome file without extension} {start_chapter} {end_chapter}
```
#### addlast
to download and add onepiece latest chapter  to a file created by this program
```
py main.py addlast {nome file without extension}
```

#### addprev
to download and add a previous chapter to a file created by this program
```
py main.py addprev {nome filew without extension}
```

to download and add a range of previous chapters to a file crated by this program


