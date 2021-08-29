# heavy rain alert notification system

edit: Aug28, 2021, ms

からheavy rain alert SMSがとどいたときに作動するnotification systemを作っている。

raspiZW2にadafruitのAdafruit 16-Channel PWM / Servo Bonnet for Raspberry Piをのせ、そこからAW9523 GPIO expanderをI2Cでつないでいる。

## LED-test.py

まずはすべてのLEDがきちんとつくのかをテストするためのコード。そもそもLEDをどうやってon-offするのかの確認コードでもある。



