import subprocess


def get_connected_devices():
    try:
        output = subprocess.check_output(['adb', 'devices']).decode('utf-8')
        devices = [line.split('\t')[0] for line in output.splitlines()[1:] if line.strip()]
        return devices
    except subprocess.CalledProcessError:
        return []


def android_get_desired_capabilities():
    devices = get_connected_devices()

    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8302,
        'takesScreenshot': True,
        'udid': devices[0] if devices else None,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
