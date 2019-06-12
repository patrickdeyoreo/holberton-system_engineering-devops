# 0x00-shell_basics
#### Collection of simple shell scripts to execute basic commands

* **0-current\_working\_directory**
  * Print the absolute path name of the current directory.

* **1-listit**
  * Display the contents list of the current directory.

* **2-bring\_me\_home**
  * Change the working directory to the user’s home directory.

* **3-listfiles**
  * Display current directory contents in a long format.

* **4-listmorefiles**
  * Display current directory contents, including hidden files, in long format.

* **5-listfilesdigitonly**
  * Display current directory contents as follows:
    * long format
    * numeric user and group IDs
    * hidden files

* **6-firstdirectory**
    * Create a directory named ```holberton``` in the ```/tmp/``` directory.

* **7-movethatfile**
  * Move the file ```betty``` from ```/tmp/``` to ```/tmp/holberton```.

* **8-firstdelete**
  * Delete the file ```betty``` from ```/tmp/holberton```.

* **9-firstdirdeletion**
  * Delete the directory ```holberton``` that is in the ```/tmp``` directory.

* **10-back**
  * Change the current working directory to the previous working directory.

* **11-lists**
  * List all files in the current directory, the parent directory, and the
    ```/boot``` directory (in this order), in long format.

* **12-file\_type**
  * Print the type of the file named ```iamafile``` in the ```/tmp``` directory.

* **13-symbolic\_link**
  * Create a symbolic link to ```/bin/ls```, named ```\_\_ls\_\_```, in the
    current directory.

* **14-copy\_html**
  * Copy all the HTML files from the current directory to the parent directory,
    but only copy files that did not exist in the parent directory or were newer
    than the versions in the parent directory.

* **15-lets\_move**
  * Move all files beginning with an uppercase letter to the directory
    ```/tmp/u```.

* **16-clean\_emacs**
  * Delete all files in the current directory that end with the character
    ```~```.

* **17-tree**
  * Create the directories ```welcome/```, ```welcome/to/``` and
    ```welcome/to/holberton``` in the current directory.

* **18-commas**
  * List all files and directories in the current directory, separated by commas
    (```.```), and as follows:
    * Directory names end with a slash (```/```)
    * Files and directories starting with a dot (```.```) are listed
    * The listing is alpha ordered, except for the directories ```.``` and
      ```..```, which are listed first
    * Only digits and letters are used to sort; digits come first
    * The listing ends with a new line
