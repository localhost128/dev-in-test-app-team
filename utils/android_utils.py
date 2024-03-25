def android_get_desired_capabilities():
    return {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
        "autoGrantPermissions": True,
        "newCommandTimeout": 500,
        "noSign": True,
        "resetKeyboard": True,
        "takesScreenshot": True,
        "systemPort": 8301,
    }
