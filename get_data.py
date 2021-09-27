from tqdm import tqdm
import requests
from pathlib import Path

urls = [
    "https://www.dropbox.com/s/r8q48mymk567f7a/chCourts.csv?dl=1",
    "https://www.dropbox.com/s/vdtfuuuvz7vt1mw/chPeople.csv?dl=1",
    "https://www.dropbox.com/s/lkp665czkrnuxyl/chPeopleCourts.csv?dl=1",
]

for url in urls:
    file_path = Path('data') / url.split('/')[-1].split('?')[0]
    if not file_path.exists():
        response = requests.get(url, stream=True)
        with open(file_path, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)
print('data downloaded')