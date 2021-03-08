# Android controller with Appium

## Как это дело настроить

[Классный гайд](https://the-creative-tester.github.io/Python-Android-Mobile-Web-Automation/)

1. Скачать Android SDK (`sudo apt update && sudo apt install android-sdk`)
2. Установить путь к Android SDK в переменную окружения `ANDROID_SDK_ROOT`. Путь к SDK один из [следующих](https://stackoverflow.com/questions/34556884/how-to-install-android-sdk-on-ubuntu):
    - `/home/AccountName/Android/Sdk`
    - `/usr/lib/android-sdk`
    - `/Library/Android/sdk/`
    - `/Users/[USER]/Library/Android/sdk`
3. Скачать Java и установить соответствующий путь в переменную окружения `JAVA_HOME` (у меня по этому пути стоят и JDK, и JRE)
4. Установить npm (у меня версия `6.14.4`)
5. [Установить](https://github.com/appium/appium/issues/10020) Appium: `sudo npm install -g appium --unsafe-perm=true --allow-root`
6. Установить Python 3.7
7. Установить [обертку Appium](https://pypi.org/project/Appium-Python-Client/) для Python: `pip install Appium-Python-Client`
8. Узнать версию Android у девайса
9. Узнать имя девайся в ADB: `adb devices` (первая колонка)
10. Узнать версию Chrome на устройстве и найти соответствующий драйвер [на сайте](https://chromedriver.chromium.org/downloads). Записать полученные значения в файл `chromedrivers/mappings.json` (формат: `версия драйвера -> версия Chrome`)

## Как это дело запустить

1. Выполнить в консоли: `appium --allow-insecure chromedriver_autodownload`
2. Выполнить в другом окне консоли: `python web_opener.py --platform_version {версия Android} --device_name {имя девайся}` (пример можно посмотреть в файле `start.sh`)

## На что еще обратить внимание

1. Appium [по умолчанию работает с w3c](https://github.com/appium/appium/issues/13306), поэтому элементы можно искать только с помощью CSS-селекторов
