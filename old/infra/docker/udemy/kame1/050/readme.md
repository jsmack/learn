# ENTRYPOINT instruction
- CMD and ENTORYPOINT are closely related
## What is the defference between CMD and ENTORYPOINT
- Can I override the default command use run for run?
  - CMD can
  - ENTORYPOINT cannnot
    - There is a means, but it is rarely used
    - Use `--entorypoint` option

## What do you use ENTORYPOINT?
- Use this when you do not want to change the default command


## Example
- CMD
```Dockerfile
FROM ubuntu:latest
RUN touch hoge
CMD ["ls", "--help"]
```
- ls --help is overwritten by pwd and pwd is executed
```bash
>>> docker run <image pwd
```

- ENTORPYPOINT
```Dockerfile
FROM ubuntu:latest
RUN touch hoge
ENTORYPOINT ["ls"]
CMD ["--help"]
```

- --help is overwritten by pwd and `ls pwd` is executed
- However, ls command does not exist pwd file or directory.
```
>>> docker run <image> pwd
>>>
```
- So use it when you want to change options etc.
- This docker command is executed `ls -la` command
```
>>> docker run <image> -la
>>>
```
## TEST
```bash
>>> cat Dockerfile
FROM ubuntu:latest

RUN touch test

ENTRYPOINT [ "ls" ]

CMD [ "--help" ]
>>>
>>> docker build .
Sending build context to Docker daemon  4.096kB
Step 1/4 : FROM ubuntu:latest
 ---> f643c72bc252
Step 2/4 : RUN touch test
 ---> Using cache
 ---> aaf7263913df
Step 3/4 : ENTRYPOINT [ "ls" ]
 ---> Using cache
 ---> a8b2cf9ea058
Step 4/4 : CMD [ "--help" ]
 ---> Using cache
 ---> 579639d4acfc
Successfully built 579639d4acfc
>>>
```
## Result
- Not override default command
  - Success because you have not overwritten the default command
  - <details>
    <summary>Result</summary>

    ```bash
    >>> docker run 579639d4acfc
    Usage: ls [OPTION]... [FILE]...
    List information about the FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
    -a, --all                  do not ignore entries starting with .
    -A, --almost-all           do not list implied . and ..
        --author               with -l, print the author of each file
    -b, --escape               print C-style escapes for nongraphic characters
        --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                                e.g., '--block-size=M'; see SIZE format below
    -B, --ignore-backups       do not list implied entries ending with ~
    -c                         with -lt: sort by, and show, ctime (time of last
                                modification of file status information);
                                with -l: show ctime and sort by name;
                                otherwise: sort by ctime, newest first
    -C                         list entries by columns
        --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                                if omitted), 'auto', or 'never'; more info below
    -d, --directory            list directories themselves, not their contents
    -D, --dired                generate output designed for Emacs' dired mode
    -f                         do not sort, enable -aU, disable -ls --color
    -F, --classify             append indicator (one of */=>@|) to entries
        --file-type            likewise, except do not append '*'
        --format=WORD          across -x, commas -m, horizontal -x, long -l,
                                single-column -1, verbose -l, vertical -C
        --full-time            like -l --time-style=full-iso
    -g                         like -l, but do not list owner
        --group-directories-first
                                group directories before files;
                                can be augmented with a --sort option, but any
                                use of --sort=none (-U) disables grouping
    -G, --no-group             in a long listing, don't print group names
    -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
        --si                   likewise, but use powers of 1000 not 1024
    -H, --dereference-command-line
                                follow symbolic links listed on the command line
        --dereference-command-line-symlink-to-dir
                                follow each command line symbolic link
                                that points to a directory
        --hide=PATTERN         do not list implied entries matching shell PATTERN
                                (overridden by -a or -A)
        --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                                (default if omitted), 'auto', or 'never'
        --indicator-style=WORD  append indicator with style WORD to entry names:
                                none (default), slash (-p),
                                file-type (--file-type), classify (-F)
    -i, --inode                print the index number of each file
    -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
    -k, --kibibytes            default to 1024-byte blocks for disk usage;
                                used only with -s and per directory totals
    -l                         use a long listing format
    -L, --dereference          when showing file information for a symbolic
                                link, show information for the file the link
                                references rather than for the link itself
    -m                         fill width with a comma separated list of entries
    -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
    -N, --literal              print entry names without quoting
    -o                         like -l, but do not list group information
    -p, --indicator-style=slash
                                append / indicator to directories
    -q, --hide-control-chars   print ? instead of nongraphic characters
        --show-control-chars   show nongraphic characters as-is (the default,
                                unless program is 'ls' and output is a terminal)
    -Q, --quote-name           enclose entry names in double quotes
        --quoting-style=WORD   use quoting style WORD for entry names:
                                literal, locale, shell, shell-always,
                                shell-escape, shell-escape-always, c, escape
                                (overrides QUOTING_STYLE environment variable)
    -r, --reverse              reverse order while sorting
    -R, --recursive            list subdirectories recursively
    -s, --size                 print the allocated size of each file, in blocks
    -S                         sort by file size, largest first
        --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                                time (-t), version (-v), extension (-X)
        --time=WORD            with -l, show time as WORD instead of default
                                modification time: atime or access or use (-u);
                                ctime or status (-c); also use specified time
                                as sort key if --sort=time (newest first)
        --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
    -t                         sort by modification time, newest first
    -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
    -u                         with -lt: sort by, and show, access time;
                                with -l: show access time and sort by name;
                                otherwise: sort by access time, newest first
    -U                         do not sort; list entries in directory order
    -v                         natural sort of (version) numbers within text
    -w, --width=COLS           set output width to COLS.  0 means no limit
    -x                         list entries by lines instead of by columns
    -X                         sort alphabetically by entry extension
    -Z, --context              print any security context of each file
    -1                         list one file per line.  Avoid '\n' with -q or -b
        --help     display this help and exit
        --version  output version information and exit

    The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
    Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

    The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
    FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
    then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
    TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
    Also the TIME_STYLE environment variable sets the default style to use.

    Using color to distinguish file types is disabled both by default and
    with --color=never.  With --color=auto, ls emits color codes only when
    standard output is connected to a terminal.  The LS_COLORS environment
    variable can change the settings.  Use the dircolors command to set it.

    Exit status:
    0  if OK,
    1  if minor problems (e.g., cannot access subdirectory),
    2  if serious trouble (e.g., cannot access command-line argument).

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Report ls translation bugs to <https://translationproject.org/team/>
    Full documentation at: <https://www.gnu.org/software/coreutils/ls>
    or available locally via: info '(coreutils) ls invocation'
    >>>
    ```
