import win32gui
import win32process
import win32con

def get_taskbar_apps():
    opened_apps = []

    def enum_windows_callback(hwnd, extra):
        # Only include visible windows
        if not win32gui.IsWindowVisible(hwnd):
            return True

        # Only include windows with text titles
        title = win32gui.GetWindowText(hwnd)
        if not title:
            return True

        # Skip child/owned windows (like popups or tooltips)
        if win32gui.GetWindow(hwnd, win32con.GW_OWNER):
            return True

        # Filter out Windows system shells and overlays
        # (e.g., Program Manager, Start Menu hosts)
        class_name = win32gui.GetClassName(hwnd)
        ignored_classes = ["Progman", "WorkerW", "Windows.UI.Core.CoreWindow"]
        if class_name in ignored_classes:
            return True

        opened_apps.append(title)
        return True

    # Enumerate through all top-level windows
    win32gui.EnumWindows(enum_windows_callback, None)
    return opened_apps

# Print the final list
apps = get_taskbar_apps()
print("Currently Open Taskbar Apps:\n" + "-"*30)
for app in apps:
    print(f"- {app}")
