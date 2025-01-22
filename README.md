# frederikring.com
> Source code for my personal homepage

This page uses the [Pelican](https://getpelican.com/) static site generator, which means you will need to have Python installed on your setup.

## Installing dependenices

```console
$ pip install -r requirements.txt
```

## Running the local dev server

```console
$ pelican -r -l
```

## Deployment

The static assets are built and deployed to GitHub Pages from GitHub Actions.
