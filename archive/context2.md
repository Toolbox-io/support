Toolbox.io — это надежный инструмент, который помогает защитить ваши приложения и данные на Android
от несанкционированного доступа. Он предлагает множество функций, которые делают вашу жизнь 
более безопасной и комфортной.

## Попробуйте это приложение
> [!NOTE]
> Это приложение может работать не на всех устройствах, поэтому, если оно работает неожиданно, отправьте сообщение на этот сайт.

Вы можете скачать это приложение [здесь](https://github.com/denis0001-dev/Toolbox-io-Website/releases/latest).

## Функции
### Приложение
- **Интуитивно понятный интерфейс.** Легко находите нужные вам инструменты через интуитивно понятный интерфейс.
- **Автоматические обновления.** В приложении есть проверка обновлений, поэтому вы никогда не пропустите
  новые версии. Вы можете обновить приложение прямо из интерфейса или загрузить последнюю версию по ссылке выше.
  Проверка обновлений происходит каждые 10 секунд. Если обнаружено обновление, вы получите уведомление.

### Защита
- **Блокировка приложений.** Установите пароль, чтобы ограничить доступ к определенным приложениям. Это обеспечит
  защиту ваших данных, личной информации и финансовой активности.

- **Действия при нескольких неудачных разблокировках.** Если кто-то не сможет разблокировать ваше устройство после
  двух попыток (можно настроить), можно настроить следующие действия:
    - Звуковой сигнал на 100% громкости (можно настроить мелодию).
    - Фото с фронтальной камеры.

  > **Внимание**<br/>
  > Для работы этой функции требуется разрешение администратора устройства, чтобы обнаружить попытки разблокировки.

- **Не трогайте мой телефон.** Эта функция поможет Вам защитить ваш телефон от физических прикосновений (например,
  когда кто-нибудь возьмет ваш телефон в руки).

  При попытке прикосновения будут выполнены те же действия, что и при срабатывании
  Защита блокировки.

  Использовать очень просто: Вы нажимаете кнопку в разделе, и после этого любое
  прикосновение к вашему телефону будет записано. Когда Вы захотите выключить эту
  защиту, просто нажмите "Стоп" и защита отключится.

### Кастомизация
- **Полезные плитки для быстрых настроек.** Быстрый доступ к важным функциям устройства через плитки в меню быстрых
  настроек. Например, с помощью плитки «Режим сна» вы можете временно отключить его до повторного включения.

  > **Внимание**<br/>
  > Не забудьте активировать режим сна обратно, иначе это может вызвать более быструю разрядку батареи.

- **Полезные ярлыки.** Быстрый доступ к скрытым приложениям. Например, скрытое приложение "Файлы" можно легко
  открыть через Toolbox.io. Просто перейдите в раздел Shortcuts и нажмите кнопку «Добавить» под кнопкой Files.
  Вы можете выбрать:
    - добавить как ярлык _(с водяным знаком)_
    - добавить как отдельное приложение _(без водяного знака)_.

### Инструменты
- **Менеджер приложений.** Эта функция позволяет:
  - делиться APK-файлом приложения, чтобы сделать резервную копию или отправить друзьям;
  - блокировать его с помощью Блокировки приложений, чтобы защитить конфиденциальную информацию;
  - получать дополнительную техническую информацию;
  - легко находить нужное приложение с помощью поиска по ключевым словам.
---

_Этот список постоянно расширяется и пополняется новыми возможностями._

## Прогресс разработки
Все мои достижения можно увидеть в [проекте на GitHub](https://github.com/users/denis0001-dev/projects/3).

## Поддержка
Если вам нужна помощь, вы нашли баг или хотите предложить новую функцию, свяжитесь со мной по электронной почте
denis0001.dev@ya.ru или отправьте запрос на GitHub.

## Совместимость
Toolbox.io совместим с Android 7 и выше. [Подробнее о совместимости](src/COMPATIBILITY.page.md).

## Конфиденциальность
- Никакие данные не собираются и не передаются третьим лицам.

### Разрешения
Toolbox.io **НИКОГДА** не использует разрешения без вашего согласия, только для указанных целей.

В приложении использованы следующие разрешения:

<table>
    <thead>
        <tr>
            <th scope="col">Название</th>
            <th scope="col">Техническое название</th>
            <th scope="col">Описание</th>
            <th scope="col">Для чего нужно</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <a href="https://developer.android.com/guide/topics/ui/accessibility/service">
                    Служба спец. возможностей
                </a>
            </td>
            <td>
                <code>android.permission.ACCESSIBILITY_SERVICE</code>
            </td>
            <td>
                Позволяет службам спец. возможностей работать
            </td>
            <td>
                Необходимо для корректной работы службы спец. возможностей
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#QUERY_ALL_PACKAGES">
                    Запрос всех пакетов
                </a>
            </td>
            <td>
                <code>android.permission.QUERY_ALL_PACKAGES</code>
            </td>
            <td>
                Позволяет приложению получать информацию о всех пакетах (приложениях),
                установленных на устройстве.
            </td>
            <td>
                Необходимо для корректной работы:
                <ul>
                    <li>Экрана выбора приложений в функции "Блокировка приложений;</li>
                    <li>извлечения APK.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#INTERNET">
                    Интернет
                </a>
            </td>
            <td>
                <code>android.permission.INTERNET</code>
            </td>
            <td>
                Позволяет приложению получать доступ в Интернет.
            </td>
            <td>
                Необходимо для корректной работы проверки обновлений.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES">
                    Запрос на установку приложений
                </a>
            </td>
            <td>
                <code>android.permission.REQUEST_INSTALL_PACKAGES</code>
            </td>
            <td>
                Позволяет приложению запрашивать установку других приложений.
            </td>
            <td>
                Необходимо для корректной работы установки обновлений.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS">
                    Уведомления
                </a>
            </td>
            <td>
                <code>android.permission.POST_NOTIFICATIONS</code>
            </td>
            <td>
                Позволяет приложению показывать уведомления.
            </td>
            <td>
                Необходимо для корректной работы обновлений и 
                <a href="https://developer.android.com/develop/background-work/services/fgs?skip_cache=true">
                    службы переднего плана
                </a> для поддержки работы 
                функций защиты.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE">
                    Службы переднего плана
                </a>
            </td>
            <td>
                <code>android.permission.FOREGROUND_SERVICE</code>
            </td>
            <td>
                Позволяет приложению запускать 
                <a href="https://developer.android.com/develop/background-work/services/fgs?skip_cache=true">
                    службы переднего плана
                </a>.
            </td>
            <td>
                Необходимо для корректной работы функций защиты.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#REQUEST_DELETE_PACKAGES">
                    Запросы на удаление приложений
                </a>
            </td>
            <td>
                <code>android.permission.REQUEST_DELETE_PACKAGES</code>
            </td>
            <td>
                Позволяет приложению запрашивать удаление приложений.
            </td>
            <td>
                Необходимо для корректной работы функции быстрого удаления приложения.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#CAMERA">
                    Камера
                </a>
            </td>
            <td>
                <code>android.permission.CAMERA</code>
            </td>
            <td>
                Позволяет приложению использовать камеру.
            </td>
            <td>
                Необходимо для корректной работы функции "Фото мошенника".
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#RECEIVE_BOOT_COMPLETED">
                    Запускатся после запуска
                </a>
            </td>
            <td>
                <code>android.permission.RECEIVE_BOOT_COMPLETED</code>
            </td>
            <td>
                Позволяет приложению запустится после запуска системы. Если есть пароль, то приложение будет
                запущено только тогда, когда пользователь разблокирует экран.
            </td>
            <td>
                Необходимо для корректной работы проверки обновлений.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CAMERA">
                    Служба переднего плана с камерой
                </a>
            </td>
            <td>
                <code>android.permission.FOREGROUND_SERVICE_CAMERA</code>
            </td>
            <td>
                Позволяет приложению использовать камеру в фоновом режиме с помощью 
                <a href="https://developer.android.com/develop/background-work/services/fgs?skip_cache=true">
                    службы переднего плана
                </a>.
            </td>
            <td>
                Необходимо для корректной работы функции "Фото мошенника".
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#VIBRATE">
                    Вибрация
                </a>
            </td>
            <td>
                <code>android.permission.VIBRATE</code>
            </td>
            <td>
                Позволяет приложению включать вибрацию телефона.
            </td>
            <td>
                Это разрешение нужно только для эффектов в приложении.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE">
                    Получение информации о сети
                </a>
            </td>
            <td>
                <code>android.permission.ACCESS_NETWORK_STATE</code>
            </td>
            <td>
                Позволяет приложению получать информацию о сети.
            </td>
            <td>
                Необходимо для правильной работы проверки обновлений.
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK">
                    Блокировка спящего режима
                </a>
            </td>
            <td>
                <code>android.permission.WAKE_LOCK</code>
            </td>
            <td>
                Позволяет приложению блокировать перход устройства в спящий режим.
            </td>
            <td>
                Необходимо для работы плитки "Спящий режим".
            </td>
        </tr>
    </tbody>
</table>

#### Вставка из [манифеста](https://developer.android.com/guide/topics/manifest/manifest-intro) приложения
```xml
<uses-permission android:name="android.permission.ACCESSIBILITY_SERVICE" />
<uses-permission
    android:name="android.permission.QUERY_ALL_PACKAGES"
    tools:ignore="QueryAllPackagesPermission" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.REQUEST_DELETE_PACKAGES" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_CAMERA" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

#### Дополнительные разрешения, использованные библиотекой [androidx-biometric](https://developer.android.com/jetpack/androidx/releases/biometric):
```xml
<uses-permission android:name="android.permission.USE_BIOMETRIC" />
<uses-permission android:name="android.permission.USE_FINGERPRINT" />
```
Эти разрешения использованы для биометрической аутентфикации в приложении.