</details>


- Override default command is pwd
  -  An error occurs because the directory or file with the name of pwd does not exist
  - <details>
    <summary>Result</summary>

    ```bash
    >>> docker run 579639d4acfc pwd
    ls: cannot access 'pwd': No such file or directory
    >>>
    ```
</details>

- Override default command is /
  -  Success because the / directory existspwd does not exist
  - <details>
    <summary>Result</summary>

    ```bash
    >>>  docker run 579639d4acfc /
    bin
    boot
    dev
    etc
    home
    lib
    lib32
    lib64
    libx32
    media
    mnt
    opt
    proc
    root
    run
    sbin
    srv
    sys
    test
    tmp
    usr
    var
    >>>
    ```
</details>

- Override default command is -la
  -  The -la option succeeds because it exists in the ls command
  - <details>
    <summary>Result</summary>

    ```bash
    >>> docker run 579639d4acfc -la
    total 56
    drwxr-xr-x   1 root root 4096 Dec 31 08:41 .
    drwxr-xr-x   1 root root 4096 Dec 31 08:41 ..
    -rwxr-xr-x   1 root root    0 Dec 31 08:41 .dockerenv
    lrwxrwxrwx   1 root root    7 Nov  6 01:21 bin -> usr/bin
    drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
    drwxr-xr-x   5 root root  340 Dec 31 08:41 dev
    drwxr-xr-x   1 root root 4096 Dec 31 08:41 etc
    drwxr-xr-x   2 root root 4096 Apr 15  2020 home
    lrwxrwxrwx   1 root root    7 Nov  6 01:21 lib -> usr/lib
    lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib32 -> usr/lib32
    lrwxrwxrwx   1 root root    9 Nov  6 01:21 lib64 -> usr/lib64
    lrwxrwxrwx   1 root root   10 Nov  6 01:21 libx32 -> usr/libx32
    drwxr-xr-x   2 root root 4096 Nov  6 01:21 media
    drwxr-xr-x   2 root root 4096 Nov  6 01:21 mnt
    drwxr-xr-x   2 root root 4096 Nov  6 01:21 opt
    dr-xr-xr-x 112 root root    0 Dec 31 08:41 proc
    drwx------   2 root root 4096 Nov  6 01:25 root
    drwxr-xr-x   1 root root 4096 Nov 25 22:25 run
    lrwxrwxrwx   1 root root    8 Nov  6 01:21 sbin -> usr/sbin
    drwxr-xr-x   2 root root 4096 Nov  6 01:21 srv
    dr-xr-xr-x  13 root root    0 Dec 31 08:36 sys
    -rw-r--r--   1 root root    0 Dec 21 13:17 test
    drwxrwxrwt   2 root root 4096 Nov  6 01:25 tmp
    drwxr-xr-x   1 root root 4096 Nov  6 01:21 usr
    drwxr-xr-x   1 root root 4096 Nov  6 01:25 var
    >>>
    ```
</details>

