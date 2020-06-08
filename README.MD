# 一個方便開始的空白專案
- 已包含虛擬環境、靜態文件、媒體文件、logging配置
- 靜態文件快取採用 ManifestStaticFilesStorage

安裝

- MySQL安裝
```
  $ sudo apt-get install -y libmysqlclient-dev
  $ pip install mysqlclient
```
- 修改設定
```
# wsgi.py
os.environ["DJANGO_SETTINGS_MODULE"] = "EmptyProject.settings"

# manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EmptyProject.settings")

# settings.py
ROOT_URLCONF = 'EmptyProject.urls'
WSGI_APPLICATION = 'EmptyProject.wsgi.application'
```
詳細安裝說明可參考[Django安裝筆記](https://hackmd.io/@njzhan/Sk7EFx5pB)