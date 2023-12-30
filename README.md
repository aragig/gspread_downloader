# Google Spreadsheets Download Manager with gspread on Python 3


## Installation

```bash
pip3 install git+https://github.com/aragig/gspread_downloader.git
```

### Requirements
- [gspread](https://docs.gspread.org/en/v5.12.0/)
- [oauth2client](https://pypi.org/project/oauth2client/)
 


事前にGoogle APIへ登録してclient_secret.jsonを取得しておく必要があります。[こちら](https://docs.gspread.org/en/latest/oauth2.html)を参考にしてください。
また、対象となるスプレッドシートを共有しておく必要があります。


## Usage

```python
import gspread_downloader  as gd

if __name__ == '__main__':
    client_secret = '/somewhere/client_secret.json'
    spreadsheet_title = 'スプレッドシートのタイトル'
    sheets = ['シート1', 'シート2']
    output_dir = '/somewhere/Desktop'

    gd.download(client_secret, spreadsheet_title, sheets, output_dir)
```
