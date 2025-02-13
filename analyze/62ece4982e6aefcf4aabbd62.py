def _replace_url_args(url, url_args):
    if url_args:
        for key, value in url_args.items():
            url = url.replace(f'{{{key}}}', str(value))
    return url