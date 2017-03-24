cookie-crunch
==========

Quick library built to simplify the decoding of Flask session cookies

Installation
----
```sh
$ pip install cookie_crunch
```


```sh
$ python setup.py install
```


Usage
----

```
In [1]: from cookie_crunch.flask import decode

In [2]: cookie = '.eJxdjUFrgzAYQP_KyLmHTdqL0MNADRSSEPi0xotoEptq0pXE0ZrS_75ug8J2fo_3bqgdvA4GpUNng14hGfzQzh-TPqH0hl56lCLi8kgTHikWF7GvXANlpKAMcSJpQK7ZvphoJq4Ml2sGxtJ4WBq-3aL7Cg1HH-b21Dn9zHFnQ__-i233n0JdLdIVm28atPR6bs9dCBf1NESSJxT4G4PHFhcjA_lKgEcG-YZkyrHssIiRjiQrfx6fQfs_C4WNla4yPd6de3ydVb1bRD095PsXaGlY1A.C7YVqQ.cveR6ObYBeQ4iBhj_34x2hKyYeQ'

In [3]: decode(cookie)
Out[3]:
{u'_fresh': False,
 u'csrf_token': '2a37d34f0aefe5357a2f6e789ad4618e898e782e',
 u'first_name': 'Bill',
 u'last_name': 'Murray',
 u'secret_passwd': 'ca654591d4ac97414391907f882b3c05',
 u'username': 'therealbillmurray'}
```
