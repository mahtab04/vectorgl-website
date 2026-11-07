from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, attrs['id']
            self.ids.add(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])

root = Path(__file__).resolve().parents[1] / 'site'
pages = {p.resolve(): Page(p) for p in root.glob('*.html')}
assert len(pages) == 5, 'Expected all five website pages'
count = 0
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.exists(), (path.name, link)
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, (path.name, link)
        count += 1
print(f'Passed: {len(pages)} HTML pages, {count} local asset/anchor links, unique IDs.')
