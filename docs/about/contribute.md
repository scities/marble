# Contribute

Contributions in the form of bugfixes, documentation or new features are more
than welcome! Here are the steps to follow when contributing some code to the
Marble repository.

## Fork marble and clone

Go on [Marble](http://scities.github.com/marble) and click on the `fork` button
to create your own fork of the repository (you will need a Github account).

Now you can clone the repository locally to work on it. Assuming your username
is **username**, cd in your console to the directory where you want the code to
be downloaded and type

```bash
git clone https://username.github.com/marble.git
```

the code of Marble now sits in the folder "marble".

## Create a new branch

**Before** making any change to the code, please create a separate branch, with
a name that makes an explicit reference to the modification you are trying to
make. If you want to make several modifications (say a bugfix, and a new
feature), create as many separate branches as necessary. For instance

```bash
git checkout -b new_code
```

## Push your changes and make a pull request

To push your branch to your forked repository, type

```bash
git push origin new_code
```

Now you can go to your forked project github page and issue a pull request from
there. Please describe the changes that you made in the Pull Request, and
reference the issues you are adressing (if any)!

Thanks!

