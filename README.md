<p align="center">
  <img src="logo.png" width="250"/>
</p>

`simqr` stands for `Simple QR`. It was built for educational purposes and supports only Version 1 QR code generation.

Usage
------
```console
git clone https://github.com/souvikshanku/simqr.git
cd simqr
pip install -r requirements.txt
cd src
```
```python
>>> from qr import draw
>>> draw("www.lichess.org")
```

Some aswesome resources that helped me get through this project -
* [Reed–Solomon codes for coders](https://en.wikiversity.org/wiki/Reed%E2%80%93Solomon_codes_for_coders)
* [Reed-Solomon Error Correcting Codes from the Bottom Up](https://tomverbeure.github.io/2022/08/07/Reed-Solomon.html)
* [Finite Field Arithmetic and Reed-Solomon Coding](https://research.swtch.com/field)
* [Encoding QR codes](https://observablehq.com/@zavierhenry/encoding-qr-codes)
