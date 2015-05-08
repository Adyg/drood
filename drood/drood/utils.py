def _remove_attrs(soup):
    """
    Remove all attributes in an BeautifulSoup object
    """
    allowed_attributes = ['src', 'href']
    blacklist_tags = ['input', 'script']

    for tag in soup.findAll(True):
        if tag.attrs:
            clean_attrs = {}
            for attr in tag.attrs:
                if attr in allowed_attributes:
                    clean_attrs[attr] = tag.attrs[attr]
            if tag.name == 'a':
                clean_attrs['target'] = '_blank'

            tag.attrs = clean_attrs

    return soup
