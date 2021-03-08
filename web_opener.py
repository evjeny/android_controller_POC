import argparse
from appium import webdriver
from selenium.webdriver.common.keys import Keys


def main(args):
    desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': args.platform_version,  # device android info
        'deviceName': args.device_name, # device name from `adb devices`
        'browserName': 'Chrome',
        'chromedriverExecutableDir': 'chromedrivers',
        'chromedriverChromeMappingFile': 'chromedrivers/mappings.json'  # chrome to chrome driver version mappings
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.get('https://2ip.ru/')  # open page with your ip

    ip_element = driver.find_element_by_css_selector('.ip')  # local ip element
    ip_text = ip_element.find_element_by_css_selector('span').text  # get text of ip element

    with open("ip.txt", "w+") as f:
        f.write(ip_text)

    driver.save_screenshot("page.png")  # make screenshot of page

    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Android controller with Appium POC")
    parser.add_argument("--device_name", type=str, help="Name of Android device from `adb devices`")
    parser.add_argument("--platform_version", type=str, help="Version of Android on device")
    args = parser.parse_args()

    main(args)
