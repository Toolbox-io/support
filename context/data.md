# Toolbox.io

Toolbox.io is a reliable tool that helps protect your Android apps and data from unauthorized access. It offers many features that make your life safer and more comfortable.

---

## Features

### App Lock
Protects your apps from unauthorized access by showing a fake crash message to intruders.  
When you try to open a protected app, it closes and displays an error message. This is not a real error, but a trick to confuse the intruder.

To unlock the app, use the selected unlock method. By default, this is a long press of the "About" button, but you can change this in the App Lock settings.  
You can read how to use this feature in the guide: [How to Lock Apps](guides/how_to_lock_apps).

#### How to use App Lock
1. Open Toolbox.io and go to the **App Lock** section.
2. Tap the **Enable** switch at the top.
3. Grant Accessibility permission when prompted. This is required to detect which app is open and to close protected apps.
4. Select the apps you want to protect.
5. Tap the checkmark in the bottom right corner.

**Notes:**
- The default password is empty. If you have not set a password, leave the password field blank and press OK.
- For best results, enable the "Foreground service for accessibility" option in settings. This keeps the feature running until you reboot your device.
- To disable the persistent notification, long-press it and select "Turn off notifications".

### Unlock Protection
Performs actions if someone repeatedly fails to unlock your phone.

#### Available Actions:
- **Alarm:** Plays an alarm sound at 100% volume. Attempts to change the volume are blocked.
- **Photo of intruder:** Takes a photo of the person trying to unlock your device using the front camera.

**Notes:**
- Device administrator permission is required for this feature to work. This is needed to detect failed unlock attempts and perform the required actions.
- On Android 12 and above, a green dot will appear in the top right corner when the camera is used. This is a system feature, not a problem with the app.

#### How to use Unlock Protection
1. Open Toolbox.io and go to the **Unlock Protection** section.
2. Tap **Enable** at the top and grant device administrator permission.
3. Open **Actions** and enable the actions you want.

### Don't Touch My Phone
Helps protect your phone from unauthorized physical touch (e.g., when someone picks up your phone).  
When triggered, the same actions as Unlock Protection are performed.

How to use:
- Press the button in the section to enable protection. Any touch will be recorded.
- To disable, press "Stop".

### Tiles
Useful quick settings tiles for fast access to important device functions.  
For example, the Sleep Mode tile temporarily disables sleep mode until you turn it back on.

**Warning:**  
If you forget to re-enable sleep mode, your battery may drain faster.

### Shortcuts
Quick access to hidden apps and system features.  
For example, you can access the hidden Files app by going to the Shortcuts section and adding a shortcut for "Files".

### Application Manager
Manage your apps easily:
- Share APK files for backup or sharing.
- Block apps with App Lock to protect confidential information.
- View technical information.
- Find apps quickly using keyword search.

---

## Requirements

- **Operating System:** Android 7 or higher. No other operating systems are supported.
- **Device:** No specific device model is required. Any device running Android 7+ should work.
- **Installation:** Download and install the APK from the official website. No device selection is needed.

---

## Tested Devices

The following devices have been tested:

**Fully Working:**
- Samsung Galaxy Tab A9+ (Android 14, Toolbox.io 2.0)
- Google Pixel 8 Pro emulator (Android 16, Toolbox.io 2.0)
- Blackview A95 (Android 11, Toolbox.io 2.0)

**Works with Issues:**
- Xiaomi Redmi Note 11 (Android 13, Toolbox.io 1.7.5)

---

## Download

You can download Toolbox.io from the official website: https://beta.toolbox-io.ru/download

---

## FAQ

**Q: What is Toolbox.io?**  
A: Toolbox.io is a security app for Android that protects your apps and data from unauthorized access.

**Q: How do I download Toolbox.io?**  
A: Go to https://beta.toolbox-io.ru/download and download the APK file. Toolbox.io only supports Android (version 7 or above). No device selection is needed—just download and install.

**Q: What devices are supported?**  
A: Toolbox.io works on any Android device running Android 7 or above. See the 'Tested Devices' section for a list of devices that have been officially tested.

**Q: What permissions are required for App Lock?**  
A: Accessibility permission is required for App Lock to detect and close protected apps.

**Q: What permissions are required for Unlock Protection?**  
A: Device administrator permission is required to detect failed unlock attempts and perform actions. Camera permission is required to take a photo of the intruder.

**Q: Is my data shared with third parties?**  
A: No, Toolbox.io does not collect or share your data with third parties.

---

## Support

If you need help, found a bug, or want to suggest a new feature, contact:  
Email: denis0001.dev@ya.ru  
GitHub project: https://github.com/users/denis0001-dev/projects/3

---

## Progress

All development progress can be seen in the [GitHub project](https://github.com/orgs/Toolbox-io/projects/1).

---

## Guides

### How to Use App Lock

App Lock is a feature designed to protect your apps from unauthorized access.  
When someone tries to open a protected app, they will see a fake crash message.  
To unlock the app, long-press the "About" button and enter your password (the default password is empty).

**How to enable App Lock:**
1. Open Toolbox.io and go to the App Lock section.
2. Tap "Enable" at the top.
3. Grant Accessibility permission when prompted.
4. Select the apps you want to protect.
5. Tap the checkmark in the bottom right corner.

**Tips:**
- For best results, enable the "Foreground service for accessibility" option in settings.
- To disable the persistent notification, long-press it and select "Turn off notifications".

### How to Use Unlock Protection

Unlock Protection is a feature that protects you from physical intruders.  
It allows you to perform certain actions after several failed unlock attempts, such as sounding an alarm or taking a photo of the intruder.

**How to enable Unlock Protection:**
1. Open Toolbox.io and go to the Unlock Protection section.
2. Tap "Enable" at the top and grant device administrator permission.
3. Open "Actions" and enable the actions you want.

**Available actions:**
- Alarm: Plays a sound at 100% volume (cannot be changed).
- Photo of intruder: Takes a photo using the front camera.

**Notes:**
- On Android 12 and above, a green dot will appear when the camera is used. This is a system feature.
- Device administrator permission is required for this feature.

---
