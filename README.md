![Version - 1.4](https://img.shields.io/badge/Version-1.4-blue?style=for-the-badge)
[![Build Status](https://img.shields.io/github/forks/soyandrey/AG-HUB.svg?style=for-the-badge)](https://github.com/soyandrey/AG-HUB)
[![Build Status](https://img.shields.io/github/stars/soyandrey/AG-HUB.svg?style=for-the-badge)](https://github.com/soyandrey/AG-HUB)
# Blackslash™ Nuker

<h1 allign="center">- Features -</h1>

* ` Delete Chanels, Emojis & Roles`
* ` Mass Create Channels `
* ` Spam Channels `
* ` Mass Role Create `
* ` Mass DM`
* ` Dm owner`
* `Customization`
* ` Blacklist Guilds `
  
# Installation 
### Installation
- Open the [Releases](https://github.com/skeqt/AveryNuker/releases) Page.
- Click on the latest version.
- Click on the `BSNuker.py`.
  
### How to use
```py
import BSNuker
```
a example can be found in [``example.py``](https://github.com/soyandrey/Blackslash-Nuker/blob/main/example.py)
# Documentetion

## Main
  - ## ``setconfig( <config_file> )``

## Raider
  - ## ``DeleteChannels( <guild> )``
     * Delete all guild Channels
  - ## ``DeleteRoles( <guild> )``
     * Delete all guild Roles
  - ## ``DeleteEmojis( <guild> )``
     * Delete all guild Emojis
  - ## ``ChangeName( <guild> )``
    * Change the name of the guild
    * ``config.NAME``: The new name for the guild 
  - ## ``ChangeIcon( <guild> )``
    * Change the guild Icon
    * ``config.ICON``: The new icon for the guild
  - ## ``CreateInvites( <guild> )``
     * Create invites for all the channels
  - ## ``CreateChannels( <guild>, <amount>)``
     * Mass Create Channels
     * ``config.SPAM_CHANNEL``: The name of the Channels
  - ## ``CreateRoles( <guild> )`` 
     * Mass Create Roles
     * ``config.ROLE_NAME``: The name of the roles
  - ## ``DMAll( <guild> )`` 
     * DMs all users in the server
     *  ``config.DM_MESSAGE``: The message that will be sended to every user
## Helpers
   - ## ``help_msg(   )`` 
     * Print the commands of the bot


