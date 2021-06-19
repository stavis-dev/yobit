# Python YoBit Binding

Питонячая обретка для АПИ биржи [Ёбит](https://yobit.net/ru/api).

`Public API` и `Trade API` представляют собой удобное средство для взаимодействия с биржей стороннего программного обеспечения.

`Public API` используется для получения информации, не требующей доступа к личным данным аккаунта.

`Trade API` необходим для осуществления создания и отмены ордеров, запроса актуальных балансов, а так же получения информации, для которой необходим доступ к личным данным аккаунта.

## Installing / Установка

```bash
# from pip
pip install git+https://github.com/stavis-dev/yobit
```

## Usage / Использование

```python
from yobit import YoBit
yob = YoBit()
ticker = yob.ticker('xch_usd')
print(ticker)


# or find all chia pairs

info = yob.info()
for key in info['pairs']:
    if 'xch' in key:
        print(key)
```

## From original README

Python binding for YoBit. Use at your own risk!

Tips are appreciated: BTC 3NoXpUm2EeUWc1jJQhi5X7xKsneN9ReEpQ

All the comments and descriptions are at [offical YoBit API page](https://yobit.net/en/api) and in the code