# Linux Based Notes

Things I usually don't remember


## LAMP

To start lamp, run the following command from it's folder

`./manager-linux-x64.run`

**PHPMyAdmin**

username: `root`
password: `admin123`

* Installed location: `/home/vivek/lampstack-7.3.11-0`
* Default url:        `127.0.0.1:8080`
* Webserver location: `/home/vivek/lampstack-7.3.11-0/apache2/htdocs/`
* Wordpress Creds: `admin` / `admin`

It has the following software installed

- PHPMyAdmin
- Laravel
- CodeIgniter
- Varnish (server accelerator)


## Virual Environment for Python

Run the following command from a project folder that you want to run a virtual
environment for

```bash
$ python -m venv env_name
$ source env_name/bin/activate
```

To come out of the environment simply run

```bash
$ deactivate
```

I can even create short-hand commands to do this

```bash
alias ae='deactivate &> /dev/null; source ./venv/bin/activate'
alias de='deactivate'
```

**Usage**
```bash
$ cd project
$ ae
# work on project
$ de
```

---

## Blog Related

To start the jekyll blog run the following command from the jekyll blog directory

```bash
$ bundle exec jekyll serve
```

Here are a list of commands I need

* `blog start` - should start the blog using `jekyll serve`
* `blog draft` - should create new file in the `_drafts` directory and open using sublime text
* `blog new --name hello-post`   - create new post in the `_posts` directory with default date stamp followed by `hello-post` in file name.
* `blog publish` - should commit & push to origin master branch on github


---

Andorid SDK         = `/opt/android_sdk`
Android Studio      = `/opt/android-studio`
                    = `/opt/android-studio/bin/studio.sh